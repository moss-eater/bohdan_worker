import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox

from convert import ConvertLogic

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.logic = ConvertLogic()

        self.iniUI()

    def create_hbox_layout(self, label, widget):
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(widget)
        return hbox

    def iniUI(self):
        self.setWindowTitle("Конвертор валют")
        self.resize(400, 200)

        currencies = ["USD", "EUR", "GBP", "UAH", "JPY", "PLN"]

        self.amount_label = QLabel("Сума:")
        self.amount_input = QLineEdit()

        self.from_currency_label = QLabel("З валюти:")
        self.from_currency_combo = QComboBox()
        self.from_currency_combo.addItems(currencies)

        self.to_currency_label = QLabel("У валюту:")
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(currencies)

        self.result_label = QLabel("Результат:")
        self.result_display = QLabel("0.00")

        self.convert_button = QPushButton("Конвертувати")
        self.convert_button.clicked.connect(self.covert_currency)

        layout = QVBoxLayout()

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)

        layout.addLayout(self.create_hbox_layout(self.amount_label, self.amount_input))
        layout.addLayout(self.create_hbox_layout(self.from_currency_label, self.from_currency_combo))
        layout.addLayout(self.create_hbox_layout(self.to_currency_label, self.to_currency_combo))
        layout.addLayout(self.create_hbox_layout(self.result_label, self.result_display))

        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.apply_styles()
        self.show()

    def apply_styles(self):
        self.setStyleSheet("""
        QLabel {
            font-family: Arial, sans-serif;
            font-size: 16px;
            color: #333;
                           
        }
                           
        QLineEdit {
            font-size: 16px;
        }
                           
        QComboBox {
            font-size: 16px;
        }
                           
        QPushButton {
            font-size: 24px;
            background-color: #ffc800;
            border: none;
            padding: 8px;
        }
                           
        QPushButton:hover {
            background-color: #be9500;
        }                   
        """)
                           
    def covert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_combo.currentText()
            to_currency = self.to_currency_combo.currentText()

            converted_amount = self.logic.convert(amount, from_currency, to_currency)
            self.result_display.setText(f"{converted_amount: .2f}")

        except ValueError:
            self.show_error("Невірна Інформація", "Будь ласка, введіть число. Десяткові дроби через крапку.")

    def show_error(self, title, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()       

if __name__ == "__main__":
    app = QApplication([])
    eksemplaar = CurrencyConverter()
    sys.exit(app.exec())




