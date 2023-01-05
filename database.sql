create user taskuploguser identified by 'taskuplogpass';
create database taskuplogdb;
grant all privileges on taskuplogdb.* to taskuploguser with grant option;
flush privileges;

CREATE TABLE registro (
  servidor VARCHAR(20) NOT NULL,
  plugin VARCHAR(255) NOT NULL,
  version VARCHAR(20) NOT NULL,
  fecha DATE NOT NULL,
  obsoleto BOOLEAN NOT NULL DEFAULT FALSE,
  premium BOOLEAN NOT NULL DEFAULT FALSE,
  db BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (servidor,plugin,fecha)
);
