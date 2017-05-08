import csv
DATA_FILEPATH = './static/legislators.csv'

def get_legislators():
    txtlines = open(DATA_FILEPATH).readlines()
    rows = list(csv.DictReader(txtlines))
    return rows

def get_senators():
    senators = []
    for row in get_legislators():
        if row['title'] == 'Sen' and row['in_office'] == '1':
            senators.append(row)
    return senators


def get_senator(bio_id):
    for row in get_senators():
        if row['bioguide_id'] == bio_id:
            return row
