import requests
import gzip
import csv 
import re

url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
response = requests.get(url)

print("Fetching the datasets from imdb........\n")

with open('name.basics.tsv.gz', 'wb') as f:
    f.write(response.content)

primary_names = []

with gzip.open('name.basics.tsv.gz', 'rt', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')

    for row in reader:
        primary_names.append(row['primaryName'])

print("Creating a file 'names.txt' and adding the primary name column...")
with open('names.txt', 'w', encoding='utf-8') as f:
    for name in primary_names:
        f.write(name + '\n')

#read names from file created above 
print("Reading names.txt file............ \n")

with open('names.txt', 'r', encoding = 'utf-8') as f:
    primary_names = f.readlines()

primary_names = [name.strip() for name in primary_names if re.match(r'^[A-Za-z]', name.strip())]

sorted_names = sorted(set(primary_names), key=lambda x: x.lower())

print("Creating a file 'sorted_names.txt' and sorting the names ")
with open('sorted_names.txt', 'w', encoding='utf-8') as f:
    for name in sorted_names:
        f.write(name + '\n')

print("Files 'names.txt' and 'sorted_names.txt' have been created successfully.")

