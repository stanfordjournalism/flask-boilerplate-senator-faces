import csv
from os.path import join
DATA_FILEPATH = join('static', 'data', 'legislators.csv')


def read_spreadsheet():
    """
    Opens the text file at static/data/legislators.csv and parses it

    Returns a Python list of dictionaries
    """
    txtlines = open(DATA_FILEPATH).readlines()
    rows = list(csv.DictReader(txtlines))
    return rows


def get_senators():
    """
    filter the spreadsheet for rows (i.e. senators) in which the
        "in_office" key is "1" and "title" key is "Sen"
    """
    records = read_spreadsheet()
    senators = []
    for row in records:
        if row['in_office'] == '1' and row['title'] == 'Sen':
            senators.append(row)
    return senators


def find_senator_by_id(bio_id):
    """
    the `bio_id` argument is a string and is expected to be a valid bioguide_id
        e.g. 'C001098' for Ted Cruz

    if `bio_id` doesn't match a bioguide_id value in the dataset, then
        a NoneValue is returned
    """

    # just incase the user submitted something like 'c001098', let's
    # upcase it, because 'c001098' is not equal to 'C001098'
    bx = bio_id.upper()

    for senator in get_senators():
        if senator['bioguide_id'] == bx: # we have a match!
            return senator

    # if the for loop completes, without breaking early for a return
    # it means that there was no match
    return None

