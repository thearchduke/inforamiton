from flask import render_template
from inforamiton import app

@app.route('/', methods=['GET'])
def home():
	return render_template('gps.html')

@app.route('/i/<lat>&<lon>', methods=['GET'])
def info(lat,lon):
	return render_template('info.html', lat=lat, lon=lon)
