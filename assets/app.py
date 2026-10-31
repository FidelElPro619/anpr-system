import re
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Placa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    propietario = db.Column(db.String(100), nullable=True)
    pais = db.Column(db.String(5), nullable=False, default='CO')

with app.app_context():
    db.create_all()

def extraer_placa_valida(texto, pais_filtro='ALL'):
    limpio = re.sub(r'[^A-Z0-9-]', '', texto.upper())
    solo_alfanum = re.sub(r'[^A-Z0-9]', '', limpio)

    if pais_filtro in ('ALL', 'CO'):
        match_co = re.search(r'(?<![A-Z])([A-Z]{3})-?([0-9]{3})(?![0-9])', limpio)
        if match_co:
            return f"{match_co.group(1)}-{match_co.group(2)}", 'CO'

        num_a_letra = {'0': 'O', '1': 'I', '2': 'Z', '5': 'S', '8': 'B'}
        letra_a_num = {'O': '0', 'Q': '0', 'D': '0', 'I': '1', 'L': '1', 'Z': '2', 'S': '5', 'B': '8'}
        if len(solo_alfanum) >= 6:
            for i in range(len(solo_alfanum) - 5):
                bloque = solo_alfanum[i:i+6]
                p_letras, p_nums = bloque[:3], bloque[3:]
                if sum(c.isalpha() for c in p_letras) >= 2 and sum(c.isdigit() for c in p_nums) >= 2:
                    l_ok = ''.join(num_a_letra.get(c, c) for c in p_letras)
                    n_ok = ''.join(letra_a_num.get(c, c) for c in p_nums)
                    if l_ok.isalpha() and n_ok.isdigit():
                        return f"{l_ok}-{n_ok}", 'CO'

    if pais_filtro in ('ALL', 'JP'):
        match_jp = re.search(r'(?<![0-9])([0-9]{2})-([0-9]{2})(?![0-9])', limpio)
        if match_jp:
            return f"{match_jp.group(1)}-{match_jp.group(2)}", 'JP'
        if pais_filtro == 'JP' and len(solo_alfanum) == 4 and solo_alfanum.isdigit():
            return f"{solo_alfanum[:2]}-{solo_alfanum[2:]}", 'JP'

    if pais_filtro in ('ALL', 'US'):
        match_us_ca = re.search(r'([0-9][A-Z]{3}[0-9]{3})', solo_alfanum)
        if match_us_ca:
            return match_us_ca.group(1), 'US'
        if 6 <= len(solo_alfanum) <= 7 and any(c.isalpha() for c in solo_alfanum) and any(c.isdigit() for c in solo_alfanum):
            return solo_alfanum, 'US'

    return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        entrada = request.form.get('numero', '').upper().strip()
        propietario = request.form.get('propietario', '').strip()
        pais_sel = request.form.get('pais', 'CO').upper().strip()

        placa_fmt, _ = extraer_placa_valida(entrada, pais_sel)
        placa_final = placa_fmt or entrada

        if placa_final:
            existente = Placa.query.filter_by(numero=placa_final).first()
            if not existente:
                nueva = Placa(numero=placa_final, propietario=propietario, pais=pais_sel)
                db.session.add(nueva)
                db.session.commit()
        return redirect(url_for('admin'))

    placas = Placa.query.all()
    return render_template('admin.html', placas=placas)

@app.route('/admin/eliminar/<int:id>')
def eliminar(id):
    placa = Placa.query.get_or_404(id)
    db.session.delete(placa)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/api/verificar_rapido', methods=['POST'])
def verificar_rapido():
    data = request.json or {}
    textos_detectados = data.get('textos', [])
    pais_escaner = data.get('pais_filtro', 'ALL')

    candidatos = []
    for item in textos_detectados:
        placa_limpia, pais_det = extraer_placa_valida(item, pais_escaner)
        if placa_limpia and (placa_limpia, pais_det) not in candidatos:
            candidatos.append((placa_limpia, pais_det))

    if not candidatos:
        return jsonify({"detectada": False})

    placas_db = Placa.query.all()

    for placa_cand, pais_cand in candidatos:
        sin_guion_cand = re.sub(r'[^A-Z0-9]', '', placa_cand)
        for p in placas_db:
            sin_guion_db = re.sub(r'[^A-Z0-9]', '', p.numero.upper())
            if sin_guion_db == sin_guion_cand:
                return jsonify({
                    "detectada": True,
                    "status": "ACEPTADO",
                    "placa": p.numero,
                    "pais": p.pais,
                    "propietario": p.propietario or "Sin nombre",
                    "mensaje": f"Acceso autorizado a: {p.propietario or 'Vehículo Registrado'}."
                })

    placa_rechazada, pais_rechazado = candidatos[0]
    return jsonify({
        "detectada": True,
        "status": "DENEGADO",
        "placa": placa_rechazada,
        "pais": pais_rechazado,
        "mensaje": f"La placa {placa_rechazada} NO está registrada en el sistema."
    })

if __name__ == '__main__':
    app.run(debug=True)