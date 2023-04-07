import csv

# data for the CSV file
data = [
    ['John', 85],
    ['Lisa', 92],
    ['David', 78],
    ['Karen', 89],
    ['Michael', 80],
    ['Sarah', 95],
    ['Steven', 87],
    ['Amanda', 91],
    ['Kevin', 83],
    ['Rachel', 88]
]

# name of the CSV file
filename = 'student_marks.csv'

# writing data to CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # writing header row
    csvwriter.writerow(['Student Name', 'Marks'])
    # writing data rows
    csvwriter.writerows(data)

print(f"{len(data)} rows written to {filename}")
