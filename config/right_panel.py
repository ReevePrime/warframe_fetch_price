from tkinter import *


def generate_right_panel(main_container, opt, get_text, lb):
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
