# thetaS_TimeLapse.py
# 3 April 2017


import requests
import json
import time
import datetime
import os


def request(url_request):
	url_base = "http://192.168.1.1/osc/"
	url = url_base + url_request
	return url
	
	
def checkAPI():
	url = request("state")
	req = requests.post(url)
	apiVersion = req.json()
	print(47 * "=")
	if (apiVersion["state"]["_apiVersion"]) == 1:
		sid = startSession()
		setAPI(sid)
	else:
		print("API is 2.1\n"+(47 * "="))
	
	
def startSession():
	url = request("commands/execute")
	body = json.dumps({"name": "camera.startSession", "parameters": {}})
	req = requests.post(url, data=body)
	response = req.json()
	print("Start Session")
	print(47 * "=")
	sid = (response["results"]["sessionId"])
	return sid
	
	
def setAPI(sid):
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.setOptions",
						"parameters": {"sessionId": sid, "options": {"clientVersion": 2}}})
	requests.post(url, data=body)
	print("API set to 2.1")
	print(47 * "=")


def getCurrentOptionValues():
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.getOptions", "parameters":
						{"optionNames": ["remainingPictures", "offDelay", "exposureDelay",
							"sleepDelay", "_shutterVolume", "exposureProgram", "fileFormat"]}})
	req = requests.post(url, data=body)
	response = req.json()
	return response


def resetOptionValues(currentValues):
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.setOptions", "parameters":
						{"options":
							{"exposureDelay":
								currentValues['results']['options']['exposureDelay'],
								"sleepDelay":
								currentValues['results']['options']['sleepDelay'],
								"offDelay":
								currentValues['results']['options']['offDelay'],
								"_shutterVolume":
								currentValues['results']['options']['_shutterVolume'],
								"exposureProgram":
								currentValues['results']['options']['exposureProgram'],
								"fileFormat":
								{"height":
									currentValues['results']['options']['fileFormat']['height'],
									"type": "jpeg",
									"width":
									currentValues['results']['options']['fileFormat']['width']}}}})
	requests.post(url, data=body)


def setImage():
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.setOptions", "parameters":
						{"options":
							{"captureMode": "image"}}})
	requests.post(url, data=body)
	print(47 * "=")
	print("Capture mode set to Image")
	print(47 * "=")

			
def setOptions(res):
	if res == "H" or res == "h":
		height = 2688
		width = 5376
	else:
		height = 1024
		width = 2048
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.setOptions", "parameters":
						{"options":
							{"exposureDelay": 0, "sleepDelay": 65535, "offDelay": 65535,
								"_shutterVolume": 0, "exposureProgram": 2,  "fileFormat":
								{"height": height, "type": "jpeg", "width": width}}}})
	requests.post(url, data=body)
	print(47 * "=")
	print("Auto Program, Delay 0, Shutter Volume 0, Sleep Mode Off & JPEG",
							str(height)+"x"+str(width), "have been  set")
	print(47 * "=")
												
	
def takePicture(lastFileUrl):
	url = request("commands/execute")
	body = json.dumps({"name": "camera.takePicture"})
	req = requests.post(url, data=body)
	response = req.json()
	id = response["id"]
	print("Processing Picture......")
	fileUrl = lastFileUrl
	try:
		# Download last completed image
		downloadImage(fileUrl)
		# Delede downloaded image from camera
		deleteImage(fileUrl)
	except:
		pass
	url = request("commands/status")
	body = json.dumps({"id": id})
	req = requests.post(url, data=body)
	response = req.json()
	while (response["state"] == "inProgress"):
		body = json.dumps({"id": id})
		req = requests.post(url, data=body)
		response = req.json()
	print(47 * "=")
	print("Transfer image:", response['results']['fileUrl'])
	return response['results']['fileUrl']
	
	
def downloadImage(fileUrl):
	imageName = fileUrl[-12:]
	req = requests.get(fileUrl)
	with open('./ThetaS-Pics/'+imageName, 'wb') as f:
		for chunk in req:
			f.write(chunk)
	

def deleteImage(fileUrl):
	fileUrls = [fileUrl]
	url = request("commands/execute")
	body = json.dumps(
					{"name": "camera.delete",
						"parameters": {"fileUrls": fileUrls}})
	requests.post(url, data=body)
	print(47 * "=")
	print("Deleted from camera:", fileUrl)
		
				
def main():
	checkAPI()
	currentValues = getCurrentOptionValues()
	# Ensure picture capture directory exists on host
	if not os.path.exists('./ThetaS-Pics/'):
		os.makedirs('./ThetaS-Pics/')
	setImage()
	res = input("Select image capture resolution"
													" - H for 2688x5376 or return for 1024x2048\n")
	setOptions(res)
	picToTake = int(input("Input number of images to capture or 0 to exit\n"))
	startTime = time.time()
	if(picToTake == 0):
		print('Script terminated on request')
		exit()
	else:
		lastFileUrl = None
		for i in range(picToTake):
			dtg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			print(47 * "=")
			print("Taking Picture", i+1, "of", picToTake, "@", dtg)
			print(47 * "=")
			fileUrl = takePicture(lastFileUrl)
			lastFileUrl = fileUrl
			print(i+1, 'of', picToTake)
			if i+1 == picToTake:
				interimStopTime = time.time()
				print('All', picToTake, 'images shot in',
										str(datetime.timedelta(seconds=int(interimStopTime - startTime))))
				# download final image taken
				downloadImage(fileUrl)
				# delete final image taken
				deleteImage(fileUrl)
	stopTime = time.time()
	print(47 * "=")
	print('Job Completed -', picToTake, 'images shot, transfered and deleted in',
							str(datetime.timedelta(seconds=int(stopTime - startTime))))
	print(47 * "=")
	resetOptionValues(currentValues)
	
		
main()
