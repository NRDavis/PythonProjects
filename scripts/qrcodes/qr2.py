#qr2.py
import qrcode          #we import qrcodes
import csv

with open('studentRoster.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(','.join(row))

