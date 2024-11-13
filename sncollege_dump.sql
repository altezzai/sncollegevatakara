-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: risan.mysql.pythonanywhere-services.com    Database: risan$sncollege
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add employee',7,'add_employee'),(26,'Can change employee',7,'change_employee'),(27,'Can delete employee',7,'delete_employee'),(28,'Can view employee',7,'view_employee'),(29,'Can add event',8,'add_event'),(30,'Can change event',8,'change_event'),(31,'Can delete event',8,'delete_event'),(32,'Can view event',8,'view_event'),(33,'Can add news',9,'add_news'),(34,'Can change news',9,'change_news'),(35,'Can delete news',9,'delete_news'),(36,'Can view news',9,'view_news'),(37,'Can add notification',10,'add_notification'),(38,'Can change notification',10,'change_notification'),(39,'Can delete notification',10,'delete_notification'),(40,'Can view notification',10,'view_notification'),(41,'Can add news image',11,'add_newsimage'),(42,'Can change news image',11,'change_newsimage'),(43,'Can delete news image',11,'delete_newsimage'),(44,'Can view news image',11,'view_newsimage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$4Scq2BccsUtNwRk52wFk01$csKIh0FHuwEAzmZrXN/ex/85P9nXoBddm2mckt3Zw8o=',NULL,1,'snclg@vdk','','','sncvatakara@gmail.com',1,1,'2024-01-08 16:31:06.574232');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'myapp','employee'),(8,'myapp','event'),(9,'myapp','news'),(11,'myapp','newsimage'),(10,'myapp','notification'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-01-08 15:36:48.806255'),(2,'auth','0001_initial','2024-01-08 15:36:50.322274'),(3,'admin','0001_initial','2024-01-08 15:36:50.761001'),(4,'admin','0002_logentry_remove_auto_add','2024-01-08 15:36:50.786792'),(5,'admin','0003_logentry_add_action_flag_choices','2024-01-08 15:36:50.808519'),(6,'contenttypes','0002_remove_content_type_name','2024-01-08 15:36:51.016211'),(7,'auth','0002_alter_permission_name_max_length','2024-01-08 15:36:51.203745'),(8,'auth','0003_alter_user_email_max_length','2024-01-08 15:36:51.465093'),(9,'auth','0004_alter_user_username_opts','2024-01-08 15:36:51.496554'),(10,'auth','0005_alter_user_last_login_null','2024-01-08 15:36:51.657089'),(11,'auth','0006_require_contenttypes_0002','2024-01-08 15:36:51.675618'),(12,'auth','0007_alter_validators_add_error_messages','2024-01-08 15:36:51.705459'),(13,'auth','0008_alter_user_username_max_length','2024-01-08 15:36:51.878515'),(14,'auth','0009_alter_user_last_name_max_length','2024-01-08 15:36:52.077234'),(15,'auth','0010_alter_group_name_max_length','2024-01-08 15:36:52.268362'),(16,'auth','0011_update_proxy_permissions','2024-01-08 15:36:52.288941'),(17,'auth','0012_alter_user_first_name_max_length','2024-01-08 15:36:52.536414'),(18,'myapp','0001_initial','2024-01-08 15:36:52.617555'),(19,'myapp','0002_event','2024-01-08 15:36:52.663247'),(20,'myapp','0003_news','2024-01-08 15:36:52.710397'),(21,'myapp','0004_remove_news_photos_newsimage','2024-01-08 15:36:53.065191'),(22,'myapp','0005_notification','2024-01-08 15:36:53.205062'),(23,'myapp','0006_employee_department','2024-01-08 15:36:53.308420'),(24,'myapp','0007_news_date','2024-01-08 15:36:53.411510'),(25,'myapp','0008_news_image_delete_newsimage','2024-01-08 15:36:53.529456'),(26,'myapp','0009_newsimage','2024-01-08 15:36:53.737242'),(27,'sessions','0001_initial','2024-01-08 15:36:53.906981');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0moic5mq3kl6x4ys07h3oxeof5uv7wi8','eyJ1c2VybmFtZSI6IlNuY2xnQHZkayAifQ:1rphAd:UNcI3BXljkO9r83boRWHbT8Txhhx0gUvff-ZfvMqfLA','2024-04-11 04:15:19.159883'),('3uelf8r4u3akbhy4z6co6a5m00nnm45o','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rdVeG:Hb9BLQOQW5608l8Zm7ksH1Fda6_Do5pCk__PpwluULI','2024-03-08 13:31:32.382870'),('3unfv7jd0o4m80le0kqmgsgscddevbfk','eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sjC8N:gg2IdNsy3_W_U7rhEivos6zGB3m_n6XXSIxravw6vUc','2024-09-11 06:26:23.484449'),('al03rlqx1gc5epq7bkr5kpb8wjnm9wap','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rx0Y4:9JRSPJFklBmhmXkesNvY39SIX0cMVRTF0Mg0bAmFUpw','2024-05-01 08:21:44.990553'),('azjd51dgjpgizaiahz4uhxrq86mnu9oq','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sOvwx:mVqAu59onoCzRCMhz7s3YASSA-yV1gpxsruXx3VlZHM','2024-07-17 09:06:51.839871'),('c3arw6ukt3zl790n6j76n6yia0nf7wcg','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rNUAS:l4yckvrd-cABIdrWojr_UHVHkmdczjc14EJIvNvWa6o','2024-01-24 08:42:32.387955'),('g0lyhmaxo8y182kxsz0auy0fpdymg66y','eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sdNh1:a6kNjAJ5ael873WoAWE6mRanpPecAIVAkOhiftOWG1s','2024-08-26 05:34:07.031121'),('gjd0elhalf3eyhl5pnyz6vxt5qfn13po','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sSGRj:VrOSWmyeeYJfT_GBHWC2ly3ovNgLsyoY5DgdzthBW0M','2024-07-26 13:36:23.994116'),('iyzogve7v83pir3by2yimywdz34f5ucx','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sA9WO:gFizY4S9X4BKfplLugsLRn-kPvoLAhZJN4cnE-HgtI4','2024-06-06 14:34:20.454969'),('kkmi2k9rxx3vbmmc83hl7n290j0xfzru','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rVxIe:ZgeJuNjqF2f0AA6FfUQUbcfBLwLDlVUlAT4I4QQYpZA','2024-02-16 17:26:00.784928'),('l7twwbyt5p9d5savj70uugnpe7yx32l3','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rSeKt:gkZ8PnI45A3TjBpz3Uvd4wnfWKpVDuFq3GO-klfA3ss','2024-02-07 14:34:39.775653'),('lb4hpmp926m6jb0pmm2i8uh7xjbufu7e','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rQPMD:sKojkNl7ba-RqzFe4hcCK6vQLtwFoscLbF1X22e83dk','2024-02-01 10:10:45.114206'),('oltczsjc4bczcnk6yrhleuk1ac271i1l','eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sM2eB:FcjO5dVOQEjJNFY8G9jQWzqP59o92rWT96zKvkF0MOQ','2024-07-09 09:39:31.364984'),('psv1fmafijeyfsx586dl49e0xv18s3mb','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sSGRj:VrOSWmyeeYJfT_GBHWC2ly3ovNgLsyoY5DgdzthBW0M','2024-07-26 13:36:23.238813'),('pwxfvu0lnpvjmd8i804p2wbgaq1nfelq','eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sEsLr:eA2WtkUgHKCRjQUx8ImI7eWm1BdzKlAz_YD9SXUtqbQ','2024-06-19 15:14:59.606101'),('qtpvbta5eyzfmtzkf0qedkbcolgrq5a7','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rfDnz:ckDkLQ-rGWK_HSUfUhUtkD9XeBolnuWozKhygB5do50','2024-03-13 06:52:39.127644'),('rigq5oofzqzmwvggkyscl4vv0hbr4sw6','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1s9M68:aBrMiwSGlCYHU8zR7zh4PEtsw3VhcsmQhnoAxHIXwWs','2024-06-04 09:47:56.493559'),('skr0pjcu5x4hd2o4s3zvyoupjaahmaav','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rcgKW:lF8hgr3enevP2DGAvBLz9fKrzplog6kz_CTRggtaiTI','2024-03-06 06:43:44.007883'),('z5zobsgx27i6i8sj6v94tfppti44od1v','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rPfRS:t1WH1qpvXisbnHkIbhNEDhjUg1t-D_Y60r4wKWWapy8','2024-01-30 09:09:06.877660'),('zihya9222sqvgpjuu09b9pm4799gcs31','eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rSBLC:tlZDzARHd2uoOxR1giNq4qvobUBiv00mAy_2WpgpIkQ','2024-02-06 07:37:02.415073');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_employee`
--

DROP TABLE IF EXISTS `myapp_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `qualification` longtext NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_employee`
--

LOCK TABLES `myapp_employee` WRITE;
/*!40000 ALTER TABLE `myapp_employee` DISABLE KEYS */;
INSERT INTO `myapp_employee` VALUES (1,'RAJI M','Head Of Department','photos/1aaa.JPG','MSc Computer Science','COMPUTER SCIENCE'),(3,'PAVITHRAN M T','Assistant Professor','photos/DSC01444.JPG','MCA , PGDCA','COMPUTER SCIENCE'),(4,'VYSAKH O K','Head Of Department','photos/vys.jpg','MCA ,PGDCA','COMPUTER APPLICATION'),(5,'KAVYA VENU K','Assistant Professor','photos/1704697243728_hp2UyyB.jpg','MCA','COMPUTER APPLICATION'),(6,'ABHIRAM KRISHNA A','Assistant Professor','photos/Screenshot_20240109_122852-01.jpeg','MSc Computer Science, NET','COMPUTER APPLICATION'),(7,'ARJUN T','Assistant Professor','photos/IMG_0920.JPG','MCA','COMPUTER APPLICATION'),(8,'SWETHA C P','Assistant Professor','photos/image0.jpeg','MSc Computer Science','COMPUTER SCIENCE'),(9,'AMAL BENNY','Assistant Professor','photos/35419-Amal-3.jpg','MCA,  JRF, NET','COMPUTER APPLICATION'),(10,'HARSHA M','Head Of Department','photos/Harsha_M_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(11,'GARGI KRISHNA','Assistant Professor','photos/Gargikrishna_R_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(12,'THASLEENA P','Assistant Professor','photos/Thasleena_P_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(13,'AVISHNA B','Assistant Professor','photos/Avishna_B_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(14,'ANJITHA S MOHAN','Assistant Professor','photos/Anjitha_S_Mohan_page-0001.jpg','MSc Psychology, NET','PSYCHOLOGY'),(15,'SAMNA ANIL','Assistant Professor','photos/Samna_Anil_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(16,'SURABHI S R','Assistant Professor','photos/Surabhi_S_R_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(17,'SHARON','Assistant Professor','photos/Sharon_Balakrishnan_page-0001.jpg','MSc Psychology','PSYCHOLOGY'),(18,'Dr. ARAVINDAN THAREMMAL','Visiting Faculty','photos/Dr._Aravindan_Tharemmal.jpg','MSc Zoology, PhD','ZOOLOGY'),(19,'Dr. K ANIL','Visiting Faculty','photos/Dr._K._Anil.jpg','MSc Zoology, M Phil. PhD','ZOOLOGY'),(20,'Dr. DEEPTHI M P','Assistant Professor','photos/Dr._Deepthi_M._P..jpg','MSc Zoology. PhD, BEd, SET, NET','ZOOLOGY'),(21,'ARYA VENUGOPAL','Assistant Professor','photos/Arya_Venugopal_page-0001.jpg','MSc Zoology, MEd','ZOOLOGY'),(22,'NARAYANAN M P','Visiting Faculty','photos/MP_Narayanan_page-0001.jpg','MSc Physics','PHYSICS'),(23,'ABDULLAKKUTTY V P','Visiting Faculty','photos/IMG-20240108-WA0017.jpg','MSc Physics, M Phil','PHYSICS'),(24,'THOMAS M C','Visiting Faculty','photos/M.C_Thomas_page-0001.jpg','MSc Physics','PHYSICS'),(25,'Dr. RAMACHANDRAN M N','Visiting Faculty','photos/Ramachandran_M.N_page-0001.jpg','MSc Physics , M Phil','PHYSICS'),(26,'ATHIRA V','Assistant Professor','photos/Athira_V_page-0001.jpg','MSc Physics, BEd,SET','PHYSICS'),(27,'GRIPHY BALAN B','Assistant Professor','photos/Griphy_Balan_page-0001.jpg','MSc Physics , BEd, SET','PHYSICS'),(28,'KAVYA C K','Assistant Professor','photos/Kavya_C_K_page-0001.jpg','MSc Physics, BEd','PHYSICS'),(29,'ANUSREE','Assistant Professor','photos/Anusree_k_page-0001.jpg','MSc Physics','PHYSICS'),(30,'SATHIAN M V','Visiting Faculty','photos/IMG_20231113_113643.jpg','MSc Mathematics, M Phil','MATHEMATICS'),(31,'NISHA E','Assistant Professor','photos/IMG_20231113_112038.jpg','MSc Mathematics, BEd','MATHEMATICS'),(32,'REJU P','Assistant Professor','photos/IMG-20231113-WA0004.jpg','MSc Mathematics, BEd,SET','MATHEMATICS'),(33,'SRUTHI P P','Assistant Professor','photos/IMG_20231113_111200.jpg','MSc Mathematics, BEd, SET','MATHEMATICS'),(34,'SHIJI C P','Assistant Professor','photos/IMG-20240109-WA0031.jpg','MSc Mathematics, BEd, SET','MATHEMATICS'),(35,'ARYA RAMESH','Assistant Professor','photos/IMG_20231113_100927.jpg','MSc Mathematics','MATHEMATICS'),(36,'TEENA N','Assistant Professor','photos/Teena_shyjesh.jpg','MSc Statistics','STATISTICS'),(37,'ANSI RAJAN','Assistant Professor','photos/IMG-20231113-WA0007.jpg','MSc Statistics, BEd','STATISTICS'),(38,'ANUTHRA S','Assistant Professor','photos/IMG-20231113-WA0010.jpg','MSc Statistics','STATISTICS'),(39,'P V RAVEENDRAN','Visiting Faculty','photos/img1.jpg','MSc Chemistry','CHEMISTRY'),(40,'Dr. PRADEEP KUMAR','Assistant Professor','photos/img16.jpg','MSc Chemistry, PhD','CHEMISTRY'),(41,'ROJA P','Head Of Department','photos/img28.jpg','MSc Chemistry','CHEMISTRY'),(42,'HARSHITHA RAJ P K','Assistant Professor','photos/img22.jpg','MSc Chemistry,BEd','CHEMISTRY'),(43,'THEERTHA SASEENDRAN','Assistant Professor','photos/img10.jpg','MSc Chemistry','CHEMISTRY'),(44,'AMRUTHA RAJ','Assistant Professor','photos/img25.jpg','MSc Chemistry, MEd','CHEMISTRY'),(45,'SRUTHI P','Assistant Professor','photos/img19.jpg','MSc Chemistry','CHEMISTRY'),(46,'JASEELA M K','Assistant Professor','photos/img13.jpg','MSc Chemistry, MEd','CHEMISTRY'),(47,'JILNA P P','Assistant Professor','photos/img6.jpg','MSc Chemistry','CHEMISTRY'),(48,'Dr. K VENUGOPALAN','Visiting Faculty','photos/Dr._K._Venugopalan.jpg','M.Com, PhD','COMMERCE & MANAGEMENT STUDIES'),(49,'Dr. ABDUL ASSIS KOROTH','Visiting Faculty','photos/Dr._Abdul_Assis_Koroth.jpg','M.Com, PhD','COMMERCE & MANAGEMENT STUDIES'),(50,'Dr. UDAYAKUMAR O K','Visiting Faculty','photos/Dr._Udayakumar_OK.jpg','M.Com, PhD','COMMERCE & MANAGEMENT STUDIES'),(51,'O P ARAVINDAN','Assistant Professor','photos/O.P._ARAVINDAN.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(52,'Dr.LALITHA DEVI','Head Of Department','photos/Dr._Lalitha_Devi._T.JPG','M.Com, M Phil, MBA, PGDCA, PhD, NET','MANAGEMENT STUDIES'),(53,'DHANYA A K','Assistant Professor','photos/DHANYA.A.K.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(54,'SUKUMARAN E','Assistant Professor','photos/SUKUMARAN._E.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(55,'SHIKHA N P','Assistant Professor','photos/SIKHA.NP.jpg','M.Com, SET','COMMERCE & MANAGEMENT STUDIES'),(56,'ATHUL V','Head Of Department','photos/ATHUL._V.jpg','M.Com, NET','COMMERCE & MANAGEMENT STUDIES'),(57,'SRUTHI ANANDAN','Assistant Professor','photos/SRUTHI_ANANDAN._K._K.jpg','M.Com, SET','COMMERCE & MANAGEMENT STUDIES'),(58,'RAJITH M','Assistant Professor','photos/WhatsApp_Image_2024-05-21_at_5.02.12_PM.jpeg','M.Com, NET','COMMERCE & MANAGEMENT STUDIES'),(59,'NIMITHA T','Assistant Professor','photos/NIMITHA_T.jpg','MBA, NET','MANAGEMENT STUDIES'),(60,'RAJINA P P','Assistant Professor','photos/RAJINA_P_P.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(61,'AMITH M A','Assistant Professor','photos/AMITH_MA.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(62,'DIVYA SUBHASH','Assistant Professor','photos/DIVYA_SUBHASH_1.jpg','M.Com','COMMERCE & MANAGEMENT STUDIES'),(63,'SNEHA','Assistant Professor','photos/SNEHA._K_1.jpg','M.Com, NET','COMMERCE & MANAGEMENT STUDIES'),(64,'BAGITHA','Assistant Professor','photos/BAGITHA._K.jpg','M.Com, MBA, SET, NET','MANAGEMENT STUDIES'),(65,'RESHMA','Assistant Professor','photos/IMG-20240109-WA0037.jpg','MBA','MANAGEMENT STUDIES'),(66,'AdV. RAMESH BABU','Assistant Professor','photos/Advocate_Ramesh_Babu.jpg','M.Com, LLB','COMMERCE & MANAGEMENT STUDIES'),(67,'P T JOSE','Visiting Faculty','photos/WhatsApp_Image_2024-01-09_at_10.14.30_PM.jpeg','MSc Botany','BOTANY'),(68,'Dr. VINJUSHA N','Assistant Professor','photos/WhatsApp_Image_2024-01-09_at_10.15.19_PM.jpeg','MSc Botany, NET,PhD','BOTANY'),(69,'SRUTHI K T K','Assistant Professor','photos/WhatsApp_Image_2024-01-09_at_10.15.10_PM.jpeg','MSc Botany, GATE, NET','BOTANY'),(70,'SREENANDANA R','Assistant Professor','photos/WhatsApp_Image_2024-01-09_at_10.30.36_PM.jpeg','MSc Botany','BOTANY'),(71,'SUDHIR KUMAR T','Visiting Faculty','photos/S.jpeg','MA English','ENGLISH'),(72,'ACHUTHANANDAN','Visiting Faculty','photos/NULL_IMG.jpg','MJMC','ENGLISH'),(73,'RAGISHA','Assistant Professor','photos/Ragisha.jpg','MA English, BEd, SET, NET','ENGLISH'),(74,'SUJATHA A K','Assistant Professor','photos/Adobe_Scan_21-Nov-2023_page-0001.jpg','MA English , BEd','ENGLISH'),(75,'NIKHIL B S','Assistant Professor','photos/NULL_IMG_HMV57Kl.jpg','MA English, BEd, SET','ENGLISH'),(76,'SAVITHA M P','Assistant Professor','photos/WhatsApp_Image_2024-01-09_at_10.49.36_PM.jpeg','MA English, BEd, SET, NET','ENGLISH'),(77,'JENNY O M','Assistant Professor','photos/WhatsApp_Image_2024-01-10_at_1.16.05_PM.jpeg','MA English , BEd, SET','ENGLISH'),(78,'RISHIBA B','Assistant Professor','photos/WhatsApp_Image_2024-01-10_at_1.06.05_PM.jpeg','MA English, BEd, SET','ENGLISH'),(79,'RINSY HARITHA','Assistant Professor','photos/WhatsApp_Image_2024-01-10_at_7.00.19_PM.jpeg','MA English, BEd, SET,NET','ENGLISH'),(80,'RINITHA C T','Assistant Professor','photos/Photo.jpg','MA English','ENGLISH'),(81,'VARSHA M K','Assistant Professor','photos/IMG-20230415-WA00321.jpg','MA English','ENGLISH'),(82,'DHANYA D','Assistant Professor','photos/WhatsApp_Image_2024-01-10_at_3.31.39_PM.jpeg','MA English, BEd, SET','ENGLISH'),(83,'SREYA P K','Assistant Professor','photos/20240110_153940.jpg','MA English, BEd,SET','ENGLISH'),(84,'JIPSI RANI','Head Of Department','photos/WhatsApp_Image_2024-01-09_at_10.17.12_PM_1.jpeg','MA Hindi','HINDI'),(85,'LIBINA T M','Head Of Department','photos/WhatsApp_Image_2024-01-09_at_10.16.50_PM_3.jpeg','MA Malayalam, BEd, M Phil','MALAYALAM'),(86,'DIVYA P B','Assistant Professor','photos/WhatsApp_Image_2024-01-09_at_10.16.50_PM_2.jpeg','MA Malayalam, BEd','MALAYALAM');
/*!40000 ALTER TABLE `myapp_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_event`
--

DROP TABLE IF EXISTS `myapp_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `description` longtext NOT NULL,
  `venue` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_event`
--

LOCK TABLES `myapp_event` WRITE;
/*!40000 ALTER TABLE `myapp_event` DISABLE KEYS */;
INSERT INTO `myapp_event` VALUES (2,'WEBSITE LAUNCHING CEREMONY','10:00:00.000000','2024-01-18','College website Inauguration Ceremony','Seminar Hall',''),(3,'\" S. U. R\" | Magazine Release | ','11:00:00.000000','2024-01-19','Presented by Hanna Mehthar ( Writer, Traveller, Social Media Influencer)','Seminar Hall',''),(4,'ENVISION 2024 - Seminar Series conducted by IQAC','10:00:00.000000','2024-01-22','Seminar Series','Seminar Hall',''),(5,'Seminar Series 1 - COMPUTATIONAL PHYSICS','10:00:00.000000','2024-01-22','One day seminar on Computational Physics hosted by Dr. Suneera T P(Associate Professor, Govt. College Madappally Vatakara) conducted by Department of Physics .','Seminar Hall',''),(6,'Seminar Series 2- CYBER SECURITY & ETHICAL HACKING','01:30:00.000000','2024-01-22','One day seminar on CYBER SECURITY & ETHICAL HACKING hosted by Sri. Dhanoop Raveendran (Associate Member, National Cyber Security Standards) conducted by Department of Computer Science.','Seminar Hall',''),(7,'Blood Donation Camp','10:00:00.000000','2024-01-24','Blood Donation camp organized by Campuses of Kozhikode and MVR Cancer center.\r\nInaugural Session Handled by College Principal, Dr. M K Radhakrishnan','Class Room Number :206',''),(8,'Mock Parliament ','10:30:00.000000','2024-01-29','Conducting Mock Parliament by Sree Narayana College CoK Members','Class Room 206',''),(9,'SN കലോത്സവം \'24- Off Stage','10:00:00.000000','2024-02-05','Off stage മത്സരങ്ങൾ Feb 5,6,7','College Campus',''),(10,'SN കലോത്സവം \'24 On Stage','10:00:00.000000','2024-02-08','SN Colorful on stage കലോത്സവം - On Stage competition : Feb 8&9','College Campus',''),(11,'Orientation Programme - 4 Year UG','14:45:00.000000','2024-02-07','Orientation programme on four year UG programme- curriculum framework by Dr. Aravindan Tharemmal, Coordinator IQAC SNC','Seminar Hall',''),(13,'Shuttle Badminton Championship ','15:30:00.000000','2024-02-23','Shuttle Badminton Championship\r\nInauguration : M K Radhakrishnan (College Principal )\r\nConducted by Department of Physical Education.','College  Campus ',''),(14,'NATIONAL SCIENCE DAY PROGRAMME 2024','11:00:00.000000','2024-02-28','Programmes\r\n\r\n1.Poster Making Competition\r\n2. Science Fiction story writing\r\n3. Science Quiz Competition\r\n','Seminar Hall',''),(15,'Zero Waste Ptogramme','15:00:00.000000','2024-02-29','Waste Bin distribution Programme conducted by PTA, CoK, NSS, WDC and Bhoomithra Sena Sree Narayana College Vatakara.\r\nInauguration : Smt. M Jayaprabha ( 4th Ward Member Maniyur Panchayat)','College Campus',''),(16,'ഓർമ്മക്കുറിപ്പ് - Mega Alumni Meet','10:00:00.000000','2024-03-30','\"ഓർമ്മക്കുറിപ്പ് \"\r\nMega Alumni വരുന്ന ശനിയാഴ്ച (30/03/24) നടക്കുകയാണ്‌.\r\nപഴയകാല പ്രിസിപ്പൽ മാരും, അധ്യാപകരും,അനദ്ധ്യാപകരും വിദ്യാർത്ഥികളും പങ്കെടുക്കുന്ന മെഗാ ഇവന്റ്.','College Campus',''),(17,'FYUGP - ORIENTATION PROGRAMME PHASE II','10:00:00.000000','2024-05-20','Orientation talk programme about FYUGP conducted by Sree Narayana College by Academic Co-ordinator Dr.Aravindan Tharemmal','College Seminar Hall',''),(18,'ഏകദിന ശില്പശാല  -4 വർഷ ബിരുദം: ഘടനയും , സവിശേഷതകളും സംശയ നിവാരണവും\"','10:00:00.000000','2024-05-31','മാന്യരെ,\r\n\r\nകാലിക്കറ്റ്‌ സർവകലാശാല ഉൾപ്പെടെ\r\n കേരളത്തിലെ എല്ലാ ഉന്നതവിദ്യാഭ്യാസ \r\nമേഖലകളിലും നാല് വർഷ ഡിഗ്രി പഠനം\r\n നിലവിൽ വന്ന സാഹചര്യത്തിൽ \r\nവിദ്യാർത്ഥികൾക്കും, രക്ഷിതാക്കൾക്കും,\r\nപൊതുജനങ്ങൾക്കും വേണ്ടി ശ്രീ നാരായണ കോളേജും മാനേജ്മെന്റും \r\n ചേർന്ന് ഒരുക്കുന്ന ഏകദിന ശില്പശാലയിൽ\r\nഏവരെയും ക്ഷണിക്കുന്നു.\r\n\r\nആമുഖ ഭാഷണം : ഡോ. അരവിന്ദൻ തരേമ്മൻ\r\nഅക്കാഡമിക് കോ- കോർഡിനേറ്റർ \r\nവിഷയ അവതാരകൻ : ഡോ. കെ ജെ വർഗീസ്\r\n(Dean of International affairs & Associate Professor, \r\nChrist College, Irinjalakkuda)','Town Hall Vatakara',''),(19,'State Level FYUGP Orientation Programme Through Online','02:00:00.000000','2024-06-28','State Level FYUGP (First Year Undergraduate Guidance Program) Orientation Program is conducted by Kerala state government through online.','Seminar Hall',''),(20,'വിജ്ഞാനോത്സവം- FYUGP 2024','10:00:00.000000','2024-07-01','വിജ്ഞാനോത്സവം- FYUGP 2024 programme conducted by Kerala state Government.\r\nState Level Inauguration : Honorable Chief Minister Sri. PINARAYI VIJAYAN\r\nCollege Level Inauguration : Sri. T ASHRAF (Maniyur Gramapanchayat President)','Seminar Hall',''),(21,'Inaugural Ceremony - Sree Narayana College General Library & Language Block','09:30:00.000000','2024-08-08','Inauguration ceremony of our new block - General Library & Language Block\r\nInauguration : Sri P M Raveendran\r\n  Manager, Sree Narayana college Vatakara & President,SNDP Union Vatakara','Block C- Sree Narayana College Campus ','');
/*!40000 ALTER TABLE `myapp_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_news`
--

DROP TABLE IF EXISTS `myapp_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_news` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_news`
--

LOCK TABLES `myapp_news` WRITE;
/*!40000 ALTER TABLE `myapp_news` DISABLE KEYS */;
INSERT INTO `myapp_news` VALUES (4,'NAAC - WORKSHOP 1','\" NAAC \", an Overview of Revised Accreditation Guidelines.\r\nRecourse Person : Dr. M P Rajan (Member Co-Ordinator & Observer, NAAC, Bangalore )\r\nConducted on 5th December 2023 , 09.30AM to 04.30PM at College Seminar Hall.\r\nOrganized by IQAC, Sree Narayana College Vatakara. ','2023-12-06',''),(5,'Seminar Presentation - Gender Equality Awareness','Conducted seminar on \"Gender Equality Awareness \" , organized by Sree Narayana college Vatakara and Block Panchayath ICDS\r\n\r\nResource Person : Abdul Gafoor(ORC Project Assistant , District Child Protection Unit, Kozhikode ).\r\nHeld On : 21st August 2023 at College Seminar Hall ','2023-08-21',''),(6,'Voice of New Generation','Public Speaking contest organized  by Senior Chamber International Badagara Legion, conducted on 21st November 2023 at Sree Narayana  College seminar hall ','2023-11-22',''),(7,'College Co-Operative store Inaugurated','Sree Narayana College Co-operative store inaugurated on 6th October 2023 by  Sri. Shiju T (Assistant Registrar, General)','2023-10-07',''),(8,'\" വേണം,  നമുക്കുമൊരു സിലിക്കൺ വാലി ❗\"','Sree Narayana College participated 1 day workshop based on Edu-Tech Conclave conducted by Talrop and Reporter TV on 18th November 2023, at The Raviz Kadav, Azhinjilam, Kozhikode.','2024-01-11',''),(9,'NSS Camp 2023','NSS Seven Days Residential Camp of Sree Narayana College Vatakara was conducted at Govt. LP School Chuzhali from 2023 December 23 to 29. The main Project of the Camp was the roads which remains in poor miserable conditions was repaired amd made suitable for transport and the sub project was campus cleaning of Chuzhali Govt. LP School.\r\n The theme of the camp was \'Malinya Vimuktha Nalekkayi Yuvakeralam\'. The Support of the people of chuzhali village during the camp was incredible.','2024-01-01',''),(10,'\"WEBSITE\" Launched ','വടകര : ശ്രീ നാരായണ കോളേജ് വടകരയിൽ വിവര സാങ്കേതിക വിദ്യയുടെ ഭാഗമായി സൈബർ സെക്യൂരിറ്റി യെ കുറിച്ചുള്ള ബോധവൽക്കരണ ക്ലാസും നവീകരിച്ച കോളേജ് വെബ്സൈറ്റും കണ്ണൂർ യൂണിവേഴ്സിറ്റി ലെ ക്വാണ്ടം കമ്പ്യൂട്ടിങ്ങ് ഡയറക്ടർ ഡോ. ആർ കെ സുനിൽ കുമാർ നിർവഹിച്ചു. ചടങ്ങിൽ ഡോ. എം കെ രാധാകൃഷ്ണൻ,\r\nഎം പി നാരായണൻ, ജയരാജൻ ബി സി, കെ ടി ഹരിമോഹൻ, കാവ്യ വേണു എന്നിവർ സംസാരിക്കുകയും അഭിരാം കൃഷ്ണ, ശരൺ ദാസ് പി എം പങ്കെടുക്കുകയും ചെയ്തു.','2024-01-19',''),(11,'ENVISION - Seminar Series','ENVISION 2024- Seminar series had inaugurated President,Maniyur Panchayat Sri. Asharaf T K on 22/01/2024  Conducted by IQAC & sponsored by PTA Sree Narayana College Vatakara. ','2024-01-22',''),(12,'കോളേജ് മാഗസിൻ \"S.U.R\" പ്രകാശനം ചെയ്തു ','2022 -23  അദ്ധ്യയന വർഷത്തെ കോളേജ് മാഗസിൻ യുവ എഴുത്തുകാരിയും സഞ്ചാരിയുമായ ഹന്ന മെഹ്തർ പ്രകാശനം ചെയ്തു.\r\nകോളേജ് സെമിനാർ ഹാളിൽ പ്രിൻസിപ്പാൾ ഡോ. എം. കെ. രാധാകൃഷ്ണന്റെ അധ്യക്ഷതയിൽ നടന്ന ചടങ്ങിന് സ്റ്റാഫ് എഡിറ്റർ അസി. പ്രൊഫ സച്ചിൻ എസ്. എൽ സ്വാഗതം പറഞ്ഞു. പ്രൊഫ. എം. പി നാരായണൻ, ഡോ.വേണുഗോപാൽ, പ്രൊഫ. സുധീർ കുമാർ, കെ. ടി ഹരിമോഹൻ, ബി. സി ജയരാജൻ, അഭിരാം കൃഷ്ണ, സോനു എന്നിവർ ആശംസകൾ നേർന്ന് സംസാരിച്ചു. മുഖ്യാതിഥിയുമായുള്ള interaction session-ന് ശേഷം സ്റ്റുഡന്റ് എഡിറ്റർ ഗോകുൽ. സി-യുടെ നന്ദി പ്രകാശനത്തോട് കൂടി ചടങ്ങ് അവസാനിച്ചു. .','2024-01-19',''),(13,'വടകര ശ്രീ നാരായണ കോളേജിൽ ആദ്യ സെമിനാർ പരമ്പര അവസാനിച്ചു.','നൂതനവും വൈവിദ്ധ്യമാർന്നതും പരിസ്തിതി സൗഹൃദവുമാക്കി നടത്തുന്ന സെമിനാർ / ശില്പശാല \' എൻവിഷൻ 2024\' തുടക്കം കുറിച്ചു. ഉന്നത വിദ്യാഭ്യാസ സ്ഥാപനങ്ങളുടെ മികവ് നിണ്ണയിക്കുന്ന ഏജൻസിയായ നാക്  (NAAC) അക്രിഡിറ്റേഷൻ അനുബന്ധ പ്രവർത്തനങ്ങളുടെ ഭാഗമായി IQAC (ഇൻറ്റേണൽ ക്വാളിറ്റി അഷ്വറൻസ് സെൽ) യുടെ ആഭിമുഖ്യത്തിൽ നടത്തുന്ന സെമിനാർ / ശില്പശാല \"എൻവിഷൻ  2024 \" ൻ്റെ ഔപചാരിക ഉദ്ഘാടനം 2024 ജനവരി 22 ന് മണിയൂർ ഗ്രാമ പഞ്ചായത്ത് പ്രസിഡണ്ട് ശ്രീ. അഷറഫ് ടി. കെ. നിർവ്വഹിച്ചു. ജ്ഞാന വിനിമയത്തിലൂടെ വിജ്ഞാന സന്മാദനം സാധ്യമാകണമെന്നും, ശ്രീ നാരായണ ഗുരുവിൻ്റെ ദർശനം ഇതിന് മുതൽ കൂട്ടാവുമെന്നും അദ്ദേഹ പറഞ്ഞു.\r\nഡോ. എം.കെ. രാധാകൃഷ്ണൻ, പ്രിൻസിപ്പാൾ, അദ്ധ്യക്ഷത വഹിച്ചു. ശ്രീ സി. വിനോദ് കുമാർ, പി.ടി.എ. വൈസ് പ്രസിഡൻ്റ് , പ്രൊഫസർ നാരായണൻ എം.പി, ഫിസ്ക്സ് ഡിപാർട്ട്മെൻ്റ് മോധവി, ശ്രീ ആദർഷ്, സെക്രട്ടറി,  സ്റ്റുഡൻസ് യൂണിയൻ എന്നിവർ ആശംസാ പ്രസംഗം നടത്തി. \r\nഡോ. അരവിന്ദൻ താരേമ്മൽ IQAC കോഓർഡിനേറ്റർ സ്വഗത ഭാഷണവും, ശ്രീ രജിത്ത് എം നന്ദി പ്രകാശനവും നടത്തി.\r\nതുടർന്നു കംപ്യൂട്ടർ ഫിസിക്സിൻ്റെ അനന്ത സാധ്യതകളെ കുറിച്ച് ഡോ. സുനീറ ടി.വി., അസ്സോസിയേറ്റ് പ്രഫസർ, ഗവ. കോളേജ്\' മടപ്പള്ളി യുടെ പ്രഭാഷണവും ശ്രീ ധനുഷ് രവീന്ദ്രൻ, അസ്സോസിയേറ്റ് മെമ്പർ, സൈബർ സെക്യരിറ്റി സ്റ്റാൻഡേഡ് സ് , സൈമ്പർ സെക്യൂരിറ്റി - എത്തിക്കൽ ഫാക്കിങ്ങിനെ കുറിച്ച് വിശകലനവും നടത്തി.\r\nസെമിനാർ/ വർക്ക്ഷോപ്പ് 29.01.2924 വരെ തുടരുന്നതാണ്.','2024-01-30',''),(14,'\"Mock Parliament\" ','The mock parliament programme was conducted by Sree Narayana College Campuses of Kozhikode Unit. ','2024-01-29',''),(15,'SN കലോത്സവം \'24 - Merit Day','SN കലോത്സവം \'24 ന്റെ ആദ്യ ദിനത്തിൽ ഉദ്ഘാടന ചടങ്ങ് പ്രശസ്ത ഗാനരചയിതാവ്      ശ്രീ. വി ടി മുരളി നിർവഹിച്ചു. പ്രസ്തുത ചടങ്ങിൽ കഴിഞ്ഞ വർഷത്തെ കാലിക്കറ്റ്‌ യൂണിവേഴ്സിറ്റി ടോപ്പർ സ്റ്റുഡൻസിനുള്ള അനുമോദന ചടങ്ങായ മേരിറ്റ്ആ ഡേ കോളേജും PTA യും ചേർന്ന് നടത്തി.  ','2024-02-10',''),(16,'SN കലോത്സവം \'24.. \'ഒച്ച\'  - Winners : SCIENCE Department ','5 ദിവസങ്ങളിൽ ആയി ഇഞ്ചോടിഞ്ചു പോരാട്ടം നടന്ന    കോളേജ് കലോത്സവത്തിന് തിരശീല വീണു. സമാപന ദിവസത്തിൽ ഏറ്റവും കൂടുതൽ പോയിന്റോടു കൂടി സയൻസ് ഡിപ്പാർട്മെന്റ് ഒന്നാം സ്ഥാനം കരസ്തമാക്കിയപ്പോൾ തൊട്ടു പുറകിൽ ആയി രണ്ടാം സ്ഥാനത്തു സൈക്കോളജി ഡിപ്പാർട്മെന്റും മൂന്നാം സ്ഥാനത്തു ഇംഗ്ലീഷ് ഡിപ്പാർട്മെന്റും നാലാം സ്ഥാനത്തു കമ്പ്യൂട്ടർ സയൻസ് ഡിപ്പാർട്മെന്റും ഇടം പിടിച്ചു. വിജയികളെ സമാപന സമ്മേളനത്തിൽ കോളേജ് പ്രിൻസിപ്പൽ, അധ്യാപകർ, അനദ്ധ്യാപകർ,കോളേജ് യൂണിയൻ കമ്മിറ്റി ഭാരവാഹികൾ തുടങ്ങിയവർ അനുമോദിച്ചു.','2024-02-10',''),(18,'Convocation Ceremony : Department of Psychology ','Convocation Ceremony of 2021-23 PG students had conducted by Department of Psychology.','2023-10-25',''),(19,'Shuttle Badminton Championship ','Shuttle Badminton Championship inaugurated by College Principal Dr. M K Radhakrishnan & conducted by Department of Physical Education on 23rd February 2024 at college campus.','2024-02-23',''),(20,'\"ഓർമക്കുറിപ്പ് \"-24','പൂർവാധ്യാപക-വിദ്യാർത്ഥി സംഗമവു० അധ്യാപകരെ ആദരിക്കൽ ചടങ്ങു० നടത്തി.\r\n\r\nവടകര:കീഴൽ ശ്രീനാരായണ കോളേജ് പൂർവവിദ്യാർത്ഥി സംഗമവും പൂർവാധ്യാപകരെ ആദരിക്കലും സംഘടിപിച്ചു.കോളേജ് ആര०ഭിച്ച വർഷ० മുതൽ(2003) പഠിച്ചിറങ്ങിയ വിദ്യാർത്ഥികളും അധ്യാപകരു० ചടങ്ങിൽ പങ്കെടുത്തു. കോളേജ് പ്രിൻസിപ്പൾ ഡോ: എം.കെ രാധാകൃഷ്ണൻ അധ്യക്ഷത വഹിച്ച ചടങ്ങിൽ ശ്രീ നാരായണ കോളേജ് മാനേജർ ശ്രീ പി. എം. രവീന്ദ്രൻ ഉദ്ഘാടനം നിർവഹിച്ചു. ഫ്ളവേഴ്സ് ചാനൽ സംഗീത പരിപാടിയിൽ (മ്യൂസിക്കൽ വൈഫ്)ജേതാവായ ആതിര വിജിത്തിന്റെ  നേതൃത്വത്തിൽ ഗാനമേള അവതരിപ്പിച്ചു. ചടങ്ങിന്റെ ഭാഗമായി അലൂമിനി അസ്സോസിയേഷൻ രൂപീകരിക്കുകയു० എക്സിക്യുട്ടീവ് അ०ഗങ്ങളെ തിരഞ്ഞെടുക്കുകയു० ചെയ്തു.ഭാരവാഹികൾ: ഡോ.എ०.കെ രാധാകൃഷ്ണൻ(പ്രസിഡൻ്റ്),തുഷാർ.വി.കപാഡിയ(വൈസ് പ്രസിഡൻ്റ്),ആകാശ്(സെക്രട്ടറി),കൃഷ്ണേന്ദു.ബി.എസ്(ജോയ്ന്റ് സെക്രട്ടറി),സുരഭി.എസ്.ആർ(ട്രഷറർ).പ്രിൻസിപ്പൾ, മുൻ പ്രിൻസിപ്പൾമാർ,പ്രൊഫസർമാർ തുടങ്ങിയവർ ചടങ്ങിൽ സ०സാരിച്ചു.','2024-03-30',''),(21,'ആധുനിക സൗകര്യങ്ങളോട് കൂടിയുള്ള പുതിയ ബസ്സ് സർവീസ് തുടങ്ങി. ','വടകര ശ്രീനാരായണ കോളേജിൽ വിദ്യാർത്ഥികൾക്കും ജീവനക്കാർക്കും വേണ്ടി SNDP യൂണിയൻ ആധുനിക സൗകര്യങ്ങളോട് കൂടിയുള്ള പുതിയ ബസ്സ് സർവീസ് തുടങ്ങി. ഇതിന്റെ താക്കോൽ ദാന ചടങ്ങ് കോളേജ് പ്രിൻസിപ്പൽ നിർവഹിച്ചു. ചടങ്ങിൽ SNDP വടകര യൂണിയൻ വൈസ് പ്രസിഡന്റ്‌ ശ്രീ. ഹരിമോഹൻ, ഓഫീസ് സുപ്രന്റ് ശ്രീ. ജയരാജൻ എന്നിവർ സംബന്ധിച്ചു.','2024-04-17',''),(22,'Sree Narayana College - AICTE Approved ','വടകര ശ്രീനാരായണ കോളേജിന് ഉജ്ജ്വല നേട്ടം.\r\n\r\nവടകരയിൽ ആദ്യമായി ശ്രീനാരായണ കോളേജിന് AICTE അംഗീകാരം ലഭിച്ചു.\r\n19 കോഴ്സുകളോടു കൂടി നിലവിൽ ശ്രീ നാരായണ കോളേജ് All India Council for Technical Education ന്റെ ഭാഗമായി പ്രവർത്തനം തുടരുന്നു.ഇതോടുകൂടി  കാലിക്കറ്റ്‌ യൂണിവേഴ്സിറ്റി യുടെ അഫിലിയേഷനോടൊപ്പം AICTE അംഗീകാരം കൂടി ലഭിച്ച വടകരയിലെ ആദ്യത്തെ വിദ്യാഭ്യാസ സ്ഥാപനമായി മാറിയിക്കുകയാണ് ശ്രീ നാരായണ കോളേജ്.','2024-05-10',''),(23,'FYUGP - Orientation Talk നടത്തി','ശ്രീ നാരായണ കോളേജിൽ നാല് വർഷ ഡിഗ്രി പഠനത്തിന്റെ ഭാഗമായി ഓറിയന്റേഷൻ ക്ലാസ്സ്‌ സംഘടിപ്പിച്ചു. അക്കാഡമിക് കോർഡിനേറ്റർ ഡോ. അരവിന്ദൻ തറേമ്മൽ ക്ലാസുകൾ കൈകാര്യം ചെയ്തു. പ്രസ്തുത മീറ്റിംഗിൽ പ്രിൻസിപ്പൽ ഡോ. M K രാധാകൃഷ്ണൻ, അധ്യാപകർ, അനദ്ധ്യാപകർ എന്നിവർ പങ്കെടുത്തു.','2024-05-20',''),(24,'FYUGP -Our Major & Minor Courses','We offered the 13 Major Disciplines under Calicut University.','2024-05-23',''),(25,'ശില്പശാല നടത്തി','ശ്രീ നാരായണ കോളേജിന്റെ ആഭിമുഖ്യത്തിൽ \r\n\"നാല് വർഷ ബിരുദം : ഘടനയും സവിശേഷതകളും സംശയ നിവാരണവും \" എന്ന വിഷയത്തിൽ ശില്പശാല നടത്തി.\r\n\r\nഡോ. കെ ജെ വർഗീസ് ( Dean of International affairs & Associate Professor, Christ College, Irinjalakkuda)  വിഷയം അവതരിപ്പിച്ച ചടങ്ങിൽ പ്രൊ. എം പി നാരായണൻ സ്വാഗതവും ഡോ. എം കെ രാധാകൃഷ്ണൻ(പ്രിൻസിപ്പാൾ )അദ്ധ്യക്ഷനും  സി മനോജ്‌ കുമാർ (DDE Calicut)ഉദ്ഘാടനവും ഡോ. അരവിന്ദൻ തരേമ്മൽ ആമുഖ ഭാഷണവും നിർവഹിച്ചു. ചടങ്ങിൽ വടകര SNDP യൂണിയൻ പ്രസിഡന്റ്‌ എം എം ദാമോദരൻ, വൈസ് പ്രസിഡന്റ്‌ കെ ടി ഹരിമോഹൻ എന്നിവർ സംസാരിച്ചു.','2024-05-31',''),(26,'\"ചേർത്ത് നിർത്താം പ്രകൃതിയെ നല്ലൊരു നാളെയ്ക്കുവേണ്ടി \"','ജൂൺ 5 പരിസ്ഥിതിദിനത്തോടനുബന്ധിച്ചു എൻ എസ് എസ്  വോളന്റീർസ് കോളേജ്  അംഗണത്തിൽ വൃക്ഷതൈകൾ നട്ടുപിടിപ്പിച്ചു.','2024-06-05',''),(27,'State Level FYUGP Orientation Program','the State Level FYUGP (First Year Undergraduate Guidance Program) Orientation Program is an excellent initiative to support faculties transitioning to hiher their teaching level ince it\'s happening online at Sree Narayana College','2024-06-29',''),(28,'വിജ്ഞാനോത്സവം- FYUGP 2024','കേരള സർക്കാരിന്റെ FYUGP വിജ്ഞാനോത്സവം പരിപാടി ബഹു. മുഖ്യമന്ത്രി ശ്രീ. പിണറായി വിജയൻ ഉദ്ഘാടനം ചെയ്തു. ഉന്നത വിദ്യാഭ്യാസ മന്ത്രി ഡോ.ആർ ബിന്ദു പങ്കെടുത്തു.കോളേജ് തല ഉദ്ഘാടനം മണിയൂർ പഞ്ചായത്ത്‌ പ്രസിഡന്റ്‌ ടി അഷറഫ് നിർവഹിച്ചു. ചടങ്ങിൽ കോളേജ് പ്രിൻസിപ്പാൾ ഡോ. എം കെ രാധാകൃഷ്ണൻ, വൈസ് പ്രിൻസിപ്പാൾ പ്രൊ. എം പി നാരായണൻ, ഡോ കെ വേണുഗോപാൽ, അക്കാഡമിക് കോ-കോർഡിനേറ്റർ ഡോ. അരവിന്ദൻ തരേമ്മൽ,PTA വൈസ് പ്രസിഡന്റ്‌, മാനേജ്മെന്റ് കമ്മിറ്റി അംഗം കെ ടി ഹരിമോഹൻ, കോളജ് യൂണിയൻ ചെയർമാൻ എന്നിവർ സംസാരിച്ചു.','2024-07-01',''),(29,'ജനറൽ ലൈബ്രറി & ലാംഗ്വേജ് ബ്ലോക്ക്‌ ഉദ്ഘാടനം ചെയ്തു.','ശ്രീ നാരായണ കോളേജിൽ പുതുതായി നിർമിച്ച ജനറൽ ലൈബ്രറി & ലാംഗ്വേജ് ബ്ലോക്ക്‌ കോളേജ് മാനേജർ ശ്രീ പി എം രവീന്ദ്രൻ ഉദ്ഘാടനം ചെയ്തു. കോളേജ് പ്രിൻസിപ്പൽ ഡോ. എം കെ രാധാകൃഷ്ണൻ,കെ ടി ഹരിമോഹൻ,ബി സി ജയരാജൻ, ടി സുധീർ കുമാർ, എം പി നാരായണൻ ജയേഷ് വടകര, ദിനേശ് മേപ്പയിൽ, വിനോദൻ, വി കെ കുമാരൻ, രജീഷ്, ശരൺ ദാസ്, മജീദ് എന്നിവർ സംസാരിച്ചു.','2024-08-08',''),(30,'Independence Day Celebration ','ശ്രീ നാരായണ കോളേജിൽ സ്വാതന്ത്ര്യ ദിനം ആഘോഷിച്ചു.','2024-08-15','');
/*!40000 ALTER TABLE `myapp_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_newsimage`
--

DROP TABLE IF EXISTS `myapp_newsimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_newsimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `news_article_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_newsimage_news_article_id_87547bc6_fk_myapp_news_id` (`news_article_id`),
  CONSTRAINT `myapp_newsimage_news_article_id_87547bc6_fk_myapp_news_id` FOREIGN KEY (`news_article_id`) REFERENCES `myapp_news` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_newsimage`
--

LOCK TABLES `myapp_newsimage` WRITE;
/*!40000 ALTER TABLE `myapp_newsimage` DISABLE KEYS */;
INSERT INTO `myapp_newsimage` VALUES (8,'news_images/4ff1859f-33a7-49e3-934f-8dca5e2f8162_G6RYHyi.jpeg',4),(9,'news_images/a1245672-9d02-46f8-851e-00b867b99068_traBEFR.jpeg',4),(10,'news_images/PHOTO-2023-08-19-22-52-51_1.jpg',5),(11,'news_images/7061f7f8-0c9d-4cde-b53c-b2076bdd9934.jpeg',5),(12,'news_images/IMG_9047.jpeg',6),(13,'news_images/WhatsApp_Image_2024-01-09_at_11.10.09_PM_1.jpeg',7),(14,'news_images/WhatsApp_Image_2024-01-10_at_6.59.01_PM.jpeg',8),(15,'news_images/WhatsApp_Image_2024-01-15_at_10.37.17_PM.jpeg',9),(16,'news_images/WhatsApp_Image_2024-01-15_at_10.37.17_PM_3.jpeg',9),(17,'news_images/WhatsApp_Image_2024-01-15_at_10.37.17_PM_2.jpeg',9),(18,'news_images/WhatsApp_Image_2024-01-15_at_10.37.17_PM_1.jpeg',9),(19,'news_images/SAVE_20240119_161734.jpg',10),(20,'news_images/IMG-20240118-WA0093.jpg',10),(21,'news_images/IMG_20240122_173843.jpg',11),(22,'news_images/SUR.jpeg',12),(23,'news_images/front.jpg',12),(24,'news_images/IMG_2197.JPG',13),(25,'news_images/WhatsApp_Image_2024-02-01_at_8.51.31_PM_1.jpeg',14),(26,'news_images/WhatsApp_Image_2024-02-01_at_8.51.31_PM.jpeg',14),(27,'news_images/WhatsApp_Image_2024-02-01_at_8.51.30_PM.jpeg',14),(28,'news_images/IMG-20240210-WA0017.jpg',15),(29,'news_images/IMG-20240210-WA0016.jpg',15),(30,'news_images/IMG-20240209-WA0027.jpg',16),(31,'news_images/IMG-20240210-WA0002.jpg',16),(32,'news_images/IMG-20240210-WA0000.jpg',16),(35,'news_images/IMG-20240223-WA0038_4RXt2Ml.jpg',18),(36,'news_images/IMG-20240223-WA0037_c5aSwWn.jpg',18),(37,'news_images/IMG-20240223-WA0021.jpg',19),(38,'news_images/IMG-20240223-WA0031.jpg',19),(39,'news_images/IMG-20240402-WA0014.jpg',20),(40,'news_images/IMG-20240402-WA0012.jpg',20),(41,'news_images/IMG-20240402-WA0010.jpg',20),(42,'news_images/5093bdac142b4faba9cc606ea521b62a.jpg',21),(43,'news_images/IMG-20240510-WA0000.jpg',22),(44,'news_images/Add_A_HeadingSR_20240523_165609_0000.png',23),(45,'news_images/WhatsApp_Image_2024-05-23_at_5.12.29_PM2.jpeg',23),(46,'news_images/WhatsApp_Image_2024-05-23_at_5.12.29_PM1.jpeg',23),(47,'news_images/WhatsApp_Image_2024-05-23_at_5.12.29_PM.jpeg',23),(48,'news_images/IMG-20240523-WA00361.jpg',24),(49,'news_images/IMG-20240531-WA0037.jpg',25),(50,'news_images/IMG-20240605-WA0078.jpg',26),(51,'news_images/FB_IMG_1717655651812.jpg',25),(52,'news_images/FB_IMG_1717655577326.jpg',25),(53,'news_images/FB_IMG_1717655567857.jpg',25),(54,'news_images/FB_IMG_1717655520505.jpg',25),(55,'news_images/FB_IMG_1717655499424.jpg',25),(56,'news_images/FB_IMG_1717655493670.jpg',25),(57,'news_images/FB_IMG_1717655488534.jpg',25),(58,'news_images/IMG-20240606-WA0010.jpg',26),(59,'news_images/IMG-20240606-WA0008.jpg',26),(60,'news_images/WhatsApp_Image_2024-06-28_at_6.43.21_PM.jpeg',27),(61,'news_images/WhatsApp_Image_2024-06-28_at_6.43.25_PM.jpeg',27),(62,'news_images/WhatsApp_Image_2024-06-28_at_6.43.22_PM.jpeg',27),(63,'news_images/WhatsApp_Image_2024-07-02_at_5.47.02_PM.jpeg',28),(64,'news_images/WhatsApp_Image_2024-07-02_at_5.47.05_PM.jpeg',28),(65,'news_images/WhatsApp_Image_2024-07-02_at_5.47.01_PM.jpeg',28),(66,'news_images/WhatsApp_Image_2024-07-02_at_5.46.18_PM.jpeg',28),(67,'news_images/IMG-20240811-WA0064.jpg',29),(68,'news_images/IMG-20240811-WA0063.jpg',29),(69,'news_images/IMG-20240815-WA0011.jpg',30),(70,'news_images/IMG-20240815-WA0008.jpg',30),(71,'news_images/IMG-20240815-WA0009.jpg',30),(72,'news_images/IMG-20240815-WA0012.jpg',30);
/*!40000 ALTER TABLE `myapp_newsimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_notification`
--

DROP TABLE IF EXISTS `myapp_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_notification`
--

LOCK TABLES `myapp_notification` WRITE;
/*!40000 ALTER TABLE `myapp_notification` DISABLE KEYS */;
INSERT INTO `myapp_notification` VALUES (1,'ug','First Semester UG Examination','It is notified for the information of all concerned that the following First Semester U.G.\r\nExaminations for the candidates of Affiliated Colleges / School of Distance Education / Private\r\nRegistration will be conducted from Monday, 19.02.2024 onwards. Detailed Time Table will\r\nbe available in the Official Website of the University later.\r\n1. First Semester B.A. / B.Com / BBA / B.Sc. and Allied Subjects (CBCSS - UG) Regular /\r\nSupplementary / Improvement Examination November 2023 (2019 to 2023 Admissions)\r\n2 . First Semester B.A. / B.Com. / BBA / B.Sc. and Allied Subjects (CUCBCSS-UG)\r\nSupplementary / Improvement Examination November 2023 (2018 Admission only)','uploads/2023-12-21_11_17_02_exnot7710_1.pdf'),(2,'ug','CALICUT UNIVERSITY 2ND SEMESTER UG CV CAMP ','Calicut University 2nd semester UG centralized valuation camp will be commenced from 29th January 2024 to 2nd February 2024. ',''),(3,'ug','1st Semester UG Examination has been postponed to March 4th 2024','1st Semester UG Examination has been postponed to March 4th 2024','uploads/2024-02-03_16_19_51_exnot7900.pdf'),(4,'ug','Calicut University Student Portal Registration 2023 admission onwards ','          All students who took admission 2023 onwards should register Calicut university Students portal. Registration instruction are attached here.','uploads/STUDENT_PORTAL_REGISTRATION.pdf'),(5,'ug','Fourth Semester Exam Registration ','It is notified for the information of all concerned that the link for Online registration of Fourth\r\nSemester (CBCSS-UG) Regular / Supplementary / Improvement Examination April\r\n2024 (2019 Admission onwards) of B.A. / B.Sc / B.Sc in Alternate pattern / B.Com / BBA / B.A. Multi\r\nMedia / BCA / B.Com Vocational Stream / BSW / BTHM / BHA / B.A. Visual Communication / B.A. Film\r\nand Television / B.A. Afsal Ul-Ulama / BGA, B.Com Honours & B.Com Professional (CUCBCSS-UG) for\r\nthe candidates of Affiliated Colleges and BTA for the candidates of School of Drama and Fine\r\nArts, Dr. John Matthai Centre, Aranattukara, Thrissur, will be available on the University website\r\n(www.uoc.ac.in) from Tuesday, 13\r\nth February 2024 onwards','uploads/2024-02-08_12_44_10_exnot7916.pdf'),(6,'ug','Fourth Semester CBCSS- UG BA Timetable','          Exam Date : 19-06-2024 ONWARDS','uploads/ba.pdf'),(7,'ug','FOURTH SEMESTER CBCSS-UG  BBA TIMETABLE ','EXAM DATE : 19-06-2024 ONWARDS','uploads/bba.pdf'),(8,'ug','FOURTH SEMESTER CBCSS-UG BCOM TIMETABLE','EXAM DATE : 19-06-2024 ONWARDS','uploads/bba_dU0Qu87.pdf'),(9,'ug','FOURTH SEMESTER CBCSS-UG BSC/BCA TIMETABLE','EXAM DATE : 19-06-2024 ONWADS','uploads/fourthbsc.pdf'),(10,'ug','FYUGP Major & Minor Courses','We offered the 13 Major Disciplines under Calicut University','uploads/IMG-20240523-WA00361.jpg');
/*!40000 ALTER TABLE `myapp_notification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13  8:38:54
