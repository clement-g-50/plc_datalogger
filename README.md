# 📊 Rockwell PLC Datalogger

<p align="center">
  <img src="https://img.shields.io/github/v/release/clement-g-50/plc_datalogger?style=for-the-badge&color=blue" alt="Release">
  <img src="https://img.shields.io/github/license/clement-g-50/plc_datalogger?style=for-the-badge" alt="License">
</p>

---

## 🇫🇷 Français

### 📝 Description
Une application légère et performante pour l'acquisition de données (**Datalogging**) sur les automates **Rockwell / Allen-Bradley** (ControlLogix, CompactLogix, etc.). Conçu pour le milieu industriel, cet outil permet de surveiller les tags en temps réel via le protocole Ethernet/IP.

### ✨ Caractéristiques
* 🎨 Interface graphique moderne avec **PySide6**.
* 🔌 Communication robuste via la bibliothèque **pycomm3**.
* 💾 Exportation des données simplifiée.
* 🚀 **Exécutable portable** : Pas besoin d'installer Python sur le PC de maintenance.

### 🖼️ Démo (Importation de configuration)
![Demo Configuration](https://github.com/clement-g-50/plc_datalogger/raw/main/template/template_import.gif)

### 🚀 Installation & Utilisation
1. Téléchargez la dernière version dans l'onglet Release.
2. Lancez l'application (Plug & Play).
3. **Configuration :** Utilisez le fichier `template_configuration.json` via **Fichier > Ouvrir** pour charger vos tags.

### 🛡️ Sécurité (VirusTotal)
| Plateforme | Rapport de Scan | État |
| :--- | :--- | :--- |
| **Windows (.exe)** | [![VT](https://img.shields.io/badge/VirusTotal-2%2F71-blue?style=flat-square&logo=windows)](https://www.virustotal.com/gui/file/f08c2a402dde31c34f3e31c1f886fe14571bb3df826436aa06c0daffe6f2397a?nocache=1) | 🟢 Sain* |
| **Linux (Binary)** | [![VT](https://img.shields.io/badge/VirusTotal-0%2F64-orange?style=flat-square&logo=linux&logoColor=white)](https://www.virustotal.com/gui/file/b22ab7524efae2567c064e16401be4ce1ecbc03bbed06cb261efcc2acd3e5539?nocache=1) | 🟢 Sain |
*\*Note: Faux-positifs courants sur Windows car l'exécutable n'est pas signé.*

### ⚖️ Licence & Responsabilité
Ce projet est sous licence **MIT**. 
**Avertissement :** Ce logiciel est un outil indépendant et n'est pas affilié à Rockwell Automation. L'utilisateur assume l'entière responsabilité de son utilisation sur des systèmes de production. L'auteur ne peut être tenu responsable des arrêts machines ou pertes de données.

---

## 🇺🇸 English

### 📝 Description
A lightweight and high-performance data logging application for **Rockwell / Allen-Bradley** PLCs. Designed for industrial environments, this tool enables real-time tag monitoring via the Ethernet/IP protocol.

### ✨ Features
* 🎨 Modern GUI powered by **PySide6**.
* 🔌 Robust communication using the **pycomm3** library.
* 💾 Simplified data export.
* 🚀 **Portable Executable**: No Python installation required on the field PC.

### 🖼️ Demo (Config Import)
![Demo Configuration](https://github.com/clement-g-50/plc_datalogger/raw/main/template/template_import.gif)

### 🚀 Installation & Setup
1. Download the latest version from the releases tab.
2. Run the application.
3. **Setup:** Use the `template_configuration.json` by going to **Fichier > Ouvrir** (File > Open) inside the app to load it.

### 🛡️ Security Scans (VirusTotal)
| Platform | Scan Report | Status |
| :--- | :--- | :--- |
| **Windows (.exe)** | [![VT](https://img.shields.io/badge/VirusTotal-2%2F71-blue?style=flat-square&logo=windows)](https://www.virustotal.com/gui/file/f08c2a402dde31c34f3e31c1f886fe14571bb3df826436aa06c0daffe6f2397a?nocache=1) | 🟢 Clean* |
| **Linux (Binary)** | [![VT](https://img.shields.io/badge/VirusTotal-0%2F64-orange?style=flat-square&logo=linux&logoColor=white)](https://www.virustotal.com/gui/file/b22ab7524efae2567c064e16401be4ce1ecbc03bbed06cb261efcc2acd3e5539?nocache=1) | 🟢 Clean |
*\*Note: Common false-positives on Windows due to unsigned binary.*

### ⚖️ License & Disclaimer
This project is licensed under the **MIT License**.
**Disclaimer:** This software is an independent tool and is not affiliated with Rockwell Automation. The user assumes full responsibility for its use on production systems. The author cannot be held liable for any machine downtime or data loss.

---

### Credits
* [pycomm3](https://github.com/ottowatt/pycomm3) (MIT License)
* [PySide6](https://www.qt.io/qt-for-python) (LGPL License)
