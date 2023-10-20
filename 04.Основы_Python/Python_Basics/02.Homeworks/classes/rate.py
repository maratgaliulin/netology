import requests


class Rate:
    def __init__(self, format_='value', diff=False):
        self.format = format_
        self.diff = diff

    def __exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах
        """

        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']

    def make_format(self, currency):
        response = self.__exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            if self.format == 'value':
                if not self.diff:
                    return response[currency]['Value']
                else:
                    return round((response[currency]['Value'] - response[currency]['Previous']), 2)
        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def brl(self):
        """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')

    def cheapest_currency(self):
        currency_dict = self.__exchange_rates()
        cheapest_value = 0
        cheapest_value_name = ''
        for key in currency_dict:
            if currency_dict[key]['Value'] > cheapest_value:
                cheapest_value = currency_dict[key]['Value']
                cheapest_value_name = currency_dict[key]['Name']
        print(f"Валюта с максимальным значением курса: {cheapest_value_name}, {cheapest_value}")
