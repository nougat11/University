CREATE OR REPLACE PROCEDURE REPLACE_OBJECT
(
schema1 IN VARCHAR2,
schema2 IN VARCHAR2,
object_type IN VARCHAR2,
object_name IN VARCHAR2
)
AS
query_string VARCHAR2(100);
BEGIN

FOR src IN (SELECT line, text FROM ALL_SOURCE WHERE OWNER = schema1 AND
NAME = object_name)
LOOP
IF src.line =1 THEN
query_string := 'CREATE OR REPLACE ' || REPLACE(src.text, LOWER(object_name),
schema2 || '.' || object_name);
ELSE
query_string := query_string || src.text;
END IF;
END LOOP;
EXECUTE IMMEDIATE query_string;
END REPLACE_OBJECT;
/
CREATE OR REPLACE PROCEDURE CREATE_OBJECT
(
schema1 IN VARCHAR2,

schema2 IN VARCHAR2,
object_type IN VARCHAR2,
object_name IN VARCHAR2
)
AS
query_string VARCHAR2(100);
BEGIN

FOR src IN (SELECT line, text FROM ALL_SOURCE WHERE OWNER = schema1 AND
NAME = object_name)
LOOP
IF src.line =1 THEN
query_string := 'CREATE ' || REPLACE(src.text, LOWER(object_name), schema2 || '.' ||
object_name);
ELSE
query_string := query_string || src.text;
END IF;
END LOOP;
EXECUTE IMMEDIATE query_string;
END CREATE_OBJECT;
/
CREATE OR REPLACE PROCEDURE DELETE_OBJECT
(
schema1 IN VARCHAR2,
object_type IN VARCHAR2,
object_name IN VARCHAR2
)

AS
delete_query VARCHAR(100);
BEGIN
delete_query := 'DROP ' || object_type || ' ' || schema1 || '.' || object_name;
EXECUTE IMMEDIATE delete_query;
END DELETE_OBJECT;
/
CREATE OR REPLACE PROCEDURE COMPARE_OBJECTS
(
schema1 IN VARCHAR2,
schema2 IN VARCHAR2,
object_type IN VARCHAR2
)
AS
diff NUMBER :=0;
BEGIN
FOR pair IN ( SELECT obj1.NAME AS name1, obj2.NAME AS name2
FROM
(SELECT OBJECT_NAME name FROM ALL_OBJECTS
WHERE OBJECT_TYPE = object_type AND OWNER = schema1) obj1
FULL JOIN
(SELECT OBJECT_NAME name FROM ALL_OBJECTS
WHERE OBJECT_TYPE = object_type AND OWNER = schema2) obj2
ON obj1.name = obj2.name ) LOOP

IF pair.name1 IS NULL THEN

DELETE_OBJECT(schema2,object_type, pair.name2);
dbms_output.put_line('D');
ELSIF pair.name2 IS NULL THEN
CREATE_OBJECT(schema1, schema2, object_type, pair.name1);
dbms_output.put_line('C');
ELSE
SELECT COUNT(*) INTO diff
FROM
all_source src1 FULL JOIN all_source src2
ON src1.name = src2.name
WHERE src1.name= pair.name1 AND src1.line = src2.line
AND src1.text != src2.text
AND src1.OWNER = schema1 AND src2.OWNER = schema2;

IF diff > 0 THEN
REPLACE_OBJECT(schema1,schema2,object_type,pair.name1);
dbms_output.put_line('R');
END IF;
END IF;
END LOOP;

END COMPARE_OBJECTS;
/
EXEC COMPARE_OBJECTS('DEV', 'PROD', 'PROCEDURE')