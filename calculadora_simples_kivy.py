from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class Separator(Widget):
    pass


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10

        self.display = TextInput(
            readonly=True, multiline=False, font_size=40, size_hint=(1, 0.8),
            background_color=(0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )
        self.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for i, row in enumerate(buttons):
            button_row = BoxLayout(spacing=10)
            for button_label in row:
                button = Button(
                    text=button_label, font_size=30, background_color=(0.5, 0.5, 0.5, 1),
                    background_normal='', background_down='button_pressed.png'
                )
                button.bind(on_press=self.on_button_press)
                button_row.add_widget(button)
            self.add_widget(button_row)
            if i < len(buttons) - 1:
                separator = Separator(height=2, size_hint_y=None)
                with separator.canvas.before:
                    Color(0.5, 0.5, 0.5, 1)
                    Rectangle(pos=separator.pos, size=separator.size)
                self.add_widget(separator)

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = 'Error'
        elif button_text == 'C':
            self.display.text = ''
        else:
            self.display.text += button_text


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.3, 0.3, 0.3, 1)
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
