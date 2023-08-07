import requests
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
from xml.etree import ElementTree as ET

from .models import CurrencyRate


@api_view(['GET'])
def currency_converter(request):
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    value = Decimal(request.GET.get('value', 1))

    if not from_currency or not to_currency:
        err = 'Не указаны обязательные параметры "От" и "До". \n(Пример запроса: /api/rates?from=USD&to=RUB&value=1)'
        return Response({'error': err}, status=400)

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Обновление курсов валют из ЦБР
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.status_code == 200:
        xml_data = response.content
        root = ET.fromstring(xml_data)
        for valute in root.findall('Valute'):
            currency_code = valute.find('CharCode').text
            if currency_code in (from_currency, to_currency):
                rate = Decimal(valute.find('Value').text.replace(',', '.'))
                CurrencyRate.objects.update_or_create(
                    from_currency=from_currency,
                    to_currency=to_currency,
                    defaults={'rate': rate}
                )

        if to_currency == 'RUB':
            rate = get_object_or_404(CurrencyRate, from_currency=from_currency, to_currency=to_currency)
            result = value * rate.rate
        else:
            result = 'Расчёт должен проводиться к рублю'

    return Response({'result': result})
