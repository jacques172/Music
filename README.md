# Music app

This is the final project of CS50x. It is an app which enables you to play local storage songs on a kivy music player by parsing .mp3 songs from our local storage. A random song will start everytime we open the application with its name, image, timespan.





#### Video Demo:  <https://www.youtube.com/watch?v=yX4usKpgDBY>



# Technology used:

- Python

- Kivy

- KivyMD

# Features:

- Play: to play the music

- Stop: to Stop the musics

- Title: display the song title

- Image: display an image representing the song thumbnail

- Progress bar: display the progression, the current and the total time of the song.

- Volume slider: enables the user to increase or decrease the volume

- Mute button: enables to mute or unmute the song for our kivy music.

# imports:
# import os to grab all .mp3 songs from folder
# and random to pick a random song from the song list
import os
import random
import time
#import kivy library for UI design
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
# import soundloader to load song in kivy
from kivy.core.audio import SoundLoader
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
Window.size = (400,600)
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch

# Picture
![Screenshot 2022-11-16 170339](https://user-images.githubusercontent.com/96381612/202203143-e85a0045-f4b7-4fb2-857f-7da5470f12c5.png)


![Screenshot 2022-11-16 170253](https://user-images.githubusercontent.com/96381612/202203151-fd9b38ab-1bf5-48be-87cf-270c54e67f85.png)

# Installation-

Kivy is an opensource multi-platform GUI development library for Python and can run on iOS, Android, Windows, OS X, and GNU/Linux. It helps develop applications that make use of innovative, multi-touch UI. The fundamental idea behind Kivy is to enable the developer to build an app once and use it across all devices, making the code reusable and deployable, allowing for quick and easy interaction design and rapid prototyping.

This easy to use framework contains all the elements for building an application such as:

- Extensive input support for input devices such as mouse, keyboard, TUIO, and OS-specific multi-touch events
- A graphic library using only OpenGL ES 2
- A wide range of widgets built with multi-touch support
- An intermediate language Kv language, used to design custom widgets easily

KivyMD is an extension of the Kivy framework. KivyMD is a collection of Material Design widgets for use with Kivy, a GUI framework for making mobile applications. It is similar to the Kivy framework but provides a more attractive GUI.

Advantages
Based on Python, which is the extremely powerful given it’s library rich nature.
Write code once and use it across all devices.
Easy to use widgets built with multi-touch support.
Performs better than HTML5 cross-platform alternatives.

Disadvantages
Non-native looking User Interface.
Bigger package size (because Python interpreter needs to be included).
Lack of community support (Kivy Community isn’t particularly large).
Lack of good examples and documentation.
Better and more community rich alternates available if only focusing on Mobile Cross-platform devices i.e React Native.

pip install kivymd
pip install kivy

- Star and clone the repository to your machine.

- Once all the dependancies have been installed, run the command python main.py

- This should start your music app automatically

![done](https://user-images.githubusercontent.com/96381612/202209391-08d05634-9cc5-444b-a14a-cd852043c337.png)

# Documentation:

https://kivy.org/doc/stable/


https://kivymd.readthedocs.io/en/1.1.1/

# About CS50

CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

Where I get CS50 course? https://cs50.harvard.edu/x/2020/
