from .rate import Rate


class CurrencyCodes(Rate):
    def __init__(self):
        super().__init__(format_='full')

    def currency_id(self, currency):
        """Получение идентификатора валюты"""
        return self.make_format(currency)['ID']