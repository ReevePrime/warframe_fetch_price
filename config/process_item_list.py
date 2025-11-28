def process_item_list(clicked_item, data):
    item_list = list(dict.fromkeys([element["name"] for element in data]))
    match clicked_item:
        case "Warframes":
            item_list = [element["name"]
                         for element in data if element["name"].endswith("Prime")]
    return item_list
