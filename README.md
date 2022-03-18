# Meta Ledger Parser
Specialized HTML parser that converts downloaded ledger html pages into CSV files for export into Google Sheets. Currently designed with a focus on extracting and compiling per-truck financial data for assisting with semi operations data analysis.

## Installation
There are currently no releases, and no plans for any. However, the program can be run as a script. To do so, first time setup requires the following:
1. Install [Python](https://www.python.org/downloads/). You may also need to install the [Python package installer, pip](https://pip.pypa.io/en/stable/installation/)
2. Clone/download the repo to a directory of your choice (Clone with `git clone https://github.com/Tropingenie/repo_Meta_Ledger_Parser.git` or download as per the screenshot)![Download button](https://cdn.discordapp.com/attachments/945223875279601687/954242216224768010/unknown.png)
2. Open a terminal of your choice and navigate to the same directory the program is downloaded to
3. Run the command `pip install -r requirements.txt` to download the dependencies

## Usage
The script is designed to work alongside dedicated spreadsheet software. Therefore, for very large entries the console will display a truncated table. All data is exported to the file `processed_ledger.csv`, which I recomment importing into Google Sheets for further analysis.

### Modes
The parser runs in one of two modes: ID mode, or date mode. 

#### ID Mode
In ID mode, the parser will parse all ledger entries above a certain ID. This is useful if you need to bring a partially filled table up to date, without parsing duplicate data. 

#### Date Mode
In date mode, the parser will parse all ledger entries that fall on a certain day. This is useful for compiling daily per-truck financial reports.

### Running the Parser
To run the parser, you need to run the program with at least 2 command line arguments: The ID of the oldest ledger entry you have saved or a date, and the path to at least one html file containing the ledger.

#### Downloading the ledger pages
To parse the ledger, currently ledger pages must be downloaded. This can be done simply enough by going into your ledger on Entreprenauts, right clicking anywhere, and selecting "Save As"

![Save as dialogue](https://cdn.discordapp.com/attachments/945223875279601687/954242999771099206/unknown.png)

#### ID Mode
General steps are:
1. Download all pages of the ledger you want parsed to .html files
2. Determine the oldest ledger entry you want parsed, and take the ID of the ledger entry ONE BELOW the oldest entry you want parsed
3. Open your terminal in the directory of the `scraper.py` file and run `python scraper.py OldestID+1 page_1.html ... page_n.html` (where `OldestID+1` is the ledger entry's ID one below the last ledger entry you want parsed, and `page_1.html ... page_n.html` are the ledger pages you want parsed)
4. The output will be printed to the terminal if it is short enough, and exported to a .csv file located in the same directory that `scraper.py` is in
![screenshot of csv file](https://cdn.discordapp.com/attachments/945223875279601687/954243405620334625/unknown.png)

For example, to parse the first three pages of my ledger, I would get the following:

![Example input for 3 pages of the ledger](https://cdn.discordapp.com/attachments/945223875279601687/954226376418926623/unknown.png "Example input for 3 pages of the ledger")

#### Date Mode
Running the parser in date mode is identical to running it in ID mode, except you specify a date (in `YYYY-MM-DD` format, like in the ledger)

`python scraper.py YYYY-MM-DD page_1.html ... page_n.html`

For example, to parse two pages of my ledger in date mode:
![Example input using date mode](https://cdn.discordapp.com/attachments/945223875279601687/954240683202478080/unknown.png "Example input using date mode")