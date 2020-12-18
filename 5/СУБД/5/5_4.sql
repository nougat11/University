use students1;
set FOREIGN_KEY_CHECKS = 0;
truncate table grade;

insert into grade(id_grade_type, id_student, id_teacher, id_matter, date)
select gt.id, s.id, t.id, m.id, DATE_ADD('1965-01-01 00:00:00', INTERVAL FLOOR(RAND()*timestampdiff(second, '1965-01-01 00:00:00','2020-12-01 00:00:00')) SECOND)
from
(SELECT id FROM grade_type ORDER BY RAND() limit 100) gt
cross join (SELECT id FROM student ORDER BY RAND() limit 100) s
cross join (SELECT id FROM teacher ORDER BY RAND() limit 100) t
cross join (SELECT id FROM matter ORDER BY RAND() limit 100) m

limit 1000000;


