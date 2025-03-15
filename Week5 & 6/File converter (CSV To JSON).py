import csv, json, os


with open('Back-to-school transportation arrangement1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('output.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

csvFilePath = "Back-to-school transportation arrangement1.csv"
jsonFilePath = "Profiles.json"

data = {}

# with open(csvFilePath, encoding='utf-8') as csvFile:
#     csvReader = csv.DictReader(csvFile)
    
#     data = [row for row in csvReader]
   

# with open(jsonFilePath, 'w') as jsonFile:
#     jsonFile.write(json.dumps(data, indent=4))  