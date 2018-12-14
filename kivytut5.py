import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class SampBoxLayout(BoxLayout):

    act1 = ObjectProperty(True)
    act2 = ObjectProperty(True)
    act3 = ObjectProperty(True)



class SampleApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app = SampleApp()
sample_app.run()