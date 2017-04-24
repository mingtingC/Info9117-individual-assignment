drop table if exists users;
create table users(
  username text primary key,
  password text not null
);
insert into users values('admin', 'admin');
insert into users values('yvonne', '1215');
insert into users values('test', 'test123');

