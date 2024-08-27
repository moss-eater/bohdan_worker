import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox



class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("Конвертор валют")
        self.resize(400, 150)

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

        from_currency_layout = QHBoxLayout()
        from_currency_layout.addWidget(self.from_currency_label)
        from_currency_layout.addWidget(self.from_currency_combo)
        layout.addLayout(from_currency_layout)

        to_currency_layout = QHBoxLayout()
        to_currency_layout.addWidget(self.to_currency_label)
        to_currency_layout.addWidget(self.to_currency_combo)
        layout.addLayout(to_currency_layout)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_display)
        layout.addLayout(result_layout)

        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.show()

    def covert_currency(self):
        rates = {
            'USD': 1.0,
            'EUR': 0.90,
            'GBP': 1.30,
            'UAH': 41.27,
            'JPY': 145.63,
            'PLN': 3.85
        }

        try:
            amount = float(self.amount_input.text())

            from_currency = self.from_currency_combo.currentText()

            to_currency = self.to_currency_combo.currentText()

            if from_currency != to_currency:
                converted_amount = amount * \
                    rates[to_currency] / rates[from_currency]
                
                self.result_display.setText(f"{converted_amount: .2f}")
            else:
                self.result_display.setText(f"{amount: .2f}")

        except ValueError:
            self.result_display.setText("Невірна Інформація")


app = QApplication([])
eksemplaar = CurrencyConverter()
sys.exit(app.exec())

