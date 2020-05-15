from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("mytrans.kv")
Builder.load_file("myTextToText.kv")
Builder.load_file("imageEdit.kv")
Builder.load_file("imageText.kv")
Builder.load_file("speech.kv")
import TransKivy
import textToText
import ImageEdit
import ImageText
import audio1
class NavigationDrawer(NavigationLayout):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
        self.title="Plethora"
    def build(self):         
        return NavigationDrawer()


MainApp().run()
