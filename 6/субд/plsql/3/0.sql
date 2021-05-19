DROP TABLESPACE tbs_1 INCLUDING CONTENTS AND DATAFILES;
DROP USER prod CASCADE;
CREATE TABLESPACE tbs_1
DATAFILE 'tbs_1.dat'
SIZE 10M
REUSE
AUTOEXTEND ON NEXT 10M MAXSIZE 200M;
CREATE USER prod
IDENTIFIED BY 321
DEFAULT TABLESPACE tbs_1
QUOTA 200M on tbs_1;
GRANT create session TO prod;
GRANT create table TO prod;
GRANT create view TO prod;
GRANT create any trigger TO prod;
GRANT create any procedure TO prod;
GRANT create sequence TO prod;
GRANT create synonym TO prod;
--conn Prod;
CREATE TABLE prod.products
( product_id number(10) not null,
product_name varchar2(50) not null,
category varchar2(50),
CONSTRAINT products_pk PRIMARY KEY (product_id)
);

DROP TABLESPACE tbs_2 INCLUDING CONTENTS AND DATAFILES;
DROP USER dev CASCADE;
CREATE TABLESPACE tbs_2
DATAFILE 'tbs_2.dat'
SIZE 10M
REUSE

AUTOEXTEND ON NEXT 10M MAXSIZE 200M;
CREATE USER dev
IDENTIFIED BY 321
DEFAULT TABLESPACE tbs_2
QUOTA 200M on tbs_2;
GRANT create session TO dev;
GRANT create table TO dev;
GRANT create view TO dev;
GRANT create any trigger TO dev;
GRANT create any procedure TO dev;
GRANT create sequence TO dev;
GRANT create synonym TO dev;
CREATE TABLE dev.products
( product_id number(10) not null,
product_name varchar2(50) not null,
-- category varchar2(50),
CONSTRAINT products_pk PRIMARY KEY (product_id)
);
CREATE TABLE dev.qwer
( qwer_id number(10) not null,
qwer_name varchar2(50) not null,
CONSTRAINT qwer_pk PRIMARY KEY (qwer_id)
);
SET SERVEROUTPUT ON;