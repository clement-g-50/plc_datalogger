import sys
import requests
import json
from datetime import timedelta
from pycomm3 import LogixDriver
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PySide6.QtCore import QThread, Signal, Slot # Importation pour le multi-threading
from gui.ui_interface import Ui_MainWindow
import webbrowser
import time

version = "v0.0.2"

configuration = {
    "type_plc": 0,
    "ip_address": "",
    "slot": 0,
    "temps_scan": 10,
    "csv_file_adress": "",
    "tags": []
}

# ------ CLASSE OUVRIÈRE POUR ÉVITER LE FREEZE ------
class PLCWorker(QThread):
    log_signal = Signal(str) # Signal pour envoyer du texte au QTextBrowser

    def __init__(self, config):
        super().__init__()
        self.config = config
        self._is_running = True

    def run(self):
        temps_ecoule = 0
        tags = [tag["plc"] for tag in self.config["tags"]]
        ip = self.config["ip_address"]
        slot = self.config["slot"]

        try:
            with LogixDriver(f"{ip}/{slot}") as plc:
                self.log_signal.emit(f"Connected to PLC at {ip}")
                
                while self._is_running:
                    results = plc.read(*tags)
                    for entry in results:
                        name, val, err = entry.tag, entry.value, entry.error
                        if err is None:
                            self.log_signal.emit(f"Tag: {name} | Valeur: {val}")
                        else:
                            self.log_signal.emit(f"Erreur sur {name}: {err}")
                    
                    # Pause sans bloquer l'interface (msleep est en millisecondes)
                    self.msleep(self.config["temps_scan"] * 1000)
                    temps_ecoule += self.config["temps_scan"]
                    temps_formate = str(timedelta(seconds=temps_ecoule))
                    self.log_signal.emit(f"-------- Temps écoulé: {temps_formate} --------")
        except Exception as e:
            self.log_signal.emit(f"Error during recording: {e}")

    def stop(self):
        self._is_running = False

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = None # Instance du thread

# ------ INITIALIZATION OF THE INTERFACE WITH THE CONFIGURATION FILE ------
    # Title name
        self.setWindowTitle(f"PLC Data Logger - {version}")
    # type PLC
        type_plc = ["Logix 5000"]
        self.ui.type_plc.addItems(type_plc)
        self.ui.type_plc.setCurrentIndex(configuration["type_plc"])
    # temps scan      
        self.ui.temps_scan.setValue(configuration["temps_scan"])
   # adresse IP
        self.ui.adressip.setText(configuration["ip_address"])
    # slot plc
        self.ui.slot_number.setValue(configuration["slot"])
    # csv file adress
        self.ui.csv_file_text.setText(configuration["csv_file_adress"])
    # tags display
        for tag in configuration["tags"]:
            self.ui.plccsvtable.insertRow(self.ui.plccsvtable.rowCount())
            row = self.ui.plccsvtable.rowCount() - 1
            self.ui.plccsvtable.setItem(row, 0, QTableWidgetItem(tag["plc"]))
            self.ui.plccsvtable.setItem(row, 1, QTableWidgetItem(tag["csv"]))
    # Check for updates
        if self.check_for_updates():
            self.ui.button_new_version.setVisible(True)
            self.ui.button_new_version.clicked.connect(lambda:webbrowser.open("https://github.com/clement-g-50/plc_datalogger/releases/latest"))
        else:
            self.ui.button_new_version.setVisible(False)
    # Hide start button
        self.ui.button_start_stop.setVisible(False)

# ------ CONFIGURATION ------
    # ---- Type PLC
        self.ui.type_plc.currentIndexChanged.connect(lambda: self.config_plc_type())
    # ---- Adresse IP
        self.ui.adressip.textChanged.connect(lambda: self.config_ip_address())
    # ---- Temps de scan
        self.ui.temps_scan.valueChanged.connect(lambda: self.config_temps_scan())
    # ---- Adresse du fichier CSV
        self.ui.csv_file_text.textChanged.connect(lambda: self.config_csv_file_adress())
        self.ui.csv_file_icon_button.clicked.connect(self.config_csv_file_dialog)

# ------ ADD / REMOVE TAGS ------
    # ---- Add line
        self.ui.add_line_bp.clicked.connect(self.table_add_item)
    # ---- Remove line
        self.ui.remove_line_bp.clicked.connect(lambda: self.table_remove_item())
    # ---- Edit line
        self.ui.plccsvtable.itemChanged.connect(lambda: self.table_edit_item())

# ----- START/STOP BUTTON ------
        self.ui.button_start_stop.clicked.connect(lambda: self.start_logix_recorder())

# ------ MENU BAR ------
    # ---- Save configuration
        self.ui.actionSauvegarder.triggered.connect(lambda: self.save_configuration())
    # ---- Load configuration
        self.ui.actionOuvrir.triggered.connect(lambda: self.load_configuration())
    # ---- Help
        self.ui.actionAide.triggered.connect(lambda: webbrowser.open("https://github.com/clement-g-50/plc_datalogger/wiki"))
    # ---- Github
        self.ui.actionGithub.triggered.connect(lambda: webbrowser.open("https://github.com/clement-g-50/plc_datalogger"))
    # ---- Exit
        self.ui.actionQuitter.triggered.connect(lambda: self.close())

# ---------------- FUNCTIONS ----------------

# ------ FUNCTIONS FOR THE TABLE ------     
    def table_add_item(self):
        self.ui.plccsvtable.insertRow(self.ui.plccsvtable.rowCount())
        configuration["tags"].append({"plc": "", "csv": ""})
        self.view_start_stop_button()
        print(configuration["tags"])
    def table_remove_item(self):
        current_row = self.ui.plccsvtable.currentRow()
        if current_row != -1:
            if current_row < len(configuration["tags"]):
                configuration["tags"].pop(current_row)
            self.ui.plccsvtable.removeRow(current_row)
        print(configuration["tags"])
        self.view_start_stop_button()
    def table_edit_item(self):
        current_row = self.ui.plccsvtable.currentRow()
        if current_row != -1:
            plc_item = self.ui.plccsvtable.item(current_row, 0)
            csv_item = self.ui.plccsvtable.item(current_row, 1)
            if plc_item and csv_item:
                configuration["tags"][current_row]["plc"] = plc_item.text()
                configuration["tags"][current_row]["csv"] = csv_item.text()
        print(configuration["tags"])
        self.view_start_stop_button()

# ------ FUNCTIONS FOR THE CONFIGURATION ------
    def config_plc_type(self):
        configuration["type_plc"] = self.ui.type_plc.currentIndex()
        print(configuration["type_plc"])
    def config_ip_address(self):
        configuration["ip_address"] = self.ui.adressip.text()
        print(configuration["ip_address"])
        self.view_start_stop_button()
    def config_temps_scan(self):
        if self.ui.temps_scan.value() >= 1:
            configuration["temps_scan"] = self.ui.temps_scan.value()
            print(configuration["temps_scan"])
        else:
            self.ui.temps_scan.setValue(1)
    def config_slot_number(self):
        configuration["slot"] = self.ui.slot_number.value()
        print(configuration["slot"])
    def config_csv_file_adress(self):
        configuration["csv_file_adress"] = self.ui.csv_file_text.text()
        print(configuration["csv_file_adress"])
        self.view_start_stop_button()
    def config_csv_file_dialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier source")
        if folder:
            self.ui.csv_file_text.setText(folder)

# ------ FUNCTIONS FOR THE UPDATE CHECKER ------
    def check_for_updates(self):
        url = f"https://api.github.com/repos/clement-g-50/plc_datalogger/releases/latest"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            release_info = response.json()
            latest_version = release_info["tag_name"][1:].split(".")
            current_version = version[1:].split(".")
            if latest_version > current_version:
                return True
            return False
        except requests.exceptions.RequestException as e:
            return False

# ------ FUNCTIONS FOR VIEW START/STOP BUTTON ------
    def view_start_stop_button(self):
        adress_ip_format = configuration["ip_address"].split(".")
        
        if len(adress_ip_format) == 4 and configuration["csv_file_adress"] != "" and len(configuration["tags"]) > 0:
            self.ui.button_start_stop.setVisible(True)
        else:
            self.ui.button_start_stop.setVisible(False)

# ------ FUNCTIONS FOR START/STOP BUTTON ------
    def start_logix_recorder(self):
        # Si le thread tourne déjà, on l'arrête
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.ui.button_start_stop.setText("Start")
            self.ui.logger.append("Arrêt de l'enregistrement...")
        else:
            # Sinon, on crée et on lance le thread
            self.worker = PLCWorker(configuration)
            # Connexion du signal à la fonction append du logger
            self.worker.log_signal.connect(self.ui.logger.append)
            self.worker.start()
            self.ui.button_start_stop.setText("Stop")
            self.ui.logger.append("Démarrage de l'enregistrement...")

# ----- FUNCTIONS FOR SAVE/LOAD CONFIGURATION ------
    def save_configuration(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Enregistrer la configuration", "", "Fichiers JSON (*.json)", options=options)
        if file_name:
            if not file_name.endswith(".json"):
                file_name += ".json"
            with open(file_name, 'w') as file:
                json.dump(configuration, file, indent=4)
    def load_configuration(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Ouvrir la configuration", "", "Fichiers JSON (*.json)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                global configuration
                configuration = json.load(file)
            self.update_interface_from_configuration()
    def update_interface_from_configuration(self):
        self.ui.type_plc.setCurrentIndex(configuration["type_plc"])
        self.ui.temps_scan.setValue(configuration["temps_scan"])
        self.ui.slot_number.setValue(configuration["slot"])
        self.ui.adressip.setText(configuration["ip_address"])
        self.ui.csv_file_text.setText(configuration["csv_file_adress"])
        self.ui.plccsvtable.setRowCount(0)
        for tag in configuration["tags"]:
            self.ui.plccsvtable.insertRow(self.ui.plccsvtable.rowCount())
            row = self.ui.plccsvtable.rowCount() - 1
            self.ui.plccsvtable.setItem(row, 0, QTableWidgetItem(tag["plc"]))
            self.ui.plccsvtable.setItem(row, 1, QTableWidgetItem(tag["csv"]))
        self.view_start_stop_button()

# ---------------- MAIN ----------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MyWindow()
    fenetre.show()
    sys.exit(app.exec())