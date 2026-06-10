from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__,
            template_folder="../frontend/templates")

# Configuración MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'steam_project'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

# ==========================
# HOME
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# GAMES PAGE + SEARCH
# ==========================
@app.route("/games")
def games():
    search = request.args.get("search", "")
    print("SEARCH VALUE:", search)
    cur = mysql.connection.cursor()

    if search:
        cur.execute("""
            SELECT appid, name, release_date, price
            FROM Game
            WHERE name LIKE %s
            LIMIT 100
        """, ('%' + search + '%',))
    else:
        cur.execute("""
            SELECT appid, name, release_date, price
            FROM Game
            LIMIT 100
        """)

    games = cur.fetchall()
    cur.close()

    return render_template("games.html", games=games, search=search)

# ==========================
# GENRES
# ==========================
@app.route("/genres")
def genres():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT genre_id, genre_name
        FROM Genre
        ORDER BY genre_name
    """)

    genres = cur.fetchall()
    cur.close()

    return render_template("genres.html", genres=genres)


# ==========================
# DEVELOPERS
# ==========================
@app.route("/developers")
def developers():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT developer_id, developer_name
        FROM Developer
        ORDER BY developer_name
        LIMIT 100
    """)

    developers = cur.fetchall()
    cur.close()

    return render_template("developers.html", developers=developers)

# ==========================
# GAME DETAILS PAGE
# ==========================

@app.route("/game/<int:appid>")
def game_details(appid):
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT appid, name, release_date, english, required_age,
               achievements, positive_ratings, negative_ratings,
               average_playtime, median_playtime, owners, price
        FROM Game
        WHERE appid = %s
    """, (appid,))
    game = cur.fetchone()

    cur.execute("""
        SELECT ge.genre_name
        FROM Genre ge
        JOIN GameGenre gg ON ge.genre_id = gg.genre_id
        WHERE gg.appid = %s
    """, (appid,))
    genres = cur.fetchall()

    cur.execute("""
        SELECT d.developer_name
        FROM Developer d
        JOIN GameDeveloper gd ON d.developer_id = gd.developer_id
        WHERE gd.appid = %s
    """, (appid,))
    developers = cur.fetchall()

    cur.execute("""
        SELECT p.publisher_name
        FROM Publisher p
        JOIN GamePublisher gp ON p.publisher_id = gp.publisher_id
        WHERE gp.appid = %s
    """, (appid,))
    publishers = cur.fetchall()

    cur.execute("""
        SELECT p.platform_name
        FROM Platform p
        JOIN GamePlatform gp
        ON p.platform_id = gp.platform_id
        WHERE gp.appid = %s
    """, (appid,))

    platforms = cur.fetchall()
    
    cur.close()

    return render_template(
        "game_details.html",
        game=game,
        genres=genres,
        developers=developers,
        publishers=publishers,
        platforms=platforms
    )
# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
