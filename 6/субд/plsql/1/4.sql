SET SERVEROUTPUT ON SIZE UNLIMITED;
DECLARE
ans CHAR(150);
FUNCTION INSERT_QUERY(id_input NUMBER) RETURN CHAR
IS
k NUMBER;
BEGIN
SELECT VAL INTO k
FROM MyTable
WHERE ID = id_input;
RETURN 'INSERT INTO MyTable VALUES ('||id_input||','||k||');';
END INSERT_QUERY;
BEGIN
ans := INSERT_QUERY(75);
DBMS_OUTPUT.PUT_LINE(ans);
END;