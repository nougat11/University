USE students1;
SELECT "WITHOUT1", COUNT(name)
FROM name2
WHERE name LIKE CONCAT('%', left('Владислав', 8), '%')
UNION ALL
SELECT "WITHOUT2", count(name)
FROM name2
WHERE name LIKE CONCAT('%', left('Владислав', 7), '%');
