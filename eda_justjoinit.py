from scraping import data
import pandas as pd
import json

print("Data type: ", type(data))
print("\nFirst item structure:")
print(json.dumps(data[0] if isinstance(data, list) else data, indent=2)[:1500])
# zwraca, trzeba się bawić dalej