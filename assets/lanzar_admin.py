import os
import threading
import webview

# Importación limpia que el editor reconoce de inmediato (adiós al amarillo)
from assets.app import app, db

# Definir rutas absolutas para las plantillas y la base de datos
base_path = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_path, 'assets')
app.template_folder = os.path.join(assets_dir, 'templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(assets_dir, "instance", "database.db")}'

def iniciar_servidor():
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # Arrancar Flask en segundo plano
    t = threading.Thread(target=iniciar_servidor)
    t.daemon = True
    t.start()

    # Abrir ventana nativa de escritorio
    webview.create_window('Identificador de Placas - Escáner', 'http://localhost:5000/', width=900, height=700)
    webview.start()