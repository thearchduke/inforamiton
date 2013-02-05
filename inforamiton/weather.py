import requests
try:
	from config import config
except:
	print "Using git, I see."
import random

def weather_from_gps(lat, lon):
	payload = 'http://api.wunderground.com/api/' + config['wunderkey'] + '/geolookup/q/' + str(lat) + ',' + str(lon) + '.json'
	r = requests.get(payload)
	print r
	try:
		foo = r.json()
	except:
		foo = r.json
	place = foo['location']['city'] + ', ' + foo['location']['state']
	payload = 'http://api.wunderground.com/api/ae007812a56622b8/conditions/q/' + foo['location']['state'] + '/' + foo['location']['city'] + '.json'
	r = requests.get(payload)
	try:
		weather = r.json()
	except:
		weather = r.json
	return weather['current_observation']['temp_f'], place


words = {'moderate':['cool', 'liveable', 'easy', 'moderate'],\
	'vacation':['warm', 'vacation', 'shorts weather (if you live on the West Coast)'],\
	'pool party':['sweaty', 'amazing', 'pool party', 'tropical vacation', 'beach weather',\
		'tank top weather', 'bikini weather', '*sizzle*', 'slurpee weather', 'shorts weather'],\
	'cool':['sweater weather', 'scarf weather', 'wintery', 'indoor weather'],\
	'cold':['indoor weather', 'brrrr!', '"literally* freezing" [*not literally]'],\
	'freezing':['literally freezing', 'whiskey weather', 'sledding weather', 'not leaving the house']\
	}
	
	
def adjectives(temp):
	out = [0]
	if temp >=62 and temp <=71:
		out = words['moderate']
	if temp >=72 and temp <=85:
		out = words['vacation']
	if temp >=86 and temp <=100:
		out = words['pool party']
	if temp >=33 and temp <= 61:
		out = words['cold']
	if temp <=32:
		out = words['freezing']
	if temp >100:
		out = ['holy crap that is hot', 'lock your daughters down (because the temperature is so hot)']
	return random.choice(out)

if __name__ == '__main__':
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)
	test = random.randint(0,110)
	print adjectives(words, test)

