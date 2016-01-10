###Raspberry Pi Doorbell

When doorbell button is pushed a picture is taken and send as a MMS message to designated mobile number.

-Raspberry Pi w/ camera, GPIO pins/breadboard
-Flask web framework
-Twilio API
-Ngrok

-Connect Raspberry PI GPIO pins (#3 & #34) with breadboard and button
-Install ```requirements.py``` on Rasberry Pi
-Install Ngrok (Linux/ARM version)
-In seperate tab run ```ngrok http 5000``` and retreive Ngrok http url
-In project's root directory create ```static``` folder and add a ```ring.mp3``` file
-Create a ```your_info.py``` with Twilio credentials ```account_sid```, ```auth_token```, 
 ```to_phone_number```, ```from_phone_number``` and the Ngrok url ```ngrok_url```.
-In seperate tabs run ```app.py``` (on default port 5000) and ```doorbell.py```

