# ThetaS-MultiPictureCapture

Python script written by Bob White to capture time-lapse pictures with a RICOH THETA S. Submitted as part of the THETA Unofficial Guide 360 Time-Lapse Video Challenge (http://lists.theta360.guide/t/theta-unofficial-guide-360-time-lapse-video-challenge/1033).

There are currently three versions available. "-orig" is the first version.

**Notes on New Version Updates (Nov 20, 2017)**

"Cleaned up the code and added some notes."

**Notes on New Version Updates (Apr 3, 2017)**

1. The script will look in the Python host working directory for a subdirectory called ThetaS-Pics. If the subdirectory is not found it will create it. This is where all pictures taken will eventually be stored.

2. Current Theta S settings (only the ones that the script is about to change) will be saved and at the end of the run re-applied to the Theta S.

3. The script will ask if you want High or Low resolution. H or h for High and any other key/return for Low.

4. The script will ask for the number of pictures that you what to capture. Since no more then 2 pictures should ever be stored on the camera the sky is the limit here. It is your responsibility to ensure that you have enough room on the Python Host device to store the pictures that you ask to take and that you have adequate power available for the Theta S.

5. Pictures will shoot as fast as they can ~5 seconds for Low resolution and ~8 seconds for High resolution as long as you are in a WIFI range allowing transfer at maximum speed. Experiment with a small number of pictures taken at a time to establish the maximum acceptable distance for your setup. The script will spit out the time that it took to shoot XX number of pictures and also the total time for the run (transferring and deleting the last picture adds to the total run time).

6. What is happening when the script is running.  The script will tell your Theta S to take a picture and after the picture has completed processing it will take the next picture and while this  picture is processing the script will transfer the previous picture to the Python host and then delete it from the Theta S storage.  After the last picture is processed it will also be transferred and deleted and you will be notified that the run is complete and the time that it took to complete the run in HH:MM:SS.

**Notes on Original Version (Mar 24, 2017)**

The script sets up the Theta S and then asks how many stills to take.  Stills are shot at 1024 x 2048 due to space limitations of the Theta S. The script will take a picture, sleep for four seconds and then start looking for the status of “inProgress” to clear.  Once the “inProgress” status clears the script will take the next picture (about 5 seconds between each still).  Limited error checking is preformed. This is just a proof of concept run.

Note on number of pictures: When you run the script it will let you know how many pictures you can take based on the amount of storage that you have left in the camera. You can enter any number up to that amount. So with an empty camera storage you could ask for as many as 9073 pictures. The other limitation for the number of pictures that you can take is battery life. Ricoh says that the internal battery will support approximately 260 photos. 

I used a fully charged Anker PowerCore 26800 (26.8Ah) battery when I shot the 3000 pictures for the Unofficial Guide challenge, and it still had charge when I was done. Bottom line is the script will let you put in whatever you want to shot but it will tell you if you ask for more then there is memory to handle and will then exit.

Tools used: I used an external Anker PowerCore 26800 (26.8Ah) battery to power the Theta S during the shooting and FFMPEG to build the videos from the stills. The script was written on my iPhone using the Pythonista app and will control the Theta S directly from the app over wifi.

Note: Special thanks to Ole Zorn the developer for the iOS app Pythonista, as I wrote and tested my script using his app.

--

Addition information on <a href="http://omz-software.com/pythonista/">Pythonista</a>, from the <a href="https://itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&mt=8">Pythonista appstore page</a>:

Description
Pythonista is a complete scripting environment for Python, running directly on your iPad or iPhone. This new edition includes support for both Python 3.5 and 2.7, so you can use all the language improvements in Python 3, while still having 2.7 available for backwards compatibility. The integrated "2 to 3" tool makes it easy to ugrade your existing scripts.

In true Python fashion, batteries are included – from popular third-party modules like numpy, matplotlib, requests, and many more, to modules that are tailor-made for iOS. You can write scripts that access motion sensor data, your photo library, contacts, reminders, the iOS clipboard, and much more.

You can also use Pythonista to build interactive multi-touch experiences, custom user interfaces, animations, and 2D games.

Features:

* Scriptable code editor with syntax highlighting and code completion
* Extended keyboard, designed specifically for Python
* Interactive prompt with code completion, command history, and support for showing images in the console output
* Integrated visual debugger
* Integrated PEP 8 style checker with issues highlighted directly in the editor
* Complete offline documentation with quick lookup directly from the editor
* Various beautiful light and dark color themes, and a theme editor to make your own
* UI editor for quick prototyping
* Includes most of the Python standard library and additional modules for graphics, sound, and iOS system services (e.g. clipboard, contacts, reminders, twitter, UI...)
* Matplotlib and NumPy for scientific visualizations
* Lots of other popular third-party modules, e.g. requests, BeautifulSoup, Flask, bottle, SymPy, and more.
* Lots of included examples to get started
* Universal app for iPad and iPhone

The name "Pythonista" is used with kind permission of the Python Software Foundation.

![Analytics](https://ga-beacon.appspot.com/UA-73311422-5/Theta-MultiPictureCapture)
