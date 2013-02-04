from inforamiton import app, views
import os

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5009))
	app.run(host='0.0.0.0', port=port)
