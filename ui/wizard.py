from tkinter import *
from tkinter import filedialog, messagebox
import os
from services.config_manager import get_config_path


def init_json_directory(root):
    folder_selected = filedialog.askdirectory(
        title="Select AlecaFrame JSON Directory"
    )

    if not folder_selected:
        return

    if not os.path.isdir(folder_selected):
        messagebox.showerror(
            "Error", "Selected path is not a valid directory.")
        return

    config_file = get_config_path()
    with open(config_file, "w", encoding="UTF-8") as file:
        file.write(f"ALECAFRAME_DATA = {folder_selected}")

    messagebox.showinfo("Success", "Configuration saved successfully!")

    root.destroy()


def init_wizard(main_container, root):
    right_frame = LabelFrame(main_container, text="Price Information",
                             bg="#3c3c3c", fg="#ffffff", font=("Arial", 10, "bold"),
                             padx=15, pady=15)
    right_frame.grid(row=0, column=1, sticky=NSEW)

    label = Label(right_frame, text="""It looks like this is the first time you are running this App.

Please select the directory containing your AlecaFrame data,
usually located in 'C:\\Users\\USER_NAME\\AppData\\Local\\AlecaFrame\\cachedData\\json'""",
                  bg="#4a4a4a", fg="#ffffff", font=("Arial", 10),
                  relief=FLAT, bd=0, padx=15, pady=15, justify=LEFT, anchor=NW)
    label.grid(row=1, column=0, sticky=NSEW)

    init_button = Button(
        right_frame, text="Select AlecaFrame JSON Directory",
        command=lambda: init_json_directory(root)
    )
    init_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    right_frame.grid_rowconfigure(1, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)
