/*
SQLyog Community v11.31 (64 bit)
MySQL - 5.5.30 : Database - carparking_python
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`carparking_python` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `carparking_python`;

/*Table structure for table `carpark` */

DROP TABLE IF EXISTS `carpark`;

CREATE TABLE `carpark` (
  `CarNo` int(9) DEFAULT NULL,
  `CustomerName` varchar(781) DEFAULT NULL,
  `MobileNo` varchar(651) DEFAULT NULL,
  `SloatNo` int(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `carpark` */

insert  into `carpark`(`CarNo`,`CustomerName`,`MobileNo`,`SloatNo`) values (22,'dsf','345',25);

/*Table structure for table `carsloat` */

DROP TABLE IF EXISTS `carsloat`;

CREATE TABLE `carsloat` (
  `IDd` varchar(22) DEFAULT NULL,
  `photo` varchar(123) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `carsloat` */

insert  into `carsloat`(`IDd`,`photo`) values ('1','1.JPG'),('2','2.JPG'),('3','1.JPG'),('4','1.JPG'),('5','1.JPG'),('6','2.JPG'),('7','1.JPG'),('8','1.JPG'),('9','1.JPG'),('10','2.JPG'),('11','2.JPG'),('12','1.JPG'),('13','1.JPG'),('14','2.JPG'),('15','1.JPG'),('16','2.JPG'),('17','1.JPG'),('18','2.JPG'),('19','1.JPG'),('20','1.JPG'),('21','2.JPG'),('22','2.JPG'),('23','1.JPG'),('24','2.JPG'),('25','1.JPG');

/*Table structure for table `reg` */

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `user_nm` varchar(561) DEFAULT NULL,
  `password` varchar(123) DEFAULT NULL,
  `Emailid` varchar(77) DEFAULT NULL,
  `mob` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `reg` */

insert  into `reg`(`user_nm`,`password`,`Emailid`,`mob`) values ('a','b',NULL,NULL),('RAJ','009','ERTR','4563'),('122','sdf','3453','3');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
