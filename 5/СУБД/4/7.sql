USE students1;

SELECT
	'Фамилия', MAX(LENGTH(name)), AVG(LENGTH(name)), MIN(LENGTH(name))
FROM
	name1
UNION ALL
SELECT
	'Имя', MAX(LENGTH(name)), AVG(LENGTH(name)), MIN(LENGTH(name))
FROM
	name2
UNION ALL
SELECT
	'Страна', MAX(LENGTH(country)), AVG(LENGTH(country)), MIN(LENGTH(country))
FROM
	country
UNION ALL
SELECT
	'Регион', MAX(LENGTH(region)), AVG(LENGTH(region)), MIN(LENGTH(region))
FROM
	regions
UNION ALL
SELECT
	'Город', MAX(LENGTH(city)), AVG(LENGTH(city)), MIN(LENGTH(city))
FROM
	city
UNION ALL
SELECT
	'ВУЗ', MAX(LENGTH(full)), AVG(LENGTH(full)), MIN(LENGTH(full))
FROM
	university;



    
    