from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__,
            template_folder="../frontend/templates")

# Configuración MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'steam_project'

mysql = MySQL(app)

# ==========================
# HOME
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# GAMES
# ==========================
@app.route("/games")
def games():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT appid, name, release_date, price
        FROM Game
        LIMIT 100
    """)

    games = cur.fetchall()
    cur.close()

    return render_template("games.html", games=games)


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
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)