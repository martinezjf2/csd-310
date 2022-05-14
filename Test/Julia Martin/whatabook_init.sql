/* 
    Julia Martin Module 10 assignment 5-7-22
    Initializing the WhatABook database 
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


-- drop tables if they are present
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- create the user table 
CREATE TABLE user (
    user_id        INT             NOT NULL        AUTO_INCREMENT,
    first_name     VARCHAR(75)     NOT NULL,
    last_name      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
); 

-- create the book table
CREATE TABLE book (
    book_id        INT             NOT NULL         AUTO_INCREMENT,
    book_name      VARCHAR(200)    NOT NULL,
    details        VARCHAR(500),
    Author         VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

-- create the store table
CREATE TABLE store (
    store_id       INT            NOT NULL,
    locale         VARCHAR(500)   NOT NULL,
    PRIMARY KEY(store_id)
);

-- create the wishlist table and set the foreign key
CREATE TABLE wishlist (
    wishlist_id   INT             NOT NULL        AUTO_INCREMENT,
    user_id       INT             NOT NULL,
    book_id       INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book 
    FOREIGN KEY(book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

-- insert user records
INSERT INTO user(first_name, last_name)
    VALUES('Michael', 'Scott');

INSERT INTO user(first_name, last_name)
    VALUES('Dwight', 'Shrute');

INSERT INTO user(first_name, last_name)
    VALUES('Pam', 'Halpert');

-- insert book records
INSERT INTO book(book_name, details, author)
    VALUES('Office Management for Dummies', 'A quick guide to office management', 'John Smith');

INSERT INTO book(book_name, details, author)
    VALUES('Coping with Complaints', 'How to keep your customers satisfied', 'Patrick Dillon');

INSERT INTO book(book_name, details, author)
    VALUES('Surviving a Hostile Work Environment', 'How to keep your job, and your sanity', 'Regina Greene');

INSERT INTO book(book_name, details, author)
    VALUES('All About Beets', 'A comprehensive encyclopedia on your favorite root', 'Mose Shrute');

INSERT INTO book(book_name, details, author)
    VALUES('So Your Boss is an Idiot', 'Dealing with poor management', 'Sherry Tibit');

INSERT INTO book(book_name, details, author)
    VALUES('Drawing 101', 'Basic drawing techniques', 'Bob Ross');

INSERT INTO book(book_name, details, author)
    VALUES('Everything You Need to Know About Paper', 'A guide to all types of paper', 'Helen Cross');

INSERT INTO book(book_name, details, author)
    VALUES('Advanced Karate Techniques', 'Take your Karate to the next level', 'Marcus Droll');

INSERT INTO book(book_name, details, author)
    VALUES('Drugs in the Workplace', 'How to spot unsavory behavior', 'George Pierce');

-- insert store records
INSERT INTO store(store_id, locale)
    VALUES('5643', '13927 Saticoy Street Panorama City CA 91402');

-- insert wishlist records 
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Michael'),
        (SELECT book_id FROM book WHERE book_name = 'Everything You Need to Know About Paper')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Dwight'),
        (SELECT book_id FROM book WHERE book_name = 'Advanced Karate Techniques')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Pam'),
        (SELECT book_id FROM book WHERE book_name = 'So Your Boss is an Idiot')
    );

