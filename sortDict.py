my_dict = {
    "b" : "45",
    "e" : "99",
    "k" : "76",
}

sorted_items = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_items)