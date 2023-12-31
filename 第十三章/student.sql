CREATE TABLE test.student (
  `姓名` VARCHAR(255) NOT NULL,
  `年龄` INT NOT NULL,
  `性别` VARCHAR(10) NOT NULL,
  `学号` VARCHAR(10) NOT NULL,
  `科目` VARCHAR(255) NOT NULL,
  `城市` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`学号`)
);


INSERT INTO test.student VALUES ('张三', '20', '男', '1001', '数学', '上海');
INSERT INTO test.student VALUES ('张四', '19', '男', '1002', '语文', '上海');
INSERT INTO test.student VALUES ('王明', '16', '男', '1003', '编程', '北京');
INSERT INTO test.student VALUES ('菲雪儿', '21', '女', '1004', '吉他', '北京');
INSERT INTO test.student VALUES ('周顺', '18', '男', '1005', '数学', '深圳');
INSERT INTO test.student VALUES ('李明', '22', '男', '1006', '编程', '成都');
INSERT INTO test.student VALUES ('玲珑', '23', '女', '1007', '吉他', '北京');
INSERT INTO test.student VALUES ('王红', '18', '女', '1008', '语文', '成都');
INSERT INTO test.student VALUES ('周志华', '20', '男', '1009', '数学', '深圳');
INSERT INTO test.student VALUES ('王菲', '23', '女', '1010', '唱歌', '上海');
INSERT INTO test.student VALUES ('阡陌', '24', '女', '1011', '唱歌', '北京');
INSERT INTO test.student VALUES ('jack', '25', '男', '1014', 'study', '北京');
INSERT INTO test.student VALUES ('nike', '25', '男', '1016', '吃鸡', '成都');
INSERT INTO test.student VALUES ('mary', '25', '女', '1017', '英语', '北京');
