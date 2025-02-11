"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist_song"

    id = db.Column(db.String)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
