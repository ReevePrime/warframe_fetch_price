from tkinter import *
import json
from pathlib import Path
from ui import create_left_panel, generate_right_panel, init_wizard
from services import get_alecaframe_path, process_item_list, fetch_in_background, is_config_valid
from constants import MARKET_CATEGORIES


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
    fetch_in_background(item, label, category)


def run_ui(root):
    root.configure(bg="#2b2b2b")

    main_container = Frame(root, bg="#2b2b2b")
    main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)

    opt = StringVar(value="Warframes")
    list_var = StringVar()

    lb = create_left_panel(main_container, opt, list_var, update_list_of_items)

    if not is_config_valid():
        init_wizard(main_container, root)
    else:
        generate_right_panel(main_container, opt, get_text, lb)


def main():
    root = Tk()
    root.geometry("900x600")
    root.title("Warframe Price Fetcher")
    root.resizable(True, True)

    run_ui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
