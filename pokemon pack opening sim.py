import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import random
import collections
import os
from sets.SV1 import SV1
from sets.SV2 import SV2
from sets.SV3 import SV3
from sets.SV35 import SV35
from sets.SV4 import SV4
from sets.SV5 import SV5
from sets.SV6 import SV6
from sets.SV65 import SV65
from sets.SV7 import SV7
from sets.SV8 import SV8
from sets.SV85 import SV85
from sets.SV9 import SV9
from sets.SV10 import SV10
# --- Set Data ---
# This dictionary holds all the data for each available Pokémon TCG set.
SETS_DATA = {}
sets = [SV1, SV2, SV3, SV35, SV4, SV5, SV6, SV65, SV7, SV8, SV85, SV9, SV10]
for set_data in sets:
    SETS_DATA.update(set_data)

BASIC_ENERGIES = ["Fire", "Water", "Grass", "Metal", "Darkness", "Psychic", "Lightning", "Fighting"]

def get_random_card(rarity, card_db):
   
    if rarity in card_db and card_db[rarity]:
        return random.choice(card_db[rarity])
    return None

def open_one_pack(set_data, set_name):
    
    pack_contents = []
    card_db = set_data['card_database']
    rates = set_data['pull_rates']
    
    # Calculate the probability of a Holo Rare in the rare slot
    p_holo = 1 - (rates.get('P_DR', 0) + rates.get('P_UR', 0) + rates.get('P_SIR', 0) + rates.get('P_HR', 0))
    pull_rates_rare_slot = {
        'Holo Rare': p_holo, 'Double Rare': rates.get('P_DR', 0), 'Ultra Rare': rates.get('P_UR', 0),
        'Special Illustration Rare': rates.get('P_SIR', 0), 'Hyper Rare': rates.get('P_HR', 0),
    }

    # Add base cards
    pack_contents.extend([get_random_card('Common', card_db) for _ in range(3)])
    pack_contents.extend([get_random_card('Uncommon', card_db) for _ in range(3)])
    pack_contents.append((f"{random.choice(BASIC_ENERGIES)} Energy", "Energy", "1", "Energy", "Energy"))

    # Define sets that have ACE SPEC cards in the reverse holo slot
    sets_with_ace_spec_in_reverse = [
        "Temporal Forces", "Twilight Masquerade", "Shrouded Fable", 
        "Stellar Crown", "Surging Sparks", "Prismatic Evolutions"
    ]

    # Handle the reverse holo slots logic
    if set_name == "Paldean Fates":
        pack_contents.append(get_random_card('Shiny Rare', card_db))
        reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
    # *** CORRECTED LOGIC HERE ***
    elif set_name in sets_with_ace_spec_in_reverse and 'ACE SPEC' in card_db and random.random() < (1/20):
        # Successfully pull an ACE SPEC in the reverse slot
        pack_contents.append(get_random_card('ACE SPEC', card_db))
        # The second reverse slot is a regular reverse holo
        reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
    else:
        # Default logic for two reverse holo slots (no ACE SPEC pulled)
        # First reverse holo slot can be an Illustration Rare
        if random.random() < rates.get('P_IR', 0):
            pack_contents.append(get_random_card('Illustration Rare', card_db))
        else:
            reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
            pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
        
        # Second reverse holo slot is always a regular reverse holo
        reverse_holo_rarity_2 = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity_2, card_db))

   
    # Determine and add the card for the final "Rare" slot
    rare_slot_rarity = random.choices(list(pull_rates_rare_slot.keys()), weights=list(pull_rates_rare_slot.values()), k=1)[0]
    card_rare = get_random_card(rare_slot_rarity, card_db)
    
    # Fallback to a regular rare if the chosen rarity has no cards
    if card_rare is None:
        card_rare = get_random_card('Rare', card_db)
    if card_rare:
        pack_contents.append(card_rare)

    return [c for c in pack_contents if c is not None]

def format_collection_for_export(collection, sort_mode='rarity'):
    if not collection:
        return "No cards collected yet."

    card_counts = collections.Counter(collection)
    
    rarity_order = [
        'Hyper Rare', 'Special Illustration Rare', 'Shiny Ultra Rare', 'Ultra Rare', 
        'Illustration Rare', 'ACE SPEC', 'Double Rare', 'Shiny Rare', 
        'Holo Rare', 'Rare', 'Uncommon', 'Common', 'Energy'
    ]
    rarity_map = {rarity: i for i, rarity in enumerate(rarity_order)}

    if sort_mode == 'rarity':
        sorted_cards = sorted(card_counts.items(), key=lambda item: rarity_map.get(item[0][3], 99))
    else: # 'name'
        sorted_cards = sorted(card_counts.items(), key=lambda item: item[0][0])

    pokemon_cards, trainer_cards, energy_cards = [], [], []
    total_pokemon, total_trainer, total_energy = 0, 0, 0

    for card, count in sorted_cards:
        if not isinstance(card, tuple) or len(card) != 5:
            continue
            
        name, set_code, num, _, card_type = card
        
        if card_type == 'Energy' and set_code == 'Energy':
            formatted_line = f"{count} {name}"
            energy_cards.append(formatted_line)
            total_energy += count
        else:
            formatted_line = f"{count} {name} {set_code} {num}"
            if card_type == 'Pokémon':
                pokemon_cards.append(formatted_line)
                total_pokemon += count
            elif card_type == 'Trainer':
                trainer_cards.append(formatted_line)
                total_trainer += count
    
    output_str = ""
    if pokemon_cards:
        output_str += f"Pokémon: {total_pokemon}\n"
        output_str += "\n".join(pokemon_cards) + "\n\n"
    if trainer_cards:
        output_str += f"Trainer: {total_trainer}\n"
        output_str += "\n".join(trainer_cards) + "\n\n"
    if energy_cards:
        output_str += f"Energy: {total_energy}\n"
        output_str += "\n".join(energy_cards) + "\n"
    
    return output_str.strip()

class PackSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon TCG Pack Simulator")
        self.root.geometry("800x600")

        self.total_collection = []
        self.sort_mode = 'rarity'

        controls_frame = ttk.Frame(root, padding="10")
        controls_frame.pack(side="top", fill="x")

        results_frame = ttk.Frame(root, padding="10")
        results_frame.pack(side="top", fill="both", expand=True)
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_columnconfigure(1, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ttk.Label(controls_frame, text="Select Set:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.set_selector = ttk.Combobox(controls_frame, values=list(SETS_DATA.keys()), state="readonly")
        self.set_selector.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.set_selector.current(0)
        
        ttk.Label(controls_frame, text="Number of Packs:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.pack_count_entry = ttk.Entry(controls_frame, width=10)
        self.pack_count_entry.grid(row=0, column=3, padx=5, pady=5)
        self.pack_count_entry.insert(0, "10")

        self.open_button = ttk.Button(controls_frame, text="Open Packs", command=self.open_packs)
        self.open_button.grid(row=0, column=4, padx=10, pady=5)
        
        self.export_button = ttk.Button(controls_frame, text="Save Collection...", command=self.export_to_file)
        self.export_button.grid(row=0, column=5, padx=5, pady=5)

        # --- Collection Display with Sorting ---
        collection_controls_frame = ttk.Frame(results_frame)
        collection_controls_frame.grid(row=0, column=1, sticky="ew", pady=(0, 5))
        ttk.Label(collection_controls_frame, text="Full Collection").pack(side="left")
        ttk.Button(collection_controls_frame, text="Sort by Name", command=self.sort_by_name).pack(side="right")
        ttk.Button(collection_controls_frame, text="Sort by Rarity", command=self.sort_by_rarity).pack(side="right")

        ttk.Label(results_frame, text="Last Pulls").grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.pulls_display = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, height=10, width=40)
        self.pulls_display.grid(row=1, column=0, sticky="nsew", padx=(0, 5))

        self.collection_display = scrolledtext.ScrolledText(results_frame, wrap=tk.WORD, height=10, width=40)
        self.collection_display.grid(row=1, column=1, sticky="nsew", padx=(5, 0))

        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w", padding="2 5")
        self.status_bar.pack(side="bottom", fill="x")
        self.status_var.set("Ready. Select a set and open some packs!")

    def sort_by_rarity(self):
        self.sort_mode = 'rarity'
        self.update_collection_display()

    def sort_by_name(self):
        self.sort_mode = 'name'
        self.update_collection_display()

    def open_packs(self):
        try:
            num_packs = int(self.pack_count_entry.get())
            if num_packs <= 0:
                self.status_var.set("Error: Please enter a positive number of packs.")
                return
        except ValueError:
            self.status_var.set("Error: Invalid number of packs.")
            return

        selected_set_name = self.set_selector.get()
        set_data = SETS_DATA[selected_set_name]
        
        current_pulls = []
        for _ in range(num_packs):
            pack = open_one_pack(set_data, selected_set_name)
            current_pulls.extend(pack)
        
        self.total_collection.extend(current_pulls)

        self.pulls_display.config(state='normal')
        self.pulls_display.delete(1.0, tk.END)
        pull_counts = collections.Counter(current_pulls)
        for card, count in sorted(pull_counts.items()):
            if not isinstance(card, tuple) or len(card) != 5:
                continue
            name, set_code, num, rarity, _ = card
            self.pulls_display.insert(tk.END, f"{count}x {name} ({set_code} {num}) - {rarity}\n")
        self.pulls_display.config(state='disabled')

        self.update_collection_display()
        self.status_var.set(f"Opened {num_packs} packs of {selected_set_name}. Total cards: {len(self.total_collection)}")

    def update_collection_display(self):
        export_text = format_collection_for_export(self.total_collection, self.sort_mode)
        self.collection_display.config(state='normal')
        self.collection_display.delete(1.0, tk.END)
        self.collection_display.insert(tk.END, export_text)
        self.collection_display.config(state='disabled')

    def export_to_file(self):
        if not self.total_collection:
            self.status_var.set("Nothing to export. Open some packs first!")
            return
            
        export_text = self.collection_display.get(1.0, tk.END)
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save Collection As..."
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(export_text)
                self.status_var.set(f"Collection successfully saved to {file_path}")
            except IOError as e:
                self.status_var.set(f"Error saving file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PackSimulatorApp(root)
    root.mainloop()
