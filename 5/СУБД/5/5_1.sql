USE students1;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE student;


INSERT INTO student(id_name1, id_name2, id_name3, id_personal_data)
WITH cte_name1 AS (SELECT id FROM name1 ORDER BY RAND()),
cte_name2 AS (SELECT id from name2 ORDER BY RAND()),
cte_name3 AS (SELECT id from name3 ORDER BY RAND()),
result as (SELECT n1.id as id_name1, 
			n2.id as id_name2, 
			n3.id as id_name3,
            row_number() over() as id_personal_data
            from cte_name1 n1
            cross join cte_name2 n2
            cross join cte_name3 n3
            )
select * from result limit 1000000;
SET FOREIGN_KEY_CHECKS = 1;