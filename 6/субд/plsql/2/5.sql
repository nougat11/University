CREATE OR REPLACE PROCEDURE restore_students(r_time in TIMESTAMP) IS
BEGIN
FOR action IN (
SELECT * FROM logging_actions WHERE r_time <= ex_time ORDER BY id DESC)
LOOP
IF action.operation = 'INSERT' THEN
DELETE students WHERE id = action.stud_id;
END IF;
IF action.operation = 'UPDATE' THEN
UPDATE students SET
id = action.stud_id,
name = action.stud_name,
group_id = action.stud_group_id
WHERE id = action.nstud_id;
END IF;
IF action.operation = 'DELETE' THEN
INSERT INTO students VALUES (action.stud_id, action.stud_name, action.stud_group_id);
END IF;
END LOOP;
END;