import requests, json, time

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
    	print("API is 2.1")
    setImage()
    setOptions()

def startSession():
    url = request("commands/execute")
    body = json.dumps({"name": "camera.startSession",
         "parameters": {}
         })
    req = requests.post(url, data=body)
    response = req.json()
    print("Start Session")
    print(47 * "=")
    print(json.dumps(response, indent=4, sort_keys=True))
    sid = (response["results"]["sessionId"])
    return sid

def takePicture():
      url = request("commands/execute")
      body = json.dumps({"name": "camera.takePicture"
           })
      req = requests.post(url, data=body)
      response = req.json()
      id = response["id"]
      print(47 * "=")
      print("Taking Picture")
      print(47 * "=")
      print(json.dumps(response, indent=4, sort_keys=True))
      print("\nProcessing Picture......\n")
      time.sleep(4)
      url = request("commands/status")
      body = json.dumps({"id": id})
      req = requests.post(url, data=body)
      response = req.json()
      while (response["state"] == "inProgress"):
        body = json.dumps({"id": id})
        req = requests.post(url, data=body)
        response = req.json()      
      print(47 * "=")
      print("Picture Status")
      print(47 * "=")
      print(json.dumps(response, indent=4, sort_keys=True))

def setAPI(sid):
      url = request("commands/execute")
      body = json.dumps({"name": "camera.setOptions",
           "parameters": {
         	"sessionId": sid,
            "options": {"clientVersion": 2}
           }
           })
      req = requests.post(url, data=body)
      response = req.json()
      print(47 * "=")
      print("API set to 2.1")
      print(47 * "=")
      print(json.dumps(response, indent=4, sort_keys=True))
	
def setOptions():
      url = request("commands/execute")
      body = json.dumps({"name": "camera.setOptions",
           "parameters":{
            "options": {"exposureDelay": 0, "exposureProgram": 2,  "fileFormat": {
                "height": 1024,
                "type": "jpeg",
                "width": 2048
            }
            }
           }})
      req = requests.post(url, data=body)
      response = req.json()
      print(47 * "=")
      print("Auto Program, Delay 0 & JPEG 1024x2048 set")
      print(47 * "=")
      print(json.dumps(response, indent=4, sort_keys=True))
      print(47 * "=")
      
def setImage():
      url = request("commands/execute")
      body = json.dumps({"name": "camera.setOptions",
           "parameters":{
            "options": {"captureMode": "image"
            }
           }})
      req = requests.post(url, data=body)
      response = req.json()
      print(47 * "=")
      print("Capture mode set to Image")
      print(47 * "=")
      print(json.dumps(response, indent=4, sort_keys=True))
      
def getRemainingPictures():
      url = request("commands/execute")
      body = json.dumps({"name": "camera.getOptions", "parameters":{
            "optionNames": ["remainingPictures"]
            }
           })
      req = requests.post(url, data=body)
      response = req.json()
      return (response["results"]["options"]["remainingPictures"])
	
def main():
      checkAPI()
      remainingPictures = getRemainingPictures()
      print("Storage has room for", remainingPictures, " more pictures.")
      picToTake = int(input("\nInput number of imeges to capture or 0 to exit\n"))
      if(picToTake == 0):
          print('Script terminated on request')
          exit()

      elif (remainingPictures >= picToTake):
          for i in range(picToTake):
              takePicture()
              print(i+1, 'of', picToTake)
      else:
          print("Not enough room in storage for", picToTake, "pictures. Try again.")
          exit()

main()
