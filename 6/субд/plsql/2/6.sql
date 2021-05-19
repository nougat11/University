CREATE OR REPLACE TRIGGER c_val_update
AFTER INSERT OR UPDATE OR DELETE
ON students
for each row
BEGIN
IF INSERTING THEN
UPDATE groups
SET C_VAL = C_VAL + 1

WHERE id = :new.group_id;
END IF;
IF INSERTING THEN
UPDATE groups
SET C_VAL = C_VAL - 1
WHERE id = :old.group_id;
UPDATE groups
SET C_VAL = C_VAL + 1
WHERE id = :new.group_id;
END IF;
IF DELETING THEN
UPDATE groups
SET C_VAL = C_VAL - 1
WHERE id = :old.group_id;
END IF;
END;