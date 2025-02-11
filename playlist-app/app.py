from flask import Flask, redirect, render_template, request



from models import *
from forms import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG'] = True


connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"


app.app_context().push()




# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    playlist = Playlist.query.get(playlist_id)
    songs = Song.query.all()
    playlist_song = PlaylistSong.query.all()

    return render_template('playlist.html', playlist=playlist, songs=songs, playlist_song=playlist_song)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_playlist = Playlist(name=name, description=description)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/')


    return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    
    song = Song.query.get(song_id)
    
    playlistSong = PlaylistSong.query.filter(PlaylistSong.song_id == song_id).all()
    playlists = Playlist.query.all()
    songs = Song.query.all()
    
    # if len(playlistSong) < 2:
    #     print(playlistSong)

    
    query = db.session.query(Playlist.name).select_from(Playlist).join(PlaylistSong, Playlist.id == PlaylistSong.playlist_id).filter(PlaylistSong.song_id == song_id)
    print(query)
    query2 = db.session.execute(query)
    results = query2.fetchall()
    print(results)
    

    # query2 = select(Playlist).where(Playlist.c.id == 1)
    

    # print(query2)
    
    # playlistss = db.session.execute(query)
    
    
    return render_template('song.html', song=song, playlists=playlists, playlistSong=playlistSong, results=results)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        new_song = Song(title=title, artist=artist)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/songs')
    
    return render_template('new_song.html', form=form)



@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    songs = Song.query.all()
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    curr_on_playlist = []
    for i in PlaylistSong.query.all():
        if i.playlist_id == playlist_id:
            curr_on_playlist.append(i.song_id)
    form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all())

    if request.method == 'POST':
        song_name = Song.query.get(request.form['song'])
        playlist_song = PlaylistSong(id=song_name.title, playlist_id=playlist_id, song_id=request.form['song'])
        db.session.add(playlist_song)
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form, songs=songs)