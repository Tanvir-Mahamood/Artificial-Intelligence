# dictionary = a collection of {key:value} pairs. ordered and changaeable. No duplication
capitals = {"USA": "Washington DC", 
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}
print(capitals.get("USA"))

country = "Japan"
if capitals.get(country):
    print(capitals.get(country))
else:
    print("Not found")

capitals.update({"Germany": "berlin"})
capitals.update({"Germany": "Berlin"})

capitals.pop("China")
capitals.popitem()
print(capitals)

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)


items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}:{value}")