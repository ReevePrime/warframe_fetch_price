from pathlib import Path
import os


def get_config_path():
    config_dir = Path(__file__).parent.parent / "config"
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
