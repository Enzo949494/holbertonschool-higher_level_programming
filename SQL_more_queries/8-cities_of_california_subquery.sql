-- list all city of california in DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use
USE hbtn_0d_usa;

-- create 
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- create
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- insert
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('Utah');

-- insert
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco'), (1, 'San Jose'), (2, 'Page'), (3, 'Paris'), (3, 'Houston'), (3, 'Dallas');

-- request for list
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
