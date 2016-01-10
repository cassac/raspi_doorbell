import os
from flask import Flask, request, send_from_directory, url_for
from twilio.rest import TwilioRestClient
from your_info import (account_sid, auth_token, to_phone_number, 
    from_phone_number, ngrok_url)

app = Flask(__name__)

client = TwilioRestClient(account_sid, auth_token)

STATIC_DIR = '/home/pi/projects/doorbell/static/'

@app.route('/incoming', methods=['GET', 'POST'])
def incoming_picture():
	if request.method == 'POST':

		file_name_to_send = ''

		for file_name, file_data in request.files.items():
			file_data.save(STATIC_DIR + file_name)

			file_name_to_send = file_name

		image_url = ngrok_url +\
					 url_for('.get_image', filename=file_name_to_send)
		
		# Send MMS via Twilio
		message = client.messages.create(
					to=to_phone_number, 
					from_=from_phone_number,
					body="Someone is ringing the doorbell!",
					media_url=image_url,
					)

		return image_url

	# Visit localhost:5000/incoming in browser to view 
	# a test picture displayed from static folder
	if request.method == 'GET':
		return send_from_directory(STATIC_DIR, 'test_pic.png')

@app.route('/image/<filename>')
def get_image(filename):
	if request.method == 'GET':
		return send_from_directory(STATIC_DIR, filename)


if '__main__' == __name__:
	app.run()
