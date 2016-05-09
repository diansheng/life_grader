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

insert into life_recorder_db.recorder_timelog (id, urs, activity, duration) values (1, '', 1, 2);
insert into life_recorder_db.recorder_timelog (id, urs, activity, duration) values (2, '', 4, 1);
insert into life_recorder_db.recorder_timelog (id, urs, activity, duration) values (3, '', 2, 3);
insert into life_recorder_db.recorder_timelog (id, urs, activity, duration) values (4, '', 3, 1);
insert into life_recorder_db.recorder_timelog (id, urs, activity, duration) values (5, '', 3, 2);