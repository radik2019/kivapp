from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Pril(App):
    def build(self):
        azzurro = background_color=(0,204,255,0.4)

        box = GridLayout(cols=1)

        for i in range(4):
            box1 = GridLayout(cols=2, size_hint=(0.4, .7))
            box.add_widget(box1)
            lb = Label(text="la scritta")
            box1.add_widget(lb)

            txt = TextInput(password=False, multiline=False)
            box1.add_widget(txt)

        box2 = GridLayout(cols=2, size_hint=(0.7,9))
        box.add_widget(box2)
        
        

        bt = Button(text=f"button {str(i)}",background_color=(0,204,255,0.4))
        box2.add_widget(bt)

        box2.add_widget(Label(text='ciao\nciao\nciao\n ciao \n ciao'))

        return box

if __name__ == "__main__":
    app = Pril()
    app.run()