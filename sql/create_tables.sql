CREATE DATABASE IF NOT EXISTS steam_project;
USE steam_project;

CREATE TABLE Game (
    appid INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    release_date DATE,
    english BOOLEAN,
    required_age INT,
    achievements INT,
    positive_ratings INT,
    negative_ratings INT,
    average_playtime INT,
    median_playtime INT,
    owners VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE GameGenre (
    appid INT,
    genre_id INT,
    PRIMARY KEY (appid, genre_id),
    FOREIGN KEY (appid) REFERENCES Game(appid),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE GameCategory (
    appid INT,
    category_id INT,
    PRIMARY KEY (appid, category_id),
    FOREIGN KEY (appid) REFERENCES Game(appid),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Platform (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE GamePlatform (
    appid INT,
    platform_id INT,
    PRIMARY KEY (appid, platform_id),
    FOREIGN KEY (appid) REFERENCES Game(appid),
    FOREIGN KEY (platform_id) REFERENCES Platform(platform_id)
);

CREATE TABLE Developer (
    developer_id INT AUTO_INCREMENT PRIMARY KEY,
    developer_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE GameDeveloper (
    appid INT,
    developer_id INT,
    PRIMARY KEY (appid, developer_id),
    FOREIGN KEY (appid) REFERENCES Game(appid),
    FOREIGN KEY (developer_id) REFERENCES Developer(developer_id)
);

CREATE TABLE Publisher (
    publisher_id INT AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE GamePublisher (
    appid INT,
    publisher_id INT,
    PRIMARY KEY (appid, publisher_id),
    FOREIGN KEY (appid) REFERENCES Game(appid),
    FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id)
);

CREATE TABLE ReviewStats (
    appid INT PRIMARY KEY,
    positive_ratings INT,
    negative_ratings INT,
    average_playtime INT,
    median_playtime INT,
    FOREIGN KEY (appid) REFERENCES Game(appid)
);

CREATE TABLE PaidGame (
    appid INT PRIMARY KEY,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (appid) REFERENCES Game(appid)
);

CREATE TABLE FreeGame (
    appid INT PRIMARY KEY,
    free_label VARCHAR(50) DEFAULT 'Free to Play',
    FOREIGN KEY (appid) REFERENCES Game(appid)
);