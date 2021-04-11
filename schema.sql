CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT,
  password TEXT,
  ADMINISTRATOR BOOLEAN
);

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  name TEXT,
  year INTEGER,
  genre TEXT,
  description TEXT,
  leading_roles TEXT
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  user_id iNTEGER,
  movie_id INTEGER,
  grade iNTEGER,
  review INTEGER,
  time, TIMESTAMP
);
