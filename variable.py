#API
key = "Y-wzvPJMtqUGqsAm911_lsIU"
secret = "IeimDbUqsNn2a96zPrUGDUnK8GANJ2Hh5rbeUuXRqTApS1Ik"

#Таймфрейм
tf = '1h'
#полная свеча или нет
partial = 'true'

#Название пары для запроса с биржи
pair = 'XBTUSD'

#Название символа дл cctx
symbol = 'BTC/USD'

#period сколько свечей забираем
period = 30

# Торговые переменные
trend = 0 # Направление тренда. Вверх или вниз.
quantity = 0.06299655 # Сумма сделки в BTC
quantityusd = 50 # Сумма сделки в контрактах USD
profits = {} # Массив с результатами сделок
buyPrice = 0 # Цена покупки
price= 0
totalProfit = 0
orderNow={}
position= 0