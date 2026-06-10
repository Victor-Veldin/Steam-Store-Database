from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(
    __name__,
    template_folder="../frontend/templates"
)

# ==========================
# MYSQL CONFIGURATION
# ==========================
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
# PUBLISHERS
# ==========================
@app.route("/publishers")
def publishers():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT publisher_id, publisher_name
        FROM Publisher
        ORDER BY publisher_name
        LIMIT 100
    """)

    publishers = cur.fetchall()
    cur.close()

    return render_template("publishers.html", publishers=publishers)


# ==========================
# PLATFORMS
# ==========================
@app.route("/platforms")
def platforms():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT platform_id, platform_name
        FROM Platform
        ORDER BY platform_name
    """)

    platforms = cur.fetchall()
    cur.close()

    return render_template("platforms.html", platforms=platforms)


# ==========================
# TOP RATED GAMES
# ==========================
@app.route("/top-rated")
def top_rated():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT name, positive_ratings, negative_ratings
        FROM Game
        ORDER BY positive_ratings DESC
        LIMIT 50
    """)

    games = cur.fetchall()
    cur.close()

    return render_template("top_rated.html", games=games)


# ==========================
# DASHBOARD
# ==========================
@app.route("/dashboard")
def dashboard():
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Game")
    total_games = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Genre")
    total_genres = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Developer")
    total_developers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Publisher")
    total_publishers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Platform")
    total_platforms = cur.fetchone()[0]

    cur.close()

    return render_template(
        "dashboard.html",
        total_games=total_games,
        total_genres=total_genres,
        total_developers=total_developers,
        total_publishers=total_publishers,
        total_platforms=total_platforms
    )


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
        JOIN GamePlatform gp ON p.platform_id = gp.platform_id
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
    platforms=platforms,
    score=score
)

@app.route("/most-played")
def most_played():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT name, average_playtime
        FROM Game
        ORDER BY average_playtime DESC
        LIMIT 50
    """)
    games = cur.fetchall()
    cur.close()
    return render_template("most_played.html", games=games)


@app.route("/most-expensive")
def most_expensive():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT name, price
        FROM Game
        ORDER BY price DESC
        LIMIT 50
    """)
    games = cur.fetchall()
    cur.close()
    return render_template("most_expensive.html", games=games)


@app.route("/most-achievements")
def most_achievements():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT name, achievements
        FROM Game
        ORDER BY achievements DESC
        LIMIT 50
    """)
    games = cur.fetchall()
    cur.close()
    return render_template("most_achievements.html", games=games)

# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)