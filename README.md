# ThetaS-MultiPictureCapture

Python script written by Bob White to capture time-lapse pictures with a RICOH THETA S. Submitted as part of the THETA Unofficial Guide 360 Time-Lapse Video Challenge (http://lists.theta360.guide/t/theta-unofficial-guide-360-time-lapse-video-challenge/1033).

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
