import json
#for storing and exchanging data.
x = {
  "name": "Canoy",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Bison"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
