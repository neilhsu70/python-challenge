# Import dependencies
import os
import csv

# Path to collect data from the Resources folder
py_bank = os.path.join("Resources","budget_data.csv")

# Assign Variables
month_count = 0
net_total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
profit_loss = []
change = []
months = []


with open(py_bank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:

# Count number of rows
        if row[0] != "":
            month_count = month_count + 1
        net_total += int(row[1])


        amount = row[1]
        profit_loss.append(amount)
    
        month_entry = row[0]
        months.append(month_entry)
        
# Calculate Greatest Increase & Decrease in Profits

for x in range(0, len(profit_loss)-1):
        if x+1 == "":
            monthly_change = 0
        else:
            month_a = int(profit_loss[x])
            month_b = int(profit_loss[x+1])
            monthly_change = month_b - month_a
        change.append(monthly_change)

# Calculates Average change
changes_sum = sum(change)
average_change = changes_sum/(len(profit_loss) - 1)
average_change = round(average_change, 2)

# Calculates Greatest Increase & Decrease in Profits
greatest_increase = max(change)
greatest_decrease = min(change)

max_month = change.index(greatest_increase)
min_month = change.index(greatest_decrease)

month_max_change = months[max_month + 1]
month_min_change = months[min_month + 1]

# Print results in Terminal

def output():
    print("Financial Analysis by Neil Hsu")
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " +str(month_max_change) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " +str(month_min_change) + " ($" + str(greatest_decrease) + ")")
output()

# Export to .txt file
with open('Financial Analyst.txt', 'w') as csvwrite:
    csvwrite.write("Financial Analysis by Neil Hsu\n"
                  "----------------------------\n"
                  "Total Months: " + str(month_count) + "\n"
                  "Total: $" + str(net_total) + "\n"
                  "Average Change: $" + str(average_change) + "\n"
                  "Greatest Increase in Profits: " +str(month_max_change) + " ($" + str(greatest_increase) + ")\n"
                  "Greatest Decrease in Profits: " +str(month_min_change) + " ($" + str(greatest_decrease) + ")")