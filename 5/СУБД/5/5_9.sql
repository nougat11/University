USE students1;

SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE personal_data;
INSERT INTO personal_data(id_address1, id_address2, id_address3, id_university, id_faculty, id_cathedra, id_specaility) 
WITH cte_address1 AS (SELECT id FROM address ORDER BY RAND() limit 10),
cte_address2 AS (SELECT id FROM address ORDER BY RAND() limit 10),
cte_address3 AS (SELECT id FROM address ORDER BY RAND() limit 10),
cte_university AS (SELECT id FROM university ORDER BY RAND() limit 10),
cte_faculty AS (SELECT id FROM faculty ORDER BY RAND() limit 10),
cte_cathedra AS (SELECT id FROM cathedra ORDER BY RAND() limit 10),
cte_speciality AS (SELECT id FROM speciality ORDER BY RAND() limit 10),
result as (SELECT a1.id as id_address1,
				a2.id as id_address2,
                a3.id as id_address3,
                u.id as id_university,
                f.id as id_faculty,
                c.id as id_cathedra,
                s.id as id_specaility
			from cte_address1 a1
            cross join cte_address2 a2
             cross join cte_address2 a3
             cross join cte_university u
              cross join cte_faculty f
              cross join cte_cathedra c
              cross join cte_speciality s)
select * from result limit 1000000;
select * from personal_data;
