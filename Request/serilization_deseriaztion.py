"""
Seriliaztion  - means converting object to string
Deseriivation means - converting string to object.
"""
import json

data = {"data": 1}
print(type(data))
serialized = json.dumps(data)
print(serialized)
print(type(serialized))

"""
Now converting the string to json
"""

deserial = json.loads(serialized)
print(deserial)
print(type(deserial))