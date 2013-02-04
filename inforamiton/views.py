from flask import render_template
from inforamiton import app, weather

@app.route('/', methods=['GET'])
def home():
	return render_template('gps.html')

@app.route('/i/<lat>&<lon>', methods=['GET'])
def info(lat,lon):
	temp, place = weather.weather_from_gps(lat, lon)
	return render_template('info.html', lat=lat, lon=lon, temp=temp, place=place)
