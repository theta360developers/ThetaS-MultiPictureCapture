# TheataS-MultiPictureCapture

Python script that I wrote to capture 3000 stills with my Theta S last night.

The script sets up the Theta S and then asks how many stills to take.  Stills are shot at 1024 x 2048 due to space limitations of the Theta S. The script will take a picture, sleep for four seconds and then start looking for the status of “inProgress” to clear.  Once the “inProgress” status clears the script will take the next picture (about 5 seconds between each still).  Limited error checking is preformed.  This is just a proof of concept run.

I used an external battery to power the Theta S during the shooting and FFMPEG to build the videos from the stills.

The script was written on my iPhone using the Pythonista app and will control the Theta S directly from the app over wifi.

The videos in the attached link are all the same but at different frame rates.  12 frames per second equates to 1 seconds = 1 minute, 48 frames per second equates to 1 second = 4 minutes (15 seconds = 1 hour).

![Analytics](https://ga-beacon.appspot.com/UA-73311422-5/Theta-MultiPictureCapture)
