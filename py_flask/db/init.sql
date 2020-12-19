-- 데이터베이스 생성
create database python_db;

-- 지금부터 사용하는 쿼리는 이 데이터베이스를 이용한다
use python_db;

-- 유저 테이블 생성
CREATE TABLE `users` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`uid` VARCHAR(32) NOT NULL COLLATE 'utf8_general_ci',
	`upw` VARCHAR(32) NOT NULL COLLATE 'utf8_general_ci',
	`name` VARCHAR(16) NOT NULL COLLATE 'utf8_general_ci',
	`regdate` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY (`id`) USING BTREE
)
COMMENT='회원 테이블'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=2
;

-- row 데이터 추가 -> 회원가입
INSERT INTO `python_db`.`users` (`id`, `uid`, `upw`, `name`, `regdate`) VALUES ('2', 'guest', '1234', '게스트', '2020-12-01 09:44:22');

-- row 데이터 삭제
DELETE FROM `python_db`.`users` WHERE  `id`=1;


