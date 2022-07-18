-- 查询所有
-- SELECT
-- 	* 
-- FROM
-- 	email
-- 案例一
-- select email as '重复邮箱'
-- from email 
-- group by email
-- having count(email) > 1;
-- 
-- 案例二
DELETE a 
FROM
	email a
	INNER JOIN email b 
WHERE
	a.email = b.email 
	AND a.id > b.id;
SELECT
	* 
FROM
	email