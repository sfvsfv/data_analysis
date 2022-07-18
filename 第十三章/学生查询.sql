-- select name from student;

-- select * from student;

-- select name,sex from student;

-- select distinct hometown from student;

-- select count(distinct hobby) from student;

-- select * from student where hometown='上海';

-- select * from student where ID=1005;

-- select * from student where ID !=1005;

-- select * from student where ID between 1002 and 1006;

-- select name from student where ID>1008;

-- select * from student where age>=21;

-- select name from student where age <19;

-- select * from student where name like '王%';

-- select * from student where name like '%明';

-- select * from student where hometown in ('成都','北京');

-- select * from student where hobby in ('吉他','唱歌');

-- select * from student where hometown='北京' and age<22;

-- select  * from student where hobby='编程' or hobby='唱歌';

-- select * from student where  not hometown='上海';

-- select * from student where age<21 and (hometown='北京' or hometown='深圳');

-- select * from student where name like '王%' and  (hobby='编程' or  hobby='数学');


-- select * from super order by price;

-- select * from super order by price  desc;

-- select * from super order by price,ID;

-- insert into super  values ('卤蛋',2,16);
-- select * from super;

-- insert into super  values ('蛋糕',10,17),('鸡腿',6.5,18);
-- select * from super;

-- insert into super (name,ID,price) values ('计算机网络',19,35),('数据库原理',20,37.5),("大数据",21,37);
-- select * from super;

-- insert into super  (price,ID) values (14,17),(13,5);
-- select * from super;


-- select * from super where name is NULL;

-- select * from super where name is not NULL;


-- update super set price=12 where name='蛋糕';
-- select * from super;

-- update super set ID=8  where name='鸡腿';
-- select * from super;


-- update super set name='蓝牙',price=80 where ID=15;
-- select * from super;

-- delete from super where name is NULL;
-- select * from super;

-- delete from super where ID=1;
-- select * from super;

-- select  * from student limit  5;

-- select * from student where hometown='上海' limit 2;

-- select min(price) from super 

-- select min(price) as '最低价' from super 

-- 	select * from super where price = (select min(price) from super)

-- select * from super where price = (select max(price) from super);

-- select count(ID) from super;

-- select count(ID)  as "数量"  from super;

-- select avg(price) as  "平均价格"  from super;

-- select sum(price) as "总共价格" from super;

-- select * from student;

-- select * from student where name like '李%';

-- select * from student where name like '%红';

-- select * from student where name like '%王%';

-- select * from student where name like '周%华';

-- select * from student where name like  '______儿%';  -- 两个下划线代表一个字符

-- insert into student values ('jack',25,'男',1014,'study','北京');
-- select * from student;

-- select * from student where name like '_a%';

-- select * from student where name like 'j__%';

-- insert into student values ('nike',25,'男',1016,'吃鸡','成都'),('mary',25,'女',1017,'英语','北京');
-- select * from student;

-- select * from student where name like 'n%';

-- select * from student where name like '_a%';

-- select  * from student where name like  '[!j]%';

-- select * from student where hometown in ('成都','深圳');
-- select * from student where hometown='成都' or hometown='深圳';

-- select * from student where hometown not in ('北京','上海');

-- select * from student where hometown in (select hometown from student where name='张三');

-- select name as fullname from  student ;

-- select name as fullname,age as sage from student;

-- select count(name) as '数量',hometown as '家乡' 
-- from student group by hometown;

-- select count(name) as '数量',hometown as '家乡' 
-- from student group by hometown 
-- order by count(name) DESC;

-- select count(name) as '数量',hometown as '家乡'  from student 
-- group by hometown  
-- having count(name) >2;

-- select count(name) as '数量',hometown as '家乡'  from student 
-- group by hometown  
-- having count(name) >2
-- order by count(name);

-- select name  as '名字' from one union select name from  two;

-- select name  as '名字' from one 
-- union 
-- select name from one ;

-- select name  as '名字' from one 
-- union  all
-- select name from one ;


-- select ID,name from one  where account='city'
-- union
-- select ID,name from two  where account='city';

-- select * from one,two

-- select  user.ID ,user.name,takeout.goods
-- from user  
-- inner join  takeout  
-- on user.ID=takeout.ID;

-- select user.name as '名字',user.phone as  '电话号码',takeout.goods  as '购买'
-- from user 
-- left join takeout on
-- user.ID=takeout.ID;


-- select user.name as '名字',user.phone as  '电话号码',takeout.goods  as '购买'
-- from user 
-- right join takeout on
-- user.ID=takeout.ID;


-- select user.name,takeout.goods
-- from user
-- cross join takeout;


-- select * from user natural join takeout;

-- select * from user natural left  join takeout;

-- select * from user natural right  join takeout;


