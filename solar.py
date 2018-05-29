import requests

api_key = 'HA6PD7LRGUKP9WSTAE5V40ORM4E5YTBV'
site_id = '111111'

try:
    r = requests.get('https://monitoringapi.solaredge.com/site/%s/overview.json?api_key=%s' % (site_id,api_key))
    data = r.json()
    current = data['overview']['currentPower']['power']/1000
    day = data['overview']['lastDayData']['energy']/1000
    print("{:.1f} kW {:.1f} kWh".format(current,day) )
except Exception as e:
    print('Problem: %s' % (e,))
