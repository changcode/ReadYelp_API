import requests
from UnicodeWriter import UnicodeWriter
import csv
import json

url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer YErwauE-lHfqCQrrhPnyoiss_tKq3HHnGLRJ3jfOGZJSdZR3Iw2i59d8sP2j-m61IvAwuKW5HRloV8ouVqWjHrHdbK9AtZoEhDGkCJq4SNv7cMd6VJha580ZYWD2WHYx'}

offset = 0
limit = 50
term = 'restaurant'
location = 'Buffalo, NY'


f = open('./yelp.csv', 'a+')
writer = UnicodeWriter(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(['id',
        'name',
        'review_count',
        'categories1',
        'categories2',
        'categories3',
        'rating',
        'latitude',
        'longitude',
        'price',
        'distance']
        )


while offset < 1000:
    

    params = {'offset' : offset, 'limit' : limit, 'term' : term, 'location' : location}
    r = requests.get(url, headers=headers, params=params)
    
    res = r.json()

    
    businesses = res['businesses']
    

    print offset
    for item in businesses :
        writer.writerow([item['id'],
        item['name'],
        str(item['review_count']),
        "" if len(item['categories']) < 1 else item['categories'][0]['alias'],
        "" if len(item['categories']) < 2 else item['categories'][1]['alias'],
        "" if len(item['categories']) < 3 else item['categories'][2]['alias'],
        str(item['rating']),
        str(item['coordinates']['latitude']),
        str(item['coordinates']['longitude']),
        item['price'] if 'price' in item else "",
        str(item['distance'])]
        )
    
    offset += limit