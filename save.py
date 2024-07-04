import csv

# ... (previous code)

# Save headlines to a CSV file
with open('headlines.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'Headline'])

    for index, headline in enumerate(headlines):
        writer.writerow([index + 1, headline.get_text()])
