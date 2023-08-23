from kivy.lang import Builder
from kivy.app import App
from kivy.uix.video import Video
class MyApp(App):
    def build(self):
        title="Simple Vidio"
        player= Video(source='v1.mp4')
        player.state ='play'
        player.options = {'eos': 'loop'}
        player.allow_stretch = True
        return player  
if __name__== '__main__':
    MyApp().run()