
--- -------------------------------------
--- table structure for user
--- -------------------------------------
DROP TABLE IF  EXISTS `user`;
CREATE TABLE `user`(
	id int(11) PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(100) NOT Null COMMENT "用户名",
	email VARCHAR(100) NOT NULL COMMENT "邮箱",
	password VARCHAR(256) NOT NULL COMMENT "hash 密码是",
	create_at VARCHAR(128) NOT NULL COMMENT "创建时间",
	update_at VARCHAR(128) COMMENT "更新时间",
	UNIQUE KEY  username (username)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT "用户表";


--- -------------------------------------
--- table structure for role
--- -------------------------------------

CREATE TABLE `role`(
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `role_name` VARCHAR(100) NOT NULL COMMENT '角色名称',
    `comment` VARCHAR(100) NOT null COMMENT "角色名称备注",
    `ststus` INT(11) DEFAULT 0 COMMENT "状态，默认为0， 0 有效，1无效",
    `create_at` VARCHAR(128) NOT NULL COMMENT "创建时间",
    `update_at` VARCHAR(128) DEFAULT NULL COMMENT "更新时间",
	 UNIQUE KEY  role_name (role_name)
     PRIMARY KEY (`id`) USING BTREE
     )ENGINE=InnoDB DEFAULT CHARSET=utf8;

--- -------------------------------------
--- records for role
--- -------------------------------------

BEGIN;
INSERT INTO `role` VALUES (1,'admin', '超级管理员',0, '1548224396000', null);
INSERT INTO `role` VALUES (2,'dev', '开发',0, '1548224396000', null);
INSERT INTO `role` VALUES (3,'test', '测试',0, '1548224396000', null);
INSERT INTO `role` VALUES (4,'opt', '运维',0, '1548224396000', null);
INSERT INTO `role` VALUES (5,'prod', '产品',0, '1548224396000', null);
INSERT INTO `role` VALUES (6,'owner', '项目管理员',0, '1548224396000', null);
INSERT INTO `role` VALUES (7,'visitor', '访客',0, '1548224396000', null);
COMMIT;

--- -------------------------------------
--- table structure for user_role
--- -------------------------------------

DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role`(
    id INT(11) AUTO_INCREMENT,
    user_id INT(11) NOT NULL COMMENT "用户id",
    role_id INT(11) NOT NULL COMMENT "角色id",
    PRIMARY KEY(`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8;

