solarwidget
===========

A widget for Mac using BetterTouchTool showing solar power and energy production for Mac

![Widget](https://raw.githubusercontent.com/vipperofvip/solarwidget/master/widget.jpeg)

Requirements
------------

* Mac laptop with Touch Bar
* BetterTouchTool [BetterTouchTool](https://folivora.ai/) application already installed
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

3. Launch the BetterTouchTool application, and under TouchBar, Create a new Widget/Gesture

![Screenshot 1](https://raw.githubusercontent.com/vipperofvip/solarwidget/master/instructions_step_1.png)

4. Change the drop down titled 'Select Widget' to 'Run Apple Script and Show Return Value', then click 'Advanced Configuration'

Fill in the information as shown below (change the path of the file to reflect the file's location on your machine)

* Set the shell script path as shown in the picture, but modify the path to point to your home directory
* Change the TouchBar Button Color, Icon and Alternate Icons to something meaningful
* Under the section on the right 'Activate alternate color', that must be set to `0\.0 kW`
* Change the 'Execute this script every x seconds' to at least 300 to ensure you don't hit the API too often and get blocked

![Screenshot 2](https://raw.githubusercontent.com/vipperofvip/solarwidget/master/instructions_step_2.png)

That should be it! Click Save, and the touchbar widget should appear.

You can test that the script is able to be called from BetterTouchTool by clicking the 'Run Script' button within the editor window and the 'Result:' section should show current power and energy for the day.


