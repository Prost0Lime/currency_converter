import httpx
import xmltodict
from fastapi import FastAPI, HTTPException

app = FastAPI()


class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.exchange_rate()

    # получаем данные
    def exchange_rate(self):
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        response = httpx.get(url)
        data = xmltodict.parse(response.text)
        exchange_rates = {}
        for valute in data["ValCurs"]["Valute"]:
            code = valute["CharCode"]
            value = float(valute["Value"].replace(",", "."))
            exchange_rates[code] = value
            print(exchange_rates)
        return exchange_rates

    # расчёты
    def convert(self, from_currency, to_currency, value):
        if from_currency == to_currency:
            return value
        if from_currency != "RUB" and from_currency not in self.exchange_rate or to_currency != "RUB" and to_currency \
                not in self.exchange_rate:
            return None
        print(to_currency)
        if to_currency == "RUB":
            return value * (self.exchange_rate[from_currency])
        if from_currency == "RUB":
            return value * (1 / self.exchange_rate[to_currency])
        return value * (self.exchange_rate[from_currency] / self.exchange_rate[to_currency])


converter = CurrencyConverter()


@app.get("/api/rates")
async def get_exchange_rate(from_currency: str, to_currency: str, value: float):
    result = converter.convert(from_currency, to_currency, value)
    print(result)
    if result is None:
        raise HTTPException(status_code=400, detail="Введённого кода валюты не существует!")
    return {"result": round(result, 2)}
