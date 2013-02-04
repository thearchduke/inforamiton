import requests

def weather_from_gps(lat, lon):
	payload = str(lat) + ',' + str(lon) + '.json'
	r = requests.get('http://api.wunderground.com/api/f43d31cc94da1791/geolookup/q/%s' % payload)
	foo = r.json()
	place = foo['location']['city'] + ', ' + foo['location']['state']
	payload = 'http://api.wunderground.com/api/f43d31cc94da1791/conditions/q/' + foo['location']['state'] + '/' + foo['location']['city'] + '.json'
	r = requests.get(payload)
	weather = r.json()
	return weather['current_observation']['temp_f'], place


if __name__ == '__main__':
	weather_from_gps(37.9199261,-122.5552514)
