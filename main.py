import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class BMSApp(App):
    def build(self):
        # Main layout is BoxLayout to hold title and two sections of grid
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title at the top of the screen (centered)
        title = Label(text='BMS 14 CELLS', size_hint=(1, 0.1), font_size=40, bold=True)
        main_layout.add_widget(title)

        # Create the two sections (7 cells on each side)
        # Use a horizontal layout to position the two grid sections
        grid_layout = BoxLayout(size_hint=(1, 0.8))

        # Create the left section with 7 numerical displays
        self.left_grid = GridLayout(cols=1, spacing=5, size_hint=(0.5, 0.9))  # Reduced width to 30%
        self.left_text_inputs = []
        for i in range(7):
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)
            # For each cell, create a TextInput for numerical value
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                input_filter='float',
                font_size=40,  # Increased font size
                halign='center',  # Center-align the text inside the TextInput
                font_name='Roboto-Bold',  # Use a font that supports bold
            )
            self.left_text_inputs.append(text_input)
            self.left_grid.add_widget(text_input)

        # Create the right section with 7 numerical displays
        self.right_grid = GridLayout(cols=1, spacing=5, size_hint=(0.5, 0.9))  # Reduced width to 30%
        self.right_text_inputs = []
        for i in range(7, 14):
            # Generate random float values between 3.567 and 3.694
            random_value = round(random.uniform(3.567, 3.694), 3)
            # For each cell, create a TextInput for numerical value
            text_input = TextInput(
                text=str(random_value),
                multiline=False,
                input_filter='float',
                font_size=40,  # Increased font size
                halign='center',  # Center-align the text inside the TextInput
                font_name='Roboto-Bold',  # Use a font that supports bold
            )
            self.right_text_inputs.append(text_input)
            self.right_grid.add_widget(text_input)

        # Add both grids to the main horizontal box layout
        grid_layout.add_widget(self.left_grid)
        grid_layout.add_widget(self.right_grid)

        # Add the grid_layout to the main layout
        main_layout.add_widget(grid_layout)

        # Schedule the update of random values every 1 second
        Clock.schedule_interval(self.update_values, 1)

        return main_layout

    def update_values(self, dt):
        # Update the random values for left grid
        for text_input in self.left_text_inputs:
            new_value = round(random.uniform(3.567, 3.694), 3)
            text_input.text = str(new_value)

        # Update the random values for right grid
        for text_input in self.right_text_inputs:
            new_value = round(random.uniform(3.567, 3.694), 3)
            text_input.text = str(new_value)

if __name__ == '__main__':
    BMSApp().run()
