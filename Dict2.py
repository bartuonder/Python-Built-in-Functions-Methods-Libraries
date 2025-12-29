my_dict = {"name": "Bartu", "age": 21, "lang": "Python"}
print(f"Başlangıç: {my_dict}\n")

keys_list = my_dict.keys()
print(f"1. keys(): {keys_list}")

values_list = my_dict.values()
print(f"2. values(): {values_list}")

items_list = my_dict.items()
print(f"3. items(): {items_list}")

val = my_dict.get("age")
val_none = my_dict.get("salary", 0)
print(f"4. get('age'): {val} | get('salary'): {val_none}")

role = my_dict.setdefault("role", "Admin")
exist_age = my_dict.setdefault("age", 99)
print(f"5. setdefault(): role={role}, age={exist_age} -> Dict: {my_dict}")

my_dict.update({"lang": "Go", "city": "Istanbul"})
print(f"6. update(): {my_dict}")

removed_val = my_dict.pop("city")
print(f"7. pop('city'): Silinen değer '{removed_val}' -> Dict: {my_dict}")

last_item = my_dict.popitem()
print(f"8. popitem(): Silinen {last_item} -> Dict: {my_dict}")

new_dict = my_dict.copy()
print(f"9. copy(): Yeni sözlük {new_dict}")

keys_tuple = ("a", "b", "c")
dict_from_keys = dict.fromkeys(keys_tuple, 0)
print(f"10. fromkeys(): {dict_from_keys}")

my_dict.clear()
print(f"11. clear(): {my_dict}")