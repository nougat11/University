USE students1;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE name3;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO name3(name)
SELECT CASE
	WHEN RIGHT(name, 1) IN ('ж', 'ц', 'ч', 'ш', 'щ') THEN
		CONCAT(name, 'евич')
	ELSE
		CONCAT(name, 'ович')
	END
FROM name2
WHERE RIGHT(name, 1) NOT IN ('а', 'я')
ORDER BY name;
