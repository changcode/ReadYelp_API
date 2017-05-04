import csv
import sys

f = open('./sample.csv', 'rb')
reader = csv.reader(f)
for row in reader:
    print row
f.close()

f = open('./sample.csv', 'a+')
writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow([u'asdf',u'123','123'])