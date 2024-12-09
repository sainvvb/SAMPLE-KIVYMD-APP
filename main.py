import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class BMSApp(App):
    def build(self):
        # Main layout is BoxLayout to hold title and two sections of grid
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title at the top of the screen (centered)
        title = Label(text='BMS 14 CELLS', size_hint=(1, 0.1), font_size=24, bold=True)
        main_layout.add_widget(title)

        # Create the two sections (7 cells on each side)
        # Use a horizontal layout to position the two grid sections
        grid_layout = BoxLayout(size_hint=(1, 0.8))

        # Create the left section with 7 numerical displays
        left_grid = GridLayout(cols=1, spacing=5, size_hint=(0.5, 1))
        for i in range(7):
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)
            # For each cell, create a TextInput for numerical value
            text_input = TextInput(text=str(random_value), multiline=False, input_filter='float', font_size=18)
            left_grid.add_widget(text_input)

        # Create the right section with 7 numerical displays
        right_grid = GridLayout(cols=1, spacing=5, size_hint=(0.5, 1))
        for i in range(7, 14):
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)
            # For each cell, create a TextInput for numerical value
            text_input = TextInput(text=str(random_value), multiline=False, input_filter='float', font_size=18)
            right_grid.add_widget(text_input)

        # Add both grids to the main horizontal box layout
        grid_layout.add_widget(left_grid)
        grid_layout.add_widget(right_grid)

        # Add the grid_layout to the main layout
        main_layout.add_widget(grid_layout)

        return main_layout


if __name__ == '__main__':
    BMSApp().run()
