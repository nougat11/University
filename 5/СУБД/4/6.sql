USE students1;
SELECT "WITHOUT1", COUNT(name)
FROM name1
WHERE name LIKE CONCAT('%', left('Кузьма', 5), '%')
UNION ALL
SELECT "WITHOUT2", count(name)
FROM name1
WHERE name LIKE CONCAT('%', left('Кузьма', 4), '%');
