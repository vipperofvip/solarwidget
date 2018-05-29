solarwidget
===========

A widget for Mac using BetterTouchTool showing solar power and energy production for Mac

Requirements
------------

* Mac laptop with Touch Bar
* BetterTouchTool application installed
* Your Solaredge API key (You might need to contact your installer for this)

Installation Instructions
-------------------------
1. Copy this text into a file called solar.py somewhere in your home directory

Change the api_key and site_id values to what was provided by your inverter installer

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

2. Verify that the script can get the data it needs about your inverter's production

Use the 'Terminal' application to run the script like below. The command is `python solar.py` and it should output the power and energy of your inverter for that day so far.

    jay-mac:~ jajohnst$ python solar.py
    1.5 kW 5.4 kWh
    jay-mac:~ jajohnst$

If your script produces an error, ensure the site_id and api_key have been correctly modified to match what were provided to you by your inverter installation.

3. Launch the BetterTouchTool application, and under TouchBar, Create a new TouchBar Button


Install [BetterTouchTool](https://folivora.ai/)
