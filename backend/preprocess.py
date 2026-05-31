import pandas as pd

df = pd.read_csv("../data/archive/steam.csv")

# Tabla principal de juegos
games = df[[
    "appid", "name", "release_date", "english",
    "required_age", "achievements",
    "positive_ratings", "negative_ratings",
    "average_playtime", "median_playtime",
    "owners", "price"
]]

print("GAMES")
print(games.head())

# Separar géneros
game_genres = df[["appid", "genres"]].copy()
game_genres["genres"] = game_genres["genres"].str.split(";")
game_genres = game_genres.explode("genres")

print("\nGAME GENRES")
print(game_genres.head(20))

games.to_csv("../data/games_clean.csv", index=False)
game_genres.to_csv("../data/game_genres.csv", index=False)

print("Archivos creados correctamente.")

# Separar categorías
game_categories = df[["appid", "categories"]].copy()
game_categories["categories"] = game_categories["categories"].str.split(";")
game_categories = game_categories.explode("categories")

# Separar plataformas
game_platforms = df[["appid", "platforms"]].copy()
game_platforms["platforms"] = game_platforms["platforms"].str.split(";")
game_platforms = game_platforms.explode("platforms")

# Separar developers
game_developers = df[["appid", "developer"]].copy()
game_developers["developer"] = game_developers["developer"].str.split(";")
game_developers = game_developers.explode("developer")

# Separar publishers
game_publishers = df[["appid", "publisher"]].copy()
game_publishers["publisher"] = game_publishers["publisher"].str.split(";")
game_publishers = game_publishers.explode("publisher")

game_categories.to_csv("../data/game_categories.csv", index=False)
game_platforms.to_csv("../data/game_platforms.csv", index=False)
game_developers.to_csv("../data/game_developers.csv", index=False)
game_publishers.to_csv("../data/game_publishers.csv", index=False)