from django.contrib import admin

from currency_converter.models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ["from_currency", "to_currency", "rate", "date_updated"]

