import csv
import os.path


def input_logic():
    name = ''
    while True:
        name = 'files/' + input("Input file name: ").strip()
        try:
            with open(name, 'r') as input_file:
                break
        except FileNotFoundError:
            print("File does not exist!")

    return name


def output_logic():
    name = 'files/' + input("Output file name: ").strip()
    while os.path.isfile(name):
        response = input("Overwrite existing file (y/n): ").strip().lower()
        while response != 'y' and response != 'n':
            response = input("Enter (y/n): ").strip().lower()
        if response == 'y':
            break
        elif response == 'n':
            name = 'files/' + input("New output file name: ").strip()
    return name


def main():
    input_file_name = input_logic()
    output_file_name = output_logic()

    data = []
    with open(input_file_name, 'r') as input_data:
        with open(output_file_name, 'w', newline='') as out_data:
            writer = csv.writer(out_data)
            new_list = []
            writer.writerow(["Email", "Time", "Confidence"])
            for line in input_data:
                line = line.rstrip()
                if line.startswith("From:"):
                    data.append(line.split()[1])
                if line.startswith("X-DSPAM-Processed:"):
                    data.append(line.split()[4])
                if line.startswith("X-DSPAM-Confidence:"):
                    data.append(line.split()[1])
                    new_list.append(float(line.split()[1]))
                    average = (sum(new_list))/len(new_list)
                    writer.writerow(data)
                    data.clear()

            writer.writerow(["", "Average", f'{average:.04}'])

    print("Data stored!")


if __name__ == '__main__':
    main()

