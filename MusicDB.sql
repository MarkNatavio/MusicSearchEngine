DROP SCHEMA IF EXISTS MusicDB;
CREATE DATABASE MusicDB;
USE MusicDB;

-- Create Songs Table - Contains Songs info
CREATE TABLE Songs(
   song_id   INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY
  ,SONG       VARCHAR(26) NOT NULL
  ,ARTIST     VARCHAR(15) NOT NULL
  ,GENRE      VARCHAR(24) NOT NULL
  ,ALBUM      VARCHAR(31) NOT NULL
  ,ALBUM_DATE INTEGER  NOT NULL
  ,DURATION   VARCHAR(4) NOT NULL
  ,LYRICS     TEXT
);

-- Create Users Table - Contains user info
CREATE TABLE Users(
	user_id	INTEGER NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    username VARCHAR(255),
    `password` VARCHAR(255),
    email VARCHAR(255),
    bio VARCHAR(250)
);

-- Create Playlists Table - Conntains user playlist info
CREATE TABLE Playlists(
	playlist_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    playlist_name VARCHAR(255),
    user_id	INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Playlists_Songs Table - Contains playlists and the songs stored within them
CREATE TABLE Playlists_Songs(
	row_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    song_id	INTEGER,
    playlist_id INTEGER,
    FOREIGN KEY (song_id) REFERENCES Songs(song_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlists(playlist_id)
);


-- =======================================================================================================================


INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Kryptonite','3 Doors Down','Alternative Rock','The Better Life',2000,'3:53',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Flying','Anathema','Progressive Doom','Hindsight',2008,'6:27',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('One Last Goodbye','Anathema','Progressive Doom','Hindsight',2008,'6:03',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Velvet Goldmine','David Bowie','Glam Rock','Five Years',2015,'3:10',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Lose Yourself','Eminem','Hip-Hop','8 Mile',2002,'5:20',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Everlong','Foo Fighters','Grunge Rock','The Colour And The Shape',1997,'4:10',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('November Rain','Guns N'' Roses','Glam Metal','Use Your Illusion I',1991,'8:56',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('A Tale That Wasn''t Right','Helloween','Melodic Metal','Keeper of the Seven Keys, Pt. I',1987,'4:43',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Take Me To Church','Hozier','Pop','Hozier',2014,'4:01',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Beyond the Realms of Death','Judas Priest','Birmingham Metal','Stained Class',1978,'6:49',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Nightcall','Kavinsky','Synthwave','OutRun',2013,'4:17',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('I Was Made For Lovin'' You','KISS','Glam Rock','Dynasty',1979,'4:31',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Detroit Rock City','KISS','Classic Rock','Double Platinum',1978,'3:35',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Sex on Fire','Kings of Leon','Modern Rock','Only By The Night',2008,'3:23',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Personal Jesus','Marilyn Manson','Alternative Metal','Personal Jesus',2004,'4:06',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Sweet Dreams','Marilyn Manson','Alternative Metal','Smells Like Children',1995,'4:53',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('She Will Be Loved','Maroon 5','Pop','Songs About Jane',2002,'4:17',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Hangar 18','Megadeth','Old School Trash','Rust In Peace',1990,'5:14',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Symphony Of Destruction','Megadeth','Melodic Trash','Countdown To Extinction',1992,'4:06',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Nothing Else Matters','Metallica','Metal','Metallica',1991,'6:28',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Master Of Puppets','Metallica','Old School Trash','Master Of Puppets',1986,'8:35',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Fade To Black','Metallica','Old School Trash','Ride The Lightning',1984,'6:57',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Seek & Destroy','Metallica','Old School Trash','Kill ''Em All',1983,'6:54',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Bir Derdim Var','Mor ve Ötesi','Turkish Alternative Rock','Dünya Yalan Söylüyor',2004,'3:24',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Something In The Way','Nirvana','Alternative Rock','Nevermind',1991,'3:52',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Come As You Are','Nirvana','Alternative Rock','Nevermind',1991,'3:38',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Crazy Train','Ozzy Osbourne','Birmingham Metal','Blizzard Of Ozz',2020,'4:53',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Perry Mason','Ozzy Osbourne','Birmingham Metal','Ozzmosis',1995,'5:53',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('20th Century Boy','Placebo','Permanent Wave','Covers',1003,'3:40',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Dont'' Stop Me Now','Queen','Glam Rock','Jazz',1978,'3:29',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Bohemian Rhapsody','Queen','Glam Rock','Bohemian Rhapsody',2018,'5:54',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('The Show Must Go On','Queen','Glam Rock','Bohemian Rhapsody',2018,'4:31',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Cum on Feel the Noize','Quiet Riot','Glam Metal','Metal Health',1983,'4:50',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Bitter Sweet','Roxy Music','Mellow Gold','Country Life',1974,'4:50',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Still Loving You','Scorpions','German Metal','Comeblack',2011,'6:43',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Sevmemeliyiz','Sena Şener','Turkish Alt Pop','İnsan Gelir İnsan Geçer',2018,'5:58',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Bir Çocuk Sevdim','Sezen Aksu','Turkish Pop','Sezen Aksu ''88',1988,'4:55',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Kaybolan Yıllar','Sezen Aksu','Turkish Pop','Serçe',1978,'3:07',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Raindrops','Shamrain','Gothic Metal','Goodbye To All That',2007,'4:30',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('To Leave','Shamrain','Gothic Metal','Someplace Else',2005,'4:27',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Anastasia','Slash','Hard Rock','Apocalyptic Love',2012,'6:07',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Seasons In The Abyss','Slayer','Old School Trash','Seasons In The Abyss',1990,'6:37',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Zombie','The Cranberries','Pop Rock','No Need To Argue',1994,'5:06',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('T.V. Eye','The Stooges','Permanent Wave','Funhouse',1970,'4:17',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Behind Blue Eyes','The Who','British Invasion','Who''s Next',1971,'3:41',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Past Perfect','Thurisaz','Belgian Black Metal','Circadian Rhythm',2007,'3:43',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('We''re Not Gonna Take It','Twisted Sister','Glam Metal','Stay Hungry',1984,'3:39',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Umrumda Değil','UZI','Turkish Trap','Kan',2021,'3:05',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Wild Child','W.A.S.P.','Glam Metal','The Last Command',1985,'5:12',NULL);
INSERT INTO Songs(SONG,ARTIST,GENRE,ALBUM,ALBUM_DATE,DURATION,LYRICS) VALUES ('Still of the Night','Whitesnake','Glam Metal','Whitesnake',1987,'6:37',NULL);

-- Creating Albums Table - Contains Album Info
CREATE TABLE Album AS (SELECT DISTINCT(ALBUM), ALBUM_DATE, ARTIST FROM Songs);
CREATE TABLE Albums AS (SELECT ROW_NUMBER() OVER() as album_id, ALBUM, ALBUM_DATE, ARTIST FROM Album);
DROP TABLE Album;

-- Add primary key to Albums table
ALTER TABLE Albums ADD PRIMARY KEY (album_id);
ALTER TABLE Albums MODIFY album_id INTEGER NOT NULL AUTO_INCREMENT;

-- Changing Album name in songs table into Album_ID according to the Albums table and setting up foreign key connection with Songs Table
UPDATE Songs t1, Albums t2 SET t1.ALBUM = t2.album_id WHERE t1.ALBUM = t2.ALBUM;
ALTER TABLE Songs MODIFY ALBUM INTEGER NOT NULL;
ALTER TABLE Songs ADD FOREIGN KEY(ALBUM) REFERENCES Albums(album_id);


-- =======================================================================================================================


-- Creating Genres table - Contains Genre Types
CREATE TABLE Genre AS (SELECT DISTINCT(GENRE) FROM Songs);
CREATE TABLE Genres AS (SELECT ROW_NUMBER() OVER() as genre_id, GENRE FROM Genre);
DROP TABLE Genre;

-- Add primary key to Genres table
ALTER TABLE Genres ADD PRIMARY KEY (genre_id);
ALTER TABLE Genres MODIFY genre_id INTEGER NOT NULL AUTO_INCREMENT;

-- Chaning Genre name in songs table into genre_id according to the Genres table and setting up foreign key connection
UPDATE Songs t1, Genres t2 SET t1.GENRE = t2.genre_id WHERE t1.GENRE = t2.GENRE;
ALTER TABLE Songs MODIFY GENRE INTEGER NOT NULL;
ALTER TABLE Songs ADD FOREIGN KEY(GENRE) REFERENCES Genres(genre_id);


-- =======================================================================================================================


-- Creating Artists table - Contains Artist Info
CREATE TABLE Artist AS (SELECT DISTINCT(ARTIST) FROM Songs);
CREATE TABLE Artists AS (SELECT ROW_NUMBER() OVER() as artist_id, ARTIST FROM Artist);
DROP TABLE Artist;

-- Add primary key to albums
ALTER TABLE Artists ADD PRIMARY KEY (artist_id);
ALTER TABLE Artists MODIFY artist_id INTEGER NOT NULL AUTO_INCREMENT;

-- Chaning Artist name in songs table into genre_id according to the Artists table and setting up foreign key connection
UPDATE Songs t1, Artists t2 SET t1.ARTIST = t2.artist_id WHERE t1.ARTIST = t2.ARTIST;
ALTER TABLE Songs MODIFY ARTIST INTEGER NOT NULL;
ALTER TABLE Songs ADD FOREIGN KEY(ARTIST) REFERENCES Artists(artist_id);
