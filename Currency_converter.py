from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input('Enter the amount of currency: '))

from_currency = input('From currency: ').upper()
to_currency = input('To currency: ').upper()

result = c.convert(from_currency, to_currency, amount)

print(f'{amount} {from_currency} ---> {result:.2f} {to_currency}')
