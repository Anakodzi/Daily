import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class Opener(AnchorLayout):
    def __init__(self, **kwargs):
        super(Opener, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.btn = Button(text="Start")
        AnchorLayout.anchor_x = "center"
        AnchorLayout.anchor_y = "center"
        AnchorLayout.padding = [200, 200, 200, 200]
        self.add_widget(self.btn)


class Daily(App):
    def build(self):
        current_layout = Opener()
        return current_layout


if __name__ == "__main__":
    Daily().run()
