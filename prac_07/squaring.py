"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class SquareNumberApp(App):
    """Kivy App for squaring a number."""
    status_message = StringProperty('Enter a number and press "Square"')

    def __init__(self, **kwargs):
        super(SquareNumberApp, self).__init__(**kwargs)

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call),
        output result to label widget."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.status_message = "Not A Number"


SquareNumberApp().run()
