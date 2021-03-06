from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:wed37dyy2410@localhost/space_time_app'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Covid(db.Model):
    __tablename__ = 'covid'
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(50))
    province_state = db.Column(db.String(50))
    country = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    combined_loc = db.Column(db.String)
    date = db.Column(db.Date)
    confirmed = db.Column(db.Integer)
    deaths = db.Column(db.Integer)

    def __init__(self, county, province_state, country, latitude, longitude, combined_loc, date, confirmed, deaths):
        self.county = county
        self.province_state = province_state
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.combined_loc = combined_loc
        self.date = date
        self.confirmed = confirmed
        self.deaths = deaths


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run()
