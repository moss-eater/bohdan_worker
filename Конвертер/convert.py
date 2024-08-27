class ConvertLogic():
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.90,
            'GBP': 1.30,
            'UAH': 41.27,
            'JPY': 145.63,
            'PLN': 3.85
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        return amount * self.rates[to_currency] / self.rates[from_currency]