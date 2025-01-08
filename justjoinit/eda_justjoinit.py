from scraping import fetch_all_offers
import pandas as pd
import json

data = fetch_all_offers()
print("Data type: ", type(data))

df = pd.json_normalize(data)
print(df.columns)
print(df.head(5))

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
            'workplaceType': row['workplaceType'],
            'requiredSkills': row['requiredSkills'],
            'niceToHaveSkills': row['niceToHaveSkills'],
            'companyName': row['companyName'],
            'remoteInterview': row['remoteInterview'],
            'publishedAt': row['publishedAt']
        })

df_salaries = pd.DataFrame(salary_data)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df_salaries.head(1))