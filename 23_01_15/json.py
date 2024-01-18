import json

# Reading and Writing JSON with External Files in Python

# Reading JSON from an External File
# Assume 'data.json' contains a JSON object like {"name": "John", "age": 30}
with open('data.json', 'r') as file:
    data = json.load(file)
# 'data' is now a Python dictionary with the content of 'data.json'

# Writing Python Object as JSON to an External File
new_data = {"name": "Alice", "age": 25, "city": "London"}
with open('new_data.json', 'w') as file:
    json.dump(new_data, file, indent=4)
# This creates or overwrites 'new_data.json' with the JSON representation of 'new_data'

# Note:
# - 'json.load()' reads JSON data from a file and converts it into a Python object.
# - 'json.dump()' writes a Python object to a file in JSON format.
# - The 'indent' parameter in 'json.dump()' is optional and used for formatting the output for readability.
