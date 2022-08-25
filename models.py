#---------------------------------------------------------#
"""
My models  containing Artist, Venue, Show
"""
# imports
#---------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy
#---------------------------------------------------------#
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(255))
    #----Defining relationship----#
    shows = db.relationship('Show', backref='venues', lazy=True)
    #----for debugging purpose we include the repr dunder method----#
    def __repr__(self):
        return f'<Venue: ID: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, address: {self.address}, genres: {self.genres}, seeking talent: {self.seeking_talent}>'

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(255))
    #----for debugging purpose we include the repr dunder method----#
    def __repr__(self):
        return f'<Artist: ID: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, genres: {self.genres}, seeking talent: {self.seeking_venue}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__='show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id =db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    #---Defining relationship----#
    artists = db.relationship('Artist', backref='shows', lazy=True)
    #----for debugging purpose we include the repr dunder method----#
    def __repr__(self):
        return f'<Show: ID: {self.id}, Venue ID: {self.venue_id}, Artist ID: {self.artist_id}, Start time: {self.start_time}>'

