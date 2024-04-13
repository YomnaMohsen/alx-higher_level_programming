-- a script that creates the table id_not_null on your MySQL servers
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT  Default  1,
    name VARCHAR(256) );