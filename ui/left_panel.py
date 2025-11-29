from tkinter import *
from constants import MARKET_CATEGORIES


def create_left_panel(main_container, opt, list_var, update_list_of_items):
    left_frame = LabelFrame(main_container, text="Select Category & Items",
                            bg="#3c3c3c", fg="#ffffff", font=("Arial", 10, "bold"),
                            padx=15, pady=15)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

    category_label = Label(left_frame, text="Category:", bg="#3c3c3c",
                           fg="#ffffff", font=("Arial", 9))
    category_label.grid(row=0, column=0, sticky=W, pady=(0, 5))

    drop = OptionMenu(left_frame, opt, *MARKET_CATEGORIES,
                      command=lambda item: update_list_of_items(item, list_var, opt))
    drop.config(bg="#4a4a4a", fg="#ffffff", font=("Arial", 10),
                activebackground="#5a5a5a", relief=RAISED, bd=2, width=25)
    drop.grid(row=1, column=0, sticky=EW, pady=(0, 15))

    items_label = Label(left_frame, text="Items:", bg="#3c3c3c",
                        fg="#ffffff", font=("Arial", 9))
    items_label.grid(row=2, column=0, sticky=W, pady=(0, 5))

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

    left_frame.grid_rowconfigure(3, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    return lb
