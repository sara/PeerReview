create table students(
    id REAL Primary key
    name CHAR(50)
    gender CHAR(10)
    gpa REAL
    gradyear REAL
);

CREATE TABLE reviews(
    authorid REAL
    subjid REAL
    partagain boolean
    score REAL
    FOREIGN KEY (authorid, subjid) REFERENCES students
);

CREATE TRIGGER StuDel
	BEFORE DELETE ON Students as s
    referencing old row as o
	FOR EACH ROW 
    when reviews.authorid = o.id
    BEGIN 
        set reviews.authorid = 0;
    end;