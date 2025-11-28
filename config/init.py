from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path
import os


def get_config_path():
    config_dir = Path(__file__).parent
    return config_dir / "alecaframe_data.txt"


def is_config_valid():
    config_file = get_config_path()
    if not config_file.exists():
        return False
    try:
        with open(config_file, "r", encoding="UTF-8") as file:
            content = file.read().strip()

        if not content:
            return False

        if "ALECAFRAME_DATA = " in content:
            path = content.split("ALECAFRAME_DATA = ", 1)[1].strip()
        else:
            path = content

        if path and os.path.isdir(path):
            return True

    except Exception:
        return False

    return False


def get_alecaframe_path():
    config_file = get_config_path()

    try:
        with open(config_file, "r", encoding="UTF-8") as file:
            content = file.read().strip()

        if "ALECAFRAME_DATA = " in content:
            return content.split("ALECAFRAME_DATA = ", 1)[1].strip()
        else:
            return content
    except Exception:
        return None


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

    # Restart the application to load with the new config
    root.destroy()
    # This will exit the init wizard and the main script can restart


def init_wizard(root):
    label = Label(root, text="""It looks like this is the first time you are running this App.

Please select the directory containing your AlecaFrame data,
usually located in 'C:\\Users\\USER_NAME\\AppData\\Local\\AlecaFrame\\cachedData\\json'""",
                  justify=CENTER, pady=20)
    label.place(relx=0.5, rely=0.4, anchor=CENTER)

    init_button = Button(
        root, text="Select AlecaFrame JSON Directory",
        command=lambda: init_json_directory(root)
    )
    init_button.place(relx=0.5, rely=0.5, anchor=CENTER)
