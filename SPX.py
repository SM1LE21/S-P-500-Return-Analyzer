import csv
from datetime import datetime

# Read the data
with open("SPX.csv", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data = []
    for row in rows:
        data.append(row)

# Initialize dictionary for yearly returns
yearly_returns = {}

for i in range(1, len(data)):
    current_price = float(data[i][1])
    previous_price = float(data[i-1][1])
    return_percentage = (current_price / previous_price) - 1

    # Convert the date string to a datetime object
    current_date = datetime.strptime(data[i][0], '%d/%m/%Y')
    
    # Use the starting year as the key, but add 1 if the month is after June or if it's June and the day is after the 25th
    current_year = current_date.year
    if current_date.month > 6 or (current_date.month == 6 and current_date.day > 25):
        current_year += 1

    # If the year is not yet in the dictionary, initialize it with an empty list
    if current_year not in yearly_returns:
        yearly_returns[current_year] = []

    # Append the return percentage to the correct year
    yearly_returns[current_year].append(return_percentage)

all_annualized_returns = []
# Calculate and print the average and annualized returns for each year
for year in yearly_returns:
    average_return = sum(yearly_returns[year]) / len(yearly_returns[year])
    print(f"Year: {year}, Average Return: {average_return}")
    annualized_return = (1 + average_return)**252 - 1
    print(f" -> Annualized Return: {annualized_return}")
    all_annualized_returns.append(annualized_return)

# Calculate and print the expected market return using a for loop
total_annualized_return = 0
for annualized_return in all_annualized_returns:
    total_annualized_return += annualized_return

expected_market_return = total_annualized_return / len(all_annualized_returns)
print(f"------------------------------------------------------------\nExpected Market Return: {expected_market_return} \n------------------------------------------------------------")