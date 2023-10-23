CREATE DOMAIN
    phone_number AS TEXT
    CHECK (VALUE ~ '^[0-9]{10}$');

drop table if exists contacts;

create table if not exists contacts (
    id int NOT NULL,
    first varchar(50),
    last varchar(50),
    phone phone_number [],
    email text [],
    PRIMARY KEY (id)
);

insert into contacts (id, first, last, phone, email) values
(1, 'John', 'Doe', '{"0987654321", "1234567890"}', '{"jd@stlawu.edu", "jd@gmail.com"}'),
(2, 'Jane', 'Doe', '{"1234567890", "1111111111", 9887766445}', '{"janed@outlook.com"}'),
(3, 'Jim', 'Shmo', '{"9887766445", "1234567890", "1111111111"}', '{"janed@outlook.com"}');

select phone[2] from contacts where id = 1;

delete from contacts;

update contacts set phone[2] = '5555555555' where id = 1;

select phone[1] from contacts;

SELECT phone FROM contacts;

-- there is a slice syntax for arrays

select * from contacts where email[1] ~ '.*@gmail.com' OR
                             email[2] ~ '.*@gmail.com'; -- and so on

-- https://dba.stackexchange.com/questions/228235/match-string-pattern-to-any-array-element/228262#228262

create function reverse_like (text, text)
    returns boolean
    language sql as
    $$ select $2 like $1 $$ IMMUTABLE PARALLEL SAFE;

create function reverse_tilde (text, text)
    returns boolean
    language sql as
    $$ select $2 ~ $1 $$  IMMUTABLE PARALLEL SAFE;

create operator <~~ ( function =reverse_like, leftarg = text, rightarg=text );
create operator <~ ( function =reverse_tilde, leftarg = text, rightarg=text );

-- Doesn't work
select * from contacts where '.*@gmail.com' ~ ANY (email);

select * from contacts where '.*@gmail.com' <~ ANY (email);

-- Doesn't work
select * from contacts where '%@gmail.com' LIKE ANY (email);

-- Works
select * from contacts where '%@gmail.com' <~~ ANY (email);

select email from contacts;
