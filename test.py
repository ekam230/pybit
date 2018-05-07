import json
import time
from variable import *

# import dateutil.parser
import primitive
import requests

#start_time = time.time() - 24 * 60 * 60
while True:
    resource = requests.get(
        "https://www.bitmex.com/api/v1/trade/bucketed?binSize=%s&partial=%s&symbol=%s&count=%d&reverse=true" % (tf, partial, pair, period))
    data = json.loads(resource.text)
    result = primitive.primitive(data)
    print(result)
    time.sleep(20)  # in seconds

# # yourdate = dateutil.parser.parse(k)
# # print(yourdate)
