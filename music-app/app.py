from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import pymysql
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'static/songs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect to MySQL
db = pymysql.connect(host="localhost", user="root", password="system1234", database="musicdb")
cursor = db.cursor()

ALLOWED_EXTENSIONS = {'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ------------------- User Routes -------------------
@app.route('/')
def index():
    user_id = session.get('user')

    # fetch all songs
    cursor.execute("""
        SELECT s.id, s.title, s.artist, s.image, s.audio_file, c.name 
        FROM songs s
        LEFT JOIN categories c ON s.category_id = c.id
    """)
    songs = cursor.fetchall()

    # fetch categories
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()

    # fetch playlists
    if user_id:
        cursor.execute("SELECT id, name FROM playlists WHERE user_id = %s", (user_id,))
        playlists = cursor.fetchall()
    else:
        playlists = []

    return render_template(
        'index.html',
        songs=songs,
        categories=categories,
        playlists=playlists
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            return redirect('/user_login')
        except:
            return "Username already exists!"
    return render_template('signup.html')

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            session['user'] = user[0]
            return redirect('/')
        else:
            return render_template('user_login.html', error="Invalid credentials")
    return render_template('user_login.html')

@app.route('/category/<int:category_id>')
def view_category(category_id):
    # fetch only songs from this category
    cursor.execute("""
        SELECT s.id, s.title, s.artist, s.image, s.audio_file, c.name 
        FROM songs s
        LEFT JOIN categories c ON s.category_id = c.id
        WHERE s.category_id = %s
    """, (category_id,))
    songs = cursor.fetchall()

    # fetch all categories for sidebar/cards
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()

    # fetch user playlists
    user_id = session.get('user')
    if user_id:
        cursor.execute("SELECT id, name FROM playlists WHERE user_id = %s", (user_id,))
        playlists = cursor.fetchall()
    else:
        playlists = []

    return render_template(
        "index.html", 
        songs=songs, 
        categories=categories, 
        playlists=playlists
    )




@app.route('/user_logout')
def user_logout():
    session.pop('user', None)
    return redirect('/')

# ------------------- Admin Routes -------------------
@app.route('/music-admin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (user, pw))
        admin = cursor.fetchone()
        if admin:
            session['admin'] = True
            return redirect('/admin/dashboard')
        else:
            return render_template("login.html", error="Invalid Credentials")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/login')

    # JOIN songs with categories to get category name
    cursor.execute("""
        SELECT s.id, s.title, s.artist, s.image, s.audio_file, c.name 
        FROM songs s
        LEFT JOIN categories c ON s.category_id = c.id
    """)
    songs = cursor.fetchall()

    return render_template("admin_dashboard.html", songs=songs)




@app.route('/add', methods=['GET', 'POST'])
def add_song():
    if not session.get('admin'):
        return redirect('/login')

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        image = request.form['image']
        category_id = request.form.get('category')  # selected category
        audio = request.files['audio']

        if not audio:
            return render_template("add_song.html", categories=categories, error="Please upload an audio file")

        if not allowed_file(audio.filename):
            return render_template("add_song.html", categories=categories, error="Only MP3 files are allowed")

        filename = secure_filename(audio.filename)
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio.save(audio_path)

        cursor.execute(
            "INSERT INTO songs (title, artist, image, audio_file, category_id) VALUES (%s, %s, %s, %s, %s)",
            (title, artist, image, filename, category_id)
        )
        db.commit()
        return redirect('/admin/dashboard')

    return render_template("add_song.html", categories=categories)



@app.route('/edit/<int:song_id>', methods=['GET', 'POST'])
def edit_song(song_id):
    if not session.get('admin'):
        return redirect('/login')
    cursor.execute("SELECT * FROM songs WHERE id=%s", (song_id,))
    song = cursor.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        image = request.form['image']
        cursor.execute("UPDATE songs SET title=%s, artist=%s, image=%s WHERE id=%s",
                       (title, artist, image, song_id))
        db.commit()
        return redirect('/admin/dashboard')
    return render_template("edit_song.html", song=song)

@app.route('/delete/<int:song_id>')
def delete_song(song_id):
    if not session.get('admin'):
        return redirect('/login')
    cursor.execute("DELETE FROM songs WHERE id=%s", (song_id,))
    db.commit()
    return redirect('/admin/dashboard')

# Admin: view and add categories
@app.route('/admin/categories', methods=['GET', 'POST'])
def manage_categories():
    if not session.get('admin'):
        return redirect('/login')
    if request.method == 'POST':
        name = request.form['name']
        cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
        db.commit()
        return redirect('/admin/categories')

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    return render_template("manage_categories.html", categories=categories)

@app.route('/admin/categories/delete/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if not session.get('admin'):
        return redirect('/login')
    
    try:
        cursor.execute("DELETE FROM categories WHERE id = %s", (category_id,))
        db.commit()
        return redirect('/admin/categories')
    except Exception as e:
        print("Error deleting category:", e)
        return redirect('/admin/categories')



# ------------------- Playlist & Favorites -------------------
@app.route('/songs')
def all_songs():
    cursor.execute("""
        SELECT s.id, s.title, s.artist, s.image, s.audio_file, c.name 
        FROM songs s
        LEFT JOIN categories c ON s.category_id = c.id
    """)
    songs = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM playlists WHERE user_id = %s", (session['user_id'],))
    playlists = cursor.fetchall()

    return render_template("songs.html", songs=songs, categories=categories, playlists=playlists)


@app.route('/toggle_favorite/<int:song_id>', methods=['POST'])
def toggle_favorite(song_id):
    user_id = session.get('user')
    if not user_id:
        return jsonify({'status': 'unauthorized'}), 403

    cursor.execute("SELECT id FROM playlists WHERE name='Favorites' AND user_id=%s", (user_id,))
    fav = cursor.fetchone()

    if not fav:
        cursor.execute("INSERT INTO playlists (name, user_id) VALUES ('Favorites', %s)", (user_id,))
        db.commit()
        cursor.execute("SELECT LAST_INSERT_ID()")
        fav_id = cursor.fetchone()[0]
    else:
        fav_id = fav[0]

    cursor.execute("SELECT * FROM playlist_songs WHERE playlist_id=%s AND song_id=%s", (fav_id, song_id))
    exists = cursor.fetchone()

    if exists:
        cursor.execute("DELETE FROM playlist_songs WHERE playlist_id=%s AND song_id=%s", (fav_id, song_id))
    else:
        cursor.execute("INSERT INTO playlist_songs (playlist_id, song_id) VALUES (%s, %s)", (fav_id, song_id))
    db.commit()

    return jsonify({'status': 'success'})

@app.route('/playlists')
def playlists():
    user_id = session.get('user')
    if not user_id:
        return redirect('/user_login')
    cursor.execute("SELECT * FROM playlists WHERE user_id=%s", (user_id,))
    playlists = cursor.fetchall()
    return render_template("create_playlist.html", playlists=playlists)

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    name = request.form['name']
    user_id = session.get('user')
    cursor.execute("INSERT INTO playlists (name, user_id) VALUES (%s, %s)", (name, user_id))
    db.commit()
    return redirect('/playlists')

@app.route('/playlist/<int:playlist_id>')
def view_playlist(playlist_id):
    cursor.execute("SELECT name FROM playlists WHERE id=%s", (playlist_id,))
    name = cursor.fetchone()[0]

    cursor.execute("""
        SELECT songs.* FROM songs
        JOIN playlist_songs ON playlist_songs.song_id = songs.id
        WHERE playlist_songs.playlist_id = %s
    """, (playlist_id,))
    songs = cursor.fetchall()
    return render_template("view_playlist.html", songs=songs, playlist_name=name, playlist_id=playlist_id)

@app.route('/add_to_playlist/<int:playlist_id>/<int:song_id>', methods=['POST'])
def add_to_playlist(playlist_id, song_id):
    user_id = session.get('user')
    if not user_id:
        return jsonify({'status': 'unauthorized'})

    cursor.execute("SELECT * FROM playlists WHERE id=%s AND user_id=%s", (playlist_id, user_id))
    if not cursor.fetchone():
        return jsonify({'status': 'error', 'message': 'Invalid playlist.'})

    cursor.execute("SELECT * FROM playlist_songs WHERE playlist_id=%s AND song_id=%s", (playlist_id, song_id))
    if cursor.fetchone():
        return jsonify({'status': 'error', 'message': 'Song already in playlist.'})

    cursor.execute("INSERT INTO playlist_songs (playlist_id, song_id) VALUES (%s, %s)", (playlist_id, song_id))
    db.commit()
    return jsonify({'status': 'success'})

@app.route('/remove_from_playlist/<int:playlist_id>/<int:song_id>', methods=['POST'])
def remove_from_playlist(playlist_id, song_id):
    user_id = session.get('user')
    if not user_id:
        return jsonify({'status': 'unauthorized'})

    cursor.execute("SELECT * FROM playlists WHERE id=%s AND user_id=%s", (playlist_id, user_id))
    if not cursor.fetchone():
        return jsonify({'status': 'error', 'message': 'Playlist not found or access denied'})

    cursor.execute("DELETE FROM playlist_songs WHERE playlist_id=%s AND song_id=%s", (playlist_id, song_id))
    db.commit()
    return jsonify({'status': 'success'})

# ------------------- Delete Playlist -------------------
@app.route('/delete_playlist/<int:playlist_id>', methods=['POST'])
def delete_playlist(playlist_id):
    user_id = session.get('user')
    if not user_id:
        return jsonify({'status': 'unauthorized'})

    cursor.execute("SELECT name FROM playlists WHERE id=%s AND user_id=%s", (playlist_id, user_id))
    playlist = cursor.fetchone()
    if not playlist:
        return jsonify({'status': 'error', 'message': 'Playlist not found or access denied'})

    # Optional: Prevent deleting Favorites
    if playlist[0].lower() == "favorites":
        return jsonify({'status': 'error', 'message': 'Favorites playlist cannot be deleted'})

    cursor.execute("DELETE FROM playlist_songs WHERE playlist_id=%s", (playlist_id,))
    cursor.execute("DELETE FROM playlists WHERE id=%s", (playlist_id,))
    db.commit()

    return jsonify({'status': 'success'})

# ------------------- Run -------------------
if __name__ == '__main__':
    app.run(debug=True)
