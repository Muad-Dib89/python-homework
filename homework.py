from pathlib import Path
import csv

csvpath = Path("../Resources/budget_data.csv")

analysis = []

month_count = 0
net_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0

# Open the csv file as an object
with open(csvpath, "r") as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    csv_header.append("Average")

    # Append the header to the list of records
    analysis.append(csv_header)

    for line in csvreader:
        month_count += 1
        net_profit_loss = (net_profit_loss) + int(line[1])
        average_profit_loss = round((net_profit_loss / month_count), 2)
        if greatest_increase < int(line[1]):
            greatest_increase = int(line[1])
        elif greatest_decrease > int(line[1]):
            greatest_decrease = int(line[1])

    # Print Results to terminal
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase: ${greatest_increase}")
    print(f"Greatest Decrease: ${greatest_decrease}")

    output_path = 'output.txt'

    # Open the output path as a file object
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${average_profit_loss}\n")
    file.write(f"Greatest Increase: ${greatest_increase}\n")
    file.write(f"Greatest Decrease: ${greatest_decrease}\n")