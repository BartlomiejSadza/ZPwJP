from scraping import data
import pandas as pd
import json

print("Data type: ", type(data))

# Normalize the JSON data without nested paths first
df = pd.json_normalize(data['data'])

# Extract first location for each job
df['city'] = df['multilocation'].apply(lambda x: x[0]['city'] if x else None)
df['street'] = df['multilocation'].apply(lambda x: x[0]['street'] if x else None)

# Extract salary information
salary_data = []
for idx, row in df.iterrows():
    for emp_type in row['employmentTypes']:
        salary_data.append({
            'title': row['title'],
            'city': row['city'],
            'type': emp_type['type'],
            'from': emp_type['from'],
            'to': emp_type['to'],
            'currency': emp_type['currency'],
            'experienceLevel': row['experienceLevel'],
            'workplaceType': row['workplaceType']
        })

df_salaries = pd.DataFrame(salary_data)

# Basic statistics
print("\nBasic Statistics:")
print(df_salaries)