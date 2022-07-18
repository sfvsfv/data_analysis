-- 查询所有
-- SELECT * FROM score

--  案例一
-- SELECT NAME 
-- FROM
-- 	score 
-- WHERE
-- 	chinese < 60 
-- 	OR math < 60 
-- 	OR English < 60
-- 案例二
-- select max(math)
-- from score

-- SELECT name
-- FROM
-- 	score 
-- WHERE
-- 	math = ( SELECT MAX( math ) FROM score );
-- 案例三
-- SELECT NAME 
-- FROM
-- 	score 
-- WHERE
-- 	chinese > 80 
-- 	AND math > 80 
-- 	AND English > 80

-- 案例四
-- SELECT
-- 	ifNull ( ( 
-- 	SELECT DISTINCT English 
-- 	FROM score 
-- 	ORDER BY English DESC LIMIT 1, 1 ), NULL ) 
-- 	AS '数学成绩第二'

