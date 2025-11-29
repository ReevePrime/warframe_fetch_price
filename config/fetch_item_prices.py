import threading
import requests
import time


def fetch_in_background(item, label, category):
    request_base_url = "https://api.warframe.market/v2/"
    item_slug = f"{item.lower().replace(" ", "_")}_set"
    url = f"{request_base_url}item/{item_slug}/set"
    r = requests.get(url)
    r_json = r.json()
    set_data = []
    for item_entry in r_json["data"]["items"]:
        item_data = {
            "slug": item_entry.get("slug"),
            "id": item_entry.get("id"),
            "name": item_entry["i18n"]["en"].get("name"),
            "set": item_entry["setRoot"]
        }
        set_data.append(item_data)

    for item_entry in set_data:
        re = requests.get(
            f"{request_base_url}orders/item/{item_entry['slug']}/top")
        re_json = re.json()
        json_data = re_json["data"]["sell"]
        ingame_orders = [
            d for d in json_data if d["user"]["status"] == "ingame"]
        item_entry["orders"] = ingame_orders[0]
        time.sleep(1)

    parts_price = sum(part["orders"]["platinum"]
                      for part in set_data if part["set"] != True)
    price_summary = []
    price_summary.append(f"Price of all parts: {parts_price}")
    for element in set_data:
        if element["set"] == True:
            price_summary.append(
                f"Set price: {element["orders"]["platinum"]}")
        else:
            price_summary.append(
                f"{element["name"]}: {element["orders"]["platinum"]}")
    label_text = "\n".join(price_summary)
    label.after(0, lambda: label.config(text=label_text))


thread = threading.Thread(target=fetch_in_background, daemon=True)
thread.start()
