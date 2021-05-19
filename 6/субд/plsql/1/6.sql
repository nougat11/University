SET SERVEROUTPUT ON SIZE UNLIMITED;
DECLARE
ans NUMBER;
FUNCTION YEAR_SALARY(month_salary INTEGER, year_percent
INTEGER) RETURN NUMBER IS
BEGIN
if year_percent < 0 THEN RAISE VALUE_ERROR; END IF;
ans := (1 + year_percent / 100) * 12 * month_salary;
RETURN ans;
END YEAR_SALARY;
BEGIN
ans:= YEAR_SALARY(1, -1);
DBMS_OUTPUT.PUT_LINE(ans);
EXCEPTION
WHEN VALUE_ERROR THEN
DBMS_OUTPUT.PUT_LINE('Некорректный формат входных
данных');
END;