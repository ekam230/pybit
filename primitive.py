import numpy
import pyti
from pyti.exponential_moving_average import exponential_moving_average as ema
#from pyti.relative_strength_index import relative_strength_index as rsi
def primitive(data):
    """
    Function return result
    """
    quotes = {}
    quotes['open']=numpy.asarray([item['open'] for item in data])
    quotes['close']=numpy.asarray([item['close'] for item in data])
    # quotes['high']=numpy.asarray([item['high'] for item in data])
    # quotes['low']=numpy.asarray([item['low'] for item in data])
    # xdate = quotes['timestamp']=numpy.asarray([item['timestamp'] for item in data])
    open=quotes['open']
    open=open[-1]
    close=quotes['close']
    close=close[-1]

    usebody = True
    # /*
    #    * Logic
    #    *
    #    */

    #   // Рассчитывается размер тела свечи
    #   // body = abs(close - open)
    body = abs(close - open)
    print("Body: ", body)

    # Рассчитывается средний размер тел свечей ( EMA за 30 последних свечей)
    #   sbody = ema(body, 30) / 2

    bodyArray = []
    bodyArray.append(abs(quotes['close'] - quotes['open']))
    # print("BodyArray: ", bodyArray[0])

    new_ema = ema(bodyArray[0], 30)
    # print("EMA: ", new_ema)
    sbody = new_ema[-1]
    print("EMA: ", sbody) # выводим Ema
    sbody = sbody/2
    print("Sbody: ", sbody)

    # bar = close > open ? 1 : close < open ? -1 : 0
    bar = None

    # // Свеча зеленая
    if (close > open):
        bar = "green"
        print(f'Close: {close} > Open: {open}')
        print("Bar: ", bar)

    #   // Свеча красная
    elif(close < open):
        bar = "red"
        print(f"Close: {close} < Open: {open}")
        print("Bar: ", bar)

    #   // Ничего не произошло
    else:
        bar = "still"
        print('Close: %(close)f < Open: %(open)f' % {close, open})
        print("Bar: ", bar)

    # stop = 1

    #   /*
    #    * Signals
    #    *
    #    */

    #   // Если свеча красная, и тело больше половины среднего - открыть лонг (и закрыть шорт, если шорт был открыт)
    #   // Если свеча зеленая, тело больше половины среднего и позиция прибыльная - закрыть лонг
    #   // Если свеча зеленая, тело больше половины среднего - открыть шорт (и закрыть лонг, если лонг был открыт)
    #   // Если свеча красная, тело больше половины среднего и позиция прибыльная - закрыть шорт

    #   // up = bar == -1 and (body > sbody or usebody == false) and (close < strategy.position_avg_price or strategy.position_size <= 0 or useus == false)
    up = None
    #   // Если свеча красная, и тело больше половины среднего - открыть лонг (и закрыть шорт, если шорт был открыт)
    if (bar == 'red' and (body > sbody or usebody == False)):
        up = True
        print(f"Bar: {bar}, Body: {body} > SBody: {sbody}, Up = true")

    #   // dn = bar == 1 and (body > sbody or usebody == false) and (close > strategy.position_avg_price or strategy.position_size >= 0 or useus == false)
    down = None
    if(bar == 'green' and (body > sbody or usebody == False)):
        down = True
        print(f"Bar: {bar}, Body: {body} > SBody: {sbody}, Down = true")

    if up:
        return 'up'
    elif down:
        return 'down'
    else:
        return 'hold'
