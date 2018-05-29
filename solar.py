import requests

api_key = '9W5YEA6PD7LE5V4TARM4GUKP0ORHSTBV'
site_id = '111111'

try:
    r = requests.get('https://monitoringapi.solaredge.com/site/%s/overview.json?api_key=%s' % (site_id,api_key))
    data = r.json()
    current = data['overview']['currentPower']['power']/1000
    day = data['overview']['lastDayData']['energy']/1000
    print("{:.1f} kW {:.1f} kWh".format(current,day) )
except Exception:
    print('?')
