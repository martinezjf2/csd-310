

/* Jeffrey Martinez
SQL Insert Statements
May 4, 2022
Module 10.3 Assignment

mysql -u root -p */

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- Create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- CREATE STORE TABLE
CREATE TABLE store (
    store_id    INT                 NOT NULL        AUTO_INCREMENT,
    locale      VARCHAR(500)        NOT NULL,
    PRIMARY KEY(store_id)
);
-- CREATE BOOK TABLE
CREATE TABLE book (
    book_id     INT                 NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)        NOT NULL,
    author      VARCHAR(200)        NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

-- CREATE USER TABLE
CREATE TABLE user (
    user_id         INT             NOT NULL        AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);



-- CREATE WISHLIST TABLE 
CREATE TABLE wishlist (
    wishlist_id     INT             NOT NULL        AUTO_INCREMENT,
    user_id         INT             NOT NULL,
    book_id         INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
); 


-- INSERT STORE RECORD (1)
INSERT INTO store(locale)
    VALUES('1234 Whoknows St, Farmingdale, New York, 11725');




-- INSERT BOOK RECORDS (9)
INSERT INTO book(book_name, author) 
    VALUES("The Time Machine", "H.G. Wells");

INSERT INTO book(book_name, author) 
    VALUES("To Kill a Mockingbird", "Harper Lee");

INSERT INTO book(book_name, author) 
    VALUES("The Night Trilogy", "Elie Wiesel");

INSERT INTO book(book_name, author) 
    VALUES("The Coffee Bean", "Jon Gordon");

INSERT INTO book(book_name, author) 
    VALUES("Finding Chika", "Mitch Albom");

INSERT INTO book(book_name, author) 
    VALUES("The Power Of Your Leadership", "John C. Maxwell");

INSERT INTO book(book_name, author) 
    VALUES("The Art of Racing in the Rain", "Garth Stein");

INSERT INTO book(book_name, author) 
    VALUES("Bold New You", "Justin Patton");

INSERT INTO book(book_name, author) 
    VALUES("The Great Gatsby", "F.Scott Fitzgerald");



-- INSERT USER RECORDS (3)
INSERT INTO user(first_name, last_name)
    VALUES('John', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('Anthony', 'Williams');

INSERT INTO user(first_name, last_name)
    VALUES('Marcus', 'Junior');



-- INSERT WISHLIST RECORDS (1 for each user)
INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Bold New You')
    );

INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Anthony'),
        (SELECT book_id FROM book WHERE book_name = 'The Art of Racing in the Rain')
    );

INSERT INTO wishlist (user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Marcus'),
        (SELECT book_id FROM book WHERE book_name = 'The Coffee Bean')
    );
