import sys
import os.path as path
from numpy import double

import pandas as pd

from truck_table import TruckTable

# Path to ledger html file
ledger = None

# One of these will stay at None, used to check whether in ID or date mode
day = None
old_most_recent_entry = None

def parse_ledger(ledger):
    """
    Input: Path to html file containing table to be parsed
    Output: DataFrame of the table, or None
    """
    if path.isfile(ledger):
        contents = None
        with open(ledger) as file:
            contents = file.read()

        if contents is not None:
            try:
                table = pd.read_html(io=contents)[0]
            except ValueError as e:
                print("Error: {}".format(e))
                return None
            else:
                return(table)
    else:
        print("Error: \"{}\" is not a file!".format(ledger))
        return None

def parse_truck_number(details):
    """
    Input: String, formatted as per the "data" column from the ledger page
    Output: Raw truck number (no #, etc) or None
    """
    words = details.split()
    i = 0
    for word in words:
        if word.lower() == "truck":
            return words[i + 1].strip("#")
        else:
            i += 1
    return None

def parse_date(timestamp):
    """
    Input: String, formatted as per the "timestamp" column from the ledger page
    Output: String containing YYYY-MM-DD
    """
    return timestamp.split()[0]

def parse_amount(amount_string):
    """
    Input: String, formatted as per the "amount" column from the ledger page
    Output: Signed double
    """
    amount_list = amount_string.split("$") #  Extract the positive/negative sign
    string = ""  # Dummy string so we can use .join
    magnitude = double(string.join(amount_list[1].split(",")))  # Convert to float, remove commas
    if amount_list[0] == "-":
        return -magnitude
    else:
        return magnitude

def process_ledger(ledgers, old_most_recent_entry=None, day=None):
    truck_table=TruckTable()
    new_most_recent_entry = 0
    early_end = False

    # Parse all passed html files into a single table
    for ledger in ledgers:
        print("Reading from file: \"{}\"".format(ledger))
        table = parse_ledger(ledger)
        if table is None:
            continue

        # Iterate through rows
        for i in range(len(table)):
            # Extract each column
            ledger_ID = table["ID"][i]
            truck_number = parse_truck_number(table["Details"][i])
            date = parse_date(table["Timestamp"][i])
            amount = parse_amount(table["Amount"][i])
            category = table["Category"][i]

            # Check if ledger ID is too low (in ID mode)
            if old_most_recent_entry is not None and ledger_ID <= old_most_recent_entry:
                early_end = True
                continue

            # Check if date is incorrect (in date mode)
            if(day is not None and date != day):
                early_end = True
                continue

            # Check if this valid entry is more or less recent and update the ID
            new_most_recent_entry = max(ledger_ID, new_most_recent_entry)

            # Save to table
            if(category == "Fuel"):
                truck_table.update_truck(date, truck_number, fuel=amount)
            elif(category == "Shipment"):
                truck_table.update_truck(date, truck_number, income=amount)
            elif(category == "Tires" or category == "Breakdown"):
                truck_table.update_truck(date, truck_number, maintenance=amount)
            # Else do nothing; this is not to do with trucks

            # print("ID: {}, Date:{}, Amount: {}, Category: {}, Truck ID: {}".format(ledger_ID, date, amount, category, truck_number))  # Debug

    # Final outputs
    print(truck_table.tabulate())
    print("New most recent entry: {}".format(new_most_recent_entry))
    if early_end is not True:
        print("Warning: Ledger entry {} was not detected. This indicates that not all new ledger entries have been parsed.".format(old_most_recent_entry))

    # Save file to CSV for easy copy-pasting to google sheets
    truck_table.tabulate().to_csv("processed_ledger.csv")


if (__name__ == "__main__"):
    if(len(sys.argv)):
        if("-" in sys.argv[1]):
            # Date mode
            day = sys.argv[1]
        else:
            # ID mode
            old_most_recent_entry = int(sys.argv[1])
        ledgers = [sys.argv[i] for i in range(2, len(sys.argv))]
        print("Ignoring entries below ledger entry: {}".format(old_most_recent_entry))
        process_ledger(ledgers, old_most_recent_entry, day)