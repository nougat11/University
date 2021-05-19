CREATE SEQUENCE students_seq;
CREATE OR REPLACE TRIGGER unique_student
BEFORE INSERT
ON STUDENTS
FOR EACH ROW
DECLARE
counter number;
BEGIN
IF :new.id IS NOT NULL THEN
select count(*) as c into counter

from students
where id = :new.id;
IF counter > 0 THEN
raise_application_error(-20000, 'Неверный id. Он должен быть
уникальным. Попробуйте другой.');
END IF;
ELSE
counter := 1;
while counter > 0
LOOP
SELECT students_seq.nextval
INTO :new.id
FROM dual;
select count(*) as c into counter
from students
where id = :new.id;
END LOOP;
END IF;
END;