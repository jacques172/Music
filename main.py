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

class PlayListApp(MDApp):
    
        def build(self):

            layout = MDRelativeLayout(md_bg_color = [0.9,0.5,1,1])
            self.music_dir = 'C:/Users/HP USER/Desktop/project'
            music_files = os.listdir(self.music_dir)
            self.playbutton = MDIconButton(pos_hint={'center_x':0.4, 'center_y':0.05},
                                                icon="play.png",
                                                on_press=self.playaudio)
            self.song_list = [x for x in music_files if x.endswith('mp3')]
            self.song_count = len(self.song_list)
            self.songlabel = Label(pos_hint={'center_x':0.5, 'center_y':.96},
                                size_hint=(1,1),
                                font_size=18)
            self.albumimage = Image(pos_hint={'center_x':0.5, 'center_y':0.55},
                                size_hint=(.8,.75))
            self.currenttime = Label(text = "00:00",
                                 pos_hint={'center_x':.16, 'center_y':.145},
                                 size_hint=(1,1),
                                 font_size=18)
            self.totaltime = Label(text = "00:00",
                                 pos_hint={'center_x':0.84, 'center_y':.145},
                                 size_hint=(1,1),
                                 font_size=18)                                         
            self.progressbar = ProgressBar(max = 100,
                                 value = 0,
                                 pos_hint={'center_x':0.5, 'center_y':0.12},
                                 size_hint=(.8,.75))
            self.volumeslider = Slider(min=0,
                           max=1,
                           value = 0.5,
                           orientation = 'horizontal',
                           pos_hint={'center_x':0.2, 'center_y':0.05},
                           size_hint=(.2,.2))
            self.switch = Switch(pos_hint={'center_x':0.75, 'center_y':0.05})
            
            self.stopbutton = MDIconButton(pos_hint={'center_x':0.55, 'center_y':0.05},
                                                icon="stop.png", 
                                                on_press=self.stopaudio, disabled=True)
            layout.add_widget(self.playbutton)
            layout.add_widget(self.stopbutton)
            layout.add_widget(self.songlabel)
            layout.add_widget(self.albumimage)
            layout.add_widget(self.currenttime)
            layout.add_widget(self.progressbar)
            layout.add_widget(self.totaltime)
            layout.add_widget(self.volumeslider)
            layout.add_widget(self.switch)

            Clock.schedule_once(self.playaudio)
            def mute(instance,value):
                if value == True:
                    self.sound.volume = 0
                else:
                    self.sound.volume = 1
            self.switch.bind(active = mute)
            def volume(instance,value):
                self.sound.volume = value  
            self.volumeslider.bind(value = volume) 

            return layout
        def playaudio(self,obj):
            self.playbutton.disabled = True
            self.stopbutton.disabled = False
            self.song_title = self.song_list[random.randrange(0, self.song_count)]
            self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
            self.songlabel.text = "---"+self.song_title[2:-4]+"---"
            self.albumimage.source = self.song_title[0]+".jpg"
            self.sound.play()

            self.progressbarEvent = Clock.schedule_interval(self.updateprogressbar,self.sound.length/60)
            self.timeEvent = Clock.schedule_interval(self.settime,1)
             
        def stopaudio(self, abj):
            self.playbutton.disabled = False
            self.stopbutton.disabled = True
            self.sound.stop()
            self.progressbarEvent.cancel()
            self.timeEvent.cancel()
            self.progressbar.value = 0
            self.currenttime.text = "00:00"
            self.totaltime.text = "00:00"
        def updateprogressbar(self,value):
            if self.progressbar.value < 100:
                self.progressbar.value +=1    
        def settime(self,t):
            current_time = time.strftime('%M:%S', time.gmtime(self.progressbar.value))
            total_time = time.strftime('%M:%S', time.gmtime(self.sound.length))
            self.currenttime.text = current_time
            self.totaltime.text = total_time
                    
if __name__ == '__main__':
    PlayListApp().run()