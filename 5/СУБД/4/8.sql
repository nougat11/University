USE students1;

SELECT
	'Фамилия' as Tab,
	count(case when val.min = length(name) then length(name) else null end) as min,
    count(case when val.max = length(name) then length(name) else null end) as max,
    count(case when val.avg = length(name) then length(name) else null end) as avg
FROM
	name1, (
				SELECT
					MIN(length(name)) as 'min',
					MAX(length(name)) as 'max', 
					ROUND(AVG(length(name)), 0) as 'avg'
				FROM
					name1) as val
UNION ALL
SELECT
	'Имя' as Tab,
	count(case when val.min = length(name) then length(name) else null end) as min,
    count(case when val.max = length(name) then length(name) else null end) as max,
    count(case when val.avg = length(name) then length(name) else null end) as avg
FROM
	name2, (
				SELECT
					MIN(length(name)) as 'min',
					MAX(length(name)) as 'max', 
					ROUND(AVG(length(name)), 0) as 'avg'
				FROM
					name2) as val
UNION ALL
SELECT
	'Страна' as Tab,
	count(case when val.min = length(country) then length(country) else null end) as min,
    count(case when val.max = length(country) then length(country) else null end) as max,
    count(case when val.avg = length(country) then length(country) else null end) as avg
FROM
	country, (
				SELECT
					MIN(length(country)) as 'min',
					MAX(length(country)) as 'max', 
					ROUND(AVG(length(country)), 0) as 'avg'
				FROM
					country) as val
UNION ALL
SELECT
	'Регион' as Tab,
	count(case when val.min = length(region) then length(region) else null end) as min,
    count(case when val.max = length(region) then length(region) else null end) as max,
    count(case when val.avg = length(region) then length(region) else null end) as avg
FROM
	regions, (
				SELECT
					MIN(length(region)) as 'min',
					MAX(length(region)) as 'max', 
					ROUND(AVG(length(region)), 0) as 'avg'
				FROM
					regions) as val
UNION ALL
SELECT
	'Город' as Tab,
	count(case when val.min = length(city) then length(city) else null end) as min,
    count(case when val.max = length(city) then length(city) else null end) as max,
    count(case when val.avg = length(city) then length(city) else null end) as avg
FROM
	city, (
				SELECT
					MIN(length(city)) as 'min',
					MAX(length(city)) as 'max', 
					ROUND(AVG(length(city)), 0) as 'avg'
				FROM
					city) as val
UNION ALL
SELECT
	'ВУЗ' as Tab,
	count(case when val.min = length(full) then length(full) else null end) as min,
    count(case when val.max = length(full) then length(full) else null end) as max,
    count(case when val.avg = length(full) then length(full) else null end) as avg
FROM
	university, (
				SELECT
					MIN(length(full)) as 'min',
					MAX(length(full)) as 'max', 
					ROUND(AVG(length(full)), 0) as 'avg'
				FROM
					university) as val;