import csv

input_file = 'names.csv'
output_file = 'emails.csv'

with open(input_file, 'r', newline='') as csvfile_in, open(output_file, 'w', newline='') as csvfile_out:
    reader = csv.reader(csvfile_in)
    writer = csv.writer(csvfile_out)

    header = next(reader)
    email_column_index = header.index('email')

    writer.writerow(['email'])

    for row in reader:
        writer.writerow([row[email_column_index]])

print("The column 'email' was copied to another file.")
