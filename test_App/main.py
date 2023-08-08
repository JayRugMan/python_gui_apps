import kivy
kivy.require('2.1.0')
from kivy.uix.widget import Widget
from kivy.properties import (StringProperty)

from kivy.app import App
from kivy.uix.label import Label


class LoginScreen(Widget):
    f_username = StringProperty(None)
    f_password = StringProperty(None)

class TestApp(App):
    def build(self):
        log_in = LoginScreen()
        return log_in


if __name__ == '__main__':
    TestApp().run()

