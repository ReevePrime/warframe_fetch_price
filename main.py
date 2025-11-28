from tkinter import *
from tkinter import filedialog, ttk
import requests
import time
import json
import os
from pathlib import Path
import threading
from config.init import init_wizard, is_config_valid, get_alecaframe_path
from config.process_item_list import process_item_list
from config.fetch_item_prices import fetch_in_background

market_list = ["Arcanes", "Arch-Gun", "Arch-Melee", "Archwing", "Melee",
               "Mods", "Primary", "Relics", "Secondary", "Sentinels", "Warframes"]


def update_list_of_items(clicked_item, list_var, opt):

    directory = get_alecaframe_path()
    aleca_file = Path(directory) / f"{clicked_item}.json"

    with open(aleca_file, encoding="UTF-8") as file:
        data = json.load(file)
        items_in_category = process_item_list(clicked_item, data)
        list_var.set(items_in_category)


def get_text(lb, label, opt):
    selection = lb.curselection()
    item = lb.get(selection)
    category = opt.get()
    fetch_in_background(item, label, opt)


def run_ui(directory, root):
    # Configure root window
    root.configure(bg="#2b2b2b")

    # Main container
    main_container = Frame(root, bg="#2b2b2b")
    main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # Left panel - Category selection and items list
    left_frame = LabelFrame(main_container, text="Select Category & Items",
                            bg="#3c3c3c", fg="#ffffff", font=("Arial", 10, "bold"),
                            padx=15, pady=15)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

    # Category dropdown label
    category_label = Label(left_frame, text="Category:", bg="#3c3c3c",
                           fg="#ffffff", font=("Arial", 9))
    category_label.grid(row=0, column=0, sticky=W, pady=(0, 5))

    # Selected option variable
    opt = StringVar(value="Warframes")

    # Dropdown menu with better styling
    drop = OptionMenu(left_frame, opt, *market_list,
                      command=lambda item: update_list_of_items(item, list_var, opt))
    drop.config(bg="#4a4a4a", fg="#ffffff", font=("Arial", 10),
                activebackground="#5a5a5a", relief=RAISED, bd=2, width=25)
    drop.grid(row=1, column=0, sticky=EW, pady=(0, 15))

    # Items label
    items_label = Label(left_frame, text="Items:", bg="#3c3c3c",
                        fg="#ffffff", font=("Arial", 9))
    items_label.grid(row=2, column=0, sticky=W, pady=(0, 5))

    # Create StringVar for the listbox
    list_var = StringVar()

    # Listbox with scrollbar
    listbox_frame = Frame(left_frame, bg="#3c3c3c")
    listbox_frame.grid(row=3, column=0, sticky=NSEW)

    scrollbar = Scrollbar(listbox_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    lb = Listbox(listbox_frame, height=20, listvariable=list_var,
                 bg="#4a4a4a", fg="#ffffff", font=("Arial", 10),
                 selectbackground="#0078d7", selectforeground="#ffffff",
                 relief=FLAT, bd=0, yscrollcommand=scrollbar.set)
    lb.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=lb.yview)

    # Configure grid weights
    left_frame.grid_rowconfigure(3, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    # Right panel - Price information
    right_frame = LabelFrame(main_container, text="Price Information",
                             bg="#3c3c3c", fg="#ffffff", font=("Arial", 10, "bold"),
                             padx=15, pady=15)
    right_frame.pack(side=LEFT, fill=BOTH, expand=True)

    # Price display label with better formatting
    label = Label(right_frame, text="Select an item and click 'Fetch Prices'",
                  bg="#4a4a4a", fg="#ffffff", font=("Arial", 10),
                  relief=FLAT, bd=0, padx=15, pady=15, justify=LEFT, anchor=NW)
    label.grid(row=1, column=0, sticky=NSEW)

    # Fetch button with better styling
    entry_btn = Button(right_frame, text="Fetch Prices", bg="#0078d7",
                       fg="#ffffff", font=("Arial", 10, "bold"),
                       activebackground="#005a9e", relief=RAISED, bd=2,
                       cursor="hand2", padx=20, pady=10,
                       command=lambda: get_text(lb, label, opt))
    entry_btn.grid(row=0, column=0, pady=(0, 15))

    # Configure grid weights for right frame
    right_frame.grid_rowconfigure(1, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)


def main():
    root = Tk()
    root.geometry("900x600")
    root.title("Warframe Price Fetcher")
    root.resizable(True, True)

    if not is_config_valid():
        directory = init_wizard(root)
    else:
        directory = get_alecaframe_path()

    if directory:
        run_ui(directory, root)

    root.mainloop()


if __name__ == "__main__":
    main()
