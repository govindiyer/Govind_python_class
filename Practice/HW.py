data_dict = {
    "item_A": 12,
    "item_B": 15,
    "item_C": 22,
    "item_D": 33,
    "item_E": 40,
    "item_F": 57
}
print("Original Dictionary:")
print(data_dict)

for key, value in data_dict.items():
    if isinstance(value,int) and value % 2 != 0:
        print(f"{key}: {value}")

    