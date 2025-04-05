create table if not exists note
(
    id int auto_increment comment 'Primary Key' primary key,
    text varchar(255) null,
    title varchar(255) null,
    location varchar(255) null
);

insert into note (id, text, title, location) values (1, 'Job Description 1', 'Job Title 1', 'Location 1');
insert into note (id, text, title, location) values (2, 'Job Description 2', 'Job Title 2', 'Location 2');
insert into note (id, text, title, location) values (3, 'Job Description 3', 'Job Title 3', 'Location 3');
insert into note (id, text, title, location) values (4, 'Job Description 4', 'Job Title 4', 'Location 4');
insert into note (id, text, title, location) values (5, 'Job Description 5', 'Job Title 5', 'Location 5');

