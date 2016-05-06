drop schema life_recorder_db;

create schema if not exists life_recorder_db;
use life_recorder_db;

drop table life_recorder_db;

CREATE TABLE IF NOT EXISTS `timelog` (
  `id` varchar(45) NOT NULL,
  `user` varchar(45) DEFAULT NULL,
  `activity` int(11) NOT NULL,
  `time_consumed` datetime DEFAULT NULL,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;