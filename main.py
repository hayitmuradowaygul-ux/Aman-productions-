from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class AmanApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        lbl = Label(text="Aman Production\nGoraýjy Programma", font_size='20sp')
        btn = Button(text="Başlat", size_hint=(1, 0.2))
        
        layout.add_widget(lbl)
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    AmanApp().run()
