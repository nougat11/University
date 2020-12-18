use students1;
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE address;
INSERT INTO address(id_country, id_regions,id_district,  id_city, id_typecity,id_street, id_type_street, house, corps, flat, post_index, number)
WITH cte_country AS (SELECT id FROM country ORDER BY RAND()),
cte_regions AS (SELECT id from regions ORDER BY RAND()),
cte_district AS (SELECT id from districts ORDER BY RAND()),
cte_city AS (SELECT id from city ORDER BY RAND()),
cte_typecity AS (SELECT id from type_city ORDER BY RAND()),
cte_street AS (SELECT id from streets ORDER BY RAND()),
cte_type_street AS (SELECT id from streets ORDER BY RAND()),
result as (SELECT 
			floor(rand()*(1024 - 1) + 1) as house,
            floor(rand()*(10 - 1) + 1) as corps,
            floor(rand()*(1024 - 1) + 1) as flat,
            floor(rand()*563552) as post_index,
            floor(rand()*1000000000000000) as number,
            c.id as id_country, 
			r.id as id_regions, 
			d.id as id_district,
            ci.id as id_city,
            tc.id as id_typecity,
            s.id as id_street,
            ts.id as id_type_street
            
            from cte_country c
            cross join cte_regions r
            cross join cte_district d
            cross join cte_city ci
            cross join cte_typecity tc
            cross join cte_street s
            cross join cte_type_street as ts
            )
select * from result limit 10000;
select * from address;
