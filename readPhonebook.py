import csv

with open("sample.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    
    for row in reader:
        if row['language'] in counts:
            counts[row['language']] += 1
        else:
            counts[row['language']] = 1
            
    def get_value(language):
        return counts[language]
    
    for i in sorted(counts, key=lambda language: counts[language], reverse=True):
        print(f"{i} : {counts[i]}")