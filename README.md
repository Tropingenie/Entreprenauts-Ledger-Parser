# Meta Ledger Parser
Specialized HTML parser that converts downloaded ledger html pages into CSV files for export into Google Sheets. Currently designed with a focus on extracting and compiling per-truck financial data for assisting with semi operations data analysis.

## Installation
There are currently no releases, and no plans for any. However, the program can be run as a script. To do so, first time setup requires the following:
1. Install [Python](https://www.python.org/downloads/)
2. Pull/download the repo to a directory of your choice
2. Open a terminal of your choice and navigate to the same directory the program is downloaded to
3. Run the command `pip install -r requirements.txt` to download the dependencies

## Usage
The script is designed to work alongside dedicated spreadsheet software. Therefore, for very large entries the console will display a truncated table. All data is exported to the file `processed_ledger.csv`, which I recomment importing into Google Sheets for further analysis.

To run the parser, you need to run the program with at least 2 command line arguments: The ID of the oldest ledger entry you have saved, and the path to at least one html file containing the ledger.

General steps are:
1. Download all pages of the ledger you want parsed to .html files
2. Determine the oldest ledger entry you want parsed, and take the ID of the ledger entry ONE BELOW the oldest entry you want parsed
3. Open your terminal in the directory of the `scraper.py` file and run `python scraper.py OldestID+1 page_1.html ... page_n.html` (where `OldestID+1` is the ledger entry's ID one below the last ledger entry you want parsed, and `page_1.html ... page_n.html` are the ledger pages you want parsed)

For example, to parse the first three pages of my ledger, I would get the following:

![Example input for 3 pages of the ledger](https://cdn.discordapp.com/attachments/945223875279601687/954226376418926623/unknown.png "Example input for 3 pages of the ledger")

