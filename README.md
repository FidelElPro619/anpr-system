# 🚗 Sistema ANPR de Control Vehicular (Identificador de Placas)
# ANPR Vehicle Control System
# 自動車ナンバープレート認識（ANPR）システム

[🇪🇸 Español](#español) | [🇺🇸 English](#english) | [🇯🇵 日本語](#japanese)

---

<a name="español"></a>
## 🇪🇸 Español: Documentación del Proyecto

### 📌 Descripción General
Aplicación web y de escritorio desarrollada en **Python (Flask)** y tecnologías web modernas que implementa un sistema de **Reconocimiento Automático de Placas (ANPR)** en tiempo real. Está diseñada para el control de accesos vehiculares, permitiendo escanear matrículas mediante la cámara web, validar formatos internacionales estrictos (Colombia, Japón y Estados Unidos) con autocorrección, y gestionar un panel de administración completo con persistencia en base de datos SQLite.

### 🛠️ Tecnologías Utilizadas
* **Backend:** Python, Flask, Flask-SQLAlchemy, SQLite, PyWebView (para modo escritorio nativo).
* **Frontend:** HTML5, Bootstrap 4, Argon Design System, Tesseract.js (para OCR directo en el navegador).
* **Empaquetado:** PyInstaller (para generar ejecutables `.exe` independientes de escritorio).

### ✨ Características Principales
1. **Escaneo en Tiempo Real:** Seguimiento por cámara con cuadros delimitadores (*bounding boxes*) y procesamiento OCR rápido.
2. **Soporte Multipaís y Autocorrector:** Validación de formatos vehiculares para:
   * 🇨🇴 **Colombia:** Formato estándar alfanumérico.
   * 🇯🇵 **Japón:** Formato de prefecturas y numeración nipona.
   * 🇺🇸 **Estados Unidos:** Formatos por estado.
3. **Panel de Administración (CRUD):** Interfaz segura para registrar nuevas placas, asignar propietarios, asociar países y eliminar registros.
4. **Internacionalización (i18n):** Soporte completo para **Español, Inglés y Japonés** con almacenamiento persistente (`localStorage`).
5. **Aplicación de Escritorio Independiente:** Capacidad de compilarse en archivos `.exe` separados (`lanzar_index.exe` y `lanzar_admin.exe`) sin requerir instalaciones previas ni consola visible.

---

<a name="english"></a>
## 🇺🇸 English: Project Documentation

### 📌 Overview
Web and desktop application built with **Python (Flask)** and modern web technologies that implements a real-time **Automatic License Plate Recognition (ANPR)** system. Designed for vehicular access control, it allows scanning license plates via webcam, validating strict international formats (Colombia, Japan, USA) with autocorrect, and managing a complete administration dashboard backed by SQLite.

### 🛠️ Tech Stack
* **Backend:** Python, Flask, Flask-SQLAlchemy, SQLite, PyWebView (for native desktop mode).
* **Frontend:** HTML5, Bootstrap 4, Argon Design System, Tesseract.js (for browser-side OCR).
* **Packaging:** PyInstaller (to generate standalone `.exe` desktop executables).

### ✨ Key Features
1. **Real-time Scanning:** Live camera tracking with bounding boxes and high-speed OCR processing.
2. **Multi-Country & Autocorrect Support:** Format validation for:
   * 🇨🇴 **Colombia:** Standard alphanumeric format.
   * 🇯🇵 **Japan:** Prefecture and Japanese numbering format.
   * 🇺🇸 **USA:** State-based formats.
3. **Admin Dashboard (CRUD):** Secure interface to register new plates, assign owners, link countries, and delete records.
4. **Internationalization (i18n):** Full support for **Spanish, English, and Japanese** with persistent storage (`localStorage`).
5. **Standalone Desktop Apps:** Compiled into independent `.exe` files (`lanzar_index.exe` and `lanzar_admin.exe`) running natively without browser dependencies or console windows.

---

<a name="japanese"></a>
## 🇯🇵 日本語: プロジェクトドキュメント

### 📌 概要
**Python (Flask)** と最新のWebテクノロジーを使用して開発された、リアルタイムの**自動車ナンバープレート認識（ANPR）**システムです。車両入退室管理向けに設計されており、Webカメラでプレートをスキャンし、厳格な国際フォーマット（コロンビア、日本、アメリカ）を自動修正機能付きで検証し、SQLiteデータベースを備えた完全な管理ダッシュボードを提供します。

### 🛠️ 技術スタック
* **バックエンド:** Python, Flask, Flask-SQLAlchemy, SQLite, PyWebView（ネイティブデスクトップモード用）
* **フロントエンド:** HTML5, Bootstrap 4, Argon Design System, Tesseract.js（ブラウザ側OCR用）
* **パッケージング:** PyInstaller（独立した `.exe` デスクトップ実行ファイルの生成用）

### ✨ 主な機能
1. **リアルタイムスキャン:** バウンディングボックス付きのライブカメラ追跡と高速OCR処理。
2. **マルチ国・自動修正サポート:** 次のフォーマットの検証:
   * 🇨🇴 **コロンビア:** 標準英数字フォーマット。
   * 🇯🇵 **日本:** 地域名・分類番号・ひらがな・一連指定番号のフォーマット。
   * 🇺🇸 **アメリカ:** 州ごとのフォーマット。
3. **管理ダッシュボード (CRUD):** 新しいプレートの登録、所有者の割り当て、国の紐付け、およびレコードの削除を行うための安全なインターフェース。
4. **多言語対応 (i18n):** `localStorage` による永続化を備えた **スペイン語、英語、日本語** の完全サポート。
5. **スタンドアロンデスクトップアプリ:** ブラウザの依存関係やコンソールウィンドウなしでネイティブ実行される、独立した `.exe` ファイル（`lanzar_index.exe` および `lanzar_admin.exe`）へのコンパイル。
