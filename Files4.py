import re
import csv


def main():
    with open('files/input.txt', 'r') as input_file:
        with open('output.csv', 'w', newline='') as output_csv:
            with open('output.txt', 'w') as output_txt:

                contents = csv.writer(output_csv)
                contents.writerow(['Email', 'Day', 'Date', 'Month', 'Year', 'Time'])
                y = {}  # empty dict
                output_txt.write(f'{"Email":40s} - Count \n')

                for line in input_file:
                    line = line.rstrip()
                    # sending data to csv file
                    if re.search('^From ', line):
                        new_line = line.split()
                        email, day, month, time, year, date = new_line[1], new_line[2], new_line[3], new_line[5], new_line[6], new_line[4]
                        contents.writerow([email, day, date, month, year, time])

                    # sending data to the txt file
                    if re.search('^From:', line):
                        email = line.split()[1]
                        y[email] = y.get(email, 0) + 1
                for i in y:
                    output_txt.write(f'{i:40s} - {y[i]} \n')
                output_txt.write('-' * 49 + '\n')
                output_txt.write(f'{"Total Emails":40s} - {sum(y.values())}')


if __name__ == '__main__':
    main()
