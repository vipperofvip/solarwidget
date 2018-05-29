import requests

api_key = '3987235V4KP9W0ORGUPD7LS5YHA6TBV'

try:
    r = requests.get('https://monitoringapi.solaredge.com/site/481902/overview.json?api_key=%s' % (api_key,))
    data = r.json()
    current = data['overview']['currentPower']['power']/1000
    day = data['overview']['lastDayData']['energy']/1000
    print("{:.1f} kW {:.1f} kWh".format(current,day) )
except Exception:
    print('?')
