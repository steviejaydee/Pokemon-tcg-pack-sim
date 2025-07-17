import collections
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ListProperty

# Import the logic and data from your other file
from pack_logic import SETS_DATA, open_one_pack, format_collection_for_export

class MainLayout(BoxLayout):
    # Properties to hold the text for our display areas
    pulls_text = StringProperty("Last Pulls will appear here.")
    collection_text = StringProperty("Full Collection will appear here.")
    
    # Property to hold the list of available sets for the Spinner
    set_list = ListProperty(list(SETS_DATA.keys()))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_collection = []

    def open_packs_action(self):
        try:
            num_packs = int(self.ids.pack_count_input.text)
            if num_packs <= 0:
                self.ids.status_label.text = "Error: Please enter a positive number."
                return
        except ValueError:
            self.ids.status_label.text = "Error: Invalid number of packs."
            return

        selected_set_name = self.ids.set_selector.text
        set_data = SETS_DATA[selected_set_name]

        current_pulls = []
        for _ in range(num_packs):
            pack = open_one_pack(set_data, selected_set_name)
            current_pulls.extend(pack)
        
        self.total_collection.extend(current_pulls)

        # Update Last Pulls display
        pull_counts = collections.Counter(current_pulls)
        last_pulls_str = ""
        for card, count in sorted(pull_counts.items()):
            if isinstance(card, tuple) and len(card) == 5:
                name, set_code, num, rarity, _ = card
                last_pulls_str += f"{count}x {name} ({set_code} {num}) - {rarity}\n"
        self.pulls_text = last_pulls_str

        # Update Full Collection display
        self.collection_text = format_collection_for_export(self.total_collection)

        self.ids.status_label.text = f"Opened {num_packs} packs. Total cards: {len(self.total_collection)}"


class PackSimulatorApp(App):
    def build(self):
        return MainLayout()

# This is where you define the layout of your app in Kivy's .kv language
# It's like HTML/CSS for Kivy. You can also do this in Python code, but .kv is cleaner.
from kivy.lang import Builder

Builder.load_string('''
<MainLayout>:
    orientation: 'vertical'
    padding: '10dp'
    spacing: '10dp'
    # Give IDs to widgets so you can access them from Python code
    id: main_layout 

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '40dp'
        spacing: '5dp'

        Label:
            text: 'Set:'
            size_hint_x: 0.2
        Spinner:
            id: set_selector
            text: root.set_list[0] if root.set_list else ''
            values: root.set_list
            size_hint_x: 0.8
        Label:
            text: 'Packs:'
            size_hint_x: 0.2
        TextInput:
            id: pack_count_input
            text: '10'
            multiline: False
            input_filter: 'int'
            size_hint_x: 0.2
        Button:
            text: 'Open Packs'
            on_press: root.open_packs_action()
            size_hint_x: 0.4

    GridLayout:
        cols: 2
        spacing: '10dp'

        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Last Pulls'
                size_hint_y: None
                height: '30dp'
            ScrollView:
                Label:
                    text: root.pulls_text
                    size_hint_y: None
                    height: self.texture_size[1] # Makes the label grow with text
                    text_size: self.width, None
                    halign: 'left'
                    valign: 'top'
        
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Full Collection'
                size_hint_y: None
                height: '30dp'
            ScrollView:
                Label:
                    text: root.collection_text
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    halign: 'left'
                    valign: 'top'

    Label:
        id: status_label
        text: 'Ready. Select a set and open some packs!'
        size_hint_y: None
        height: '30dp'
''')

if __name__ == "__main__":
    PackSimulatorApp().run()