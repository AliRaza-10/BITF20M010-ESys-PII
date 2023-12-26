-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: std_interest_sys
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `interest`
--

DROP TABLE IF EXISTS `interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interest` (
  `id` int NOT NULL AUTO_INCREMENT,
  `RollNo` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `Dob` date NOT NULL,
  `City` varchar(255) NOT NULL,
  `Interest` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Degree` varchar(255) NOT NULL,
  `Subject` varchar(255) NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `RollNo` (`RollNo`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest` DISABLE KEYS */;
INSERT INTO `interest` VALUES (54,'BSEF20M021','Abdullah','johnK@gmail.com','Male','2023-12-12','Gojra','Cooking','Computer Science','Diploma','coding','2023-12-05','2023-12-21'),(60,'40','Michael','michael@gmail.com','male','2022-12-05','islamabad','Movies','Information Technology','Master','film','2023-11-30','2023-12-20'),(61,'44','Olivia','olivia@gmail.com','female','2021-12-20','lahore','Coding','Computer Science','Bachelor','programming','2023-12-03','2023-12-19'),(65,'RN001','John Doe','john.doe@example.com','Male','1990-05-15','New York','Traveling','Computer Science','Bachelor','Programming','2022-01-01','2022-05-30'),(66,'RN765','Jane Smith','jane@example.com','Female','1988-08-22','Los Angeles','Reading','English Literature','Bachelor','Classic Literature','2022-02-15','2022-06-15'),(67,'RN003','Michael Johnson','michael.j@example.com','Male','1995-03-10','Chicago','Photography','Fine Arts','Master','Photography','2021-12-01','2022-05-31'),(68,'RN004','Emily Brown','emily.b@example.com','Female','1992-11-05','San Francisco','Cooking','Culinary Arts','Associate','International Cuisine','2022-03-20','2022-07-30'),(69,'RN005','William Davis','william.d@example.com','Male','1987-07-18','Miami','Fitness','Sports Science','Bachelor','Fitness Training','2022-01-10','2022-06-10'),(70,'RN006','Olivia Wilson','olivia.w@example.com','Female','1991-12-02','Seattle','Gaming','Computer Science','Master','Game Development','2022-02-28','2022-08-15'),(71,'RN007','Ethan Taylor','ethan.t@example.com','Male','1989-09-25','Austin','Music','Music Education','Bachelor','Piano','2022-04-05','2022-09-05'),(72,'RN008','Ava Miller','ava.m@example.com','Female','1993-06-08','Denver','Hiking','Environmental Science','Bachelor','Nature Exploration','2022-03-15','2022-08-31'),(73,'RN009','Liam Anderson','liam.a@example.com','Male','1994-04-30','Phoenix','Painting','Fine Arts','Master','Abstract Art','2021-11-20','2022-04-30'),(74,'RN010','Sophia Martinez','sophia.m@example.com','Female','1997-01-12','Dallas','Dancing','Performing Arts','Bachelor','Ballet','2022-01-05','2022-06-05'),(75,'RN011','Noah Wilson','noah.w@example.com','Male','1986-08-05','Houston','Reading','English Literature','Master','Modern Poetry','2022-02-10','2022-07-10'),(76,'RN012','Emma Davis','emma.d@example.com','Female','1996-02-18','San Diego','Cooking','Culinary Arts','Bachelor','Vegetarian Cuisine','2022-04-15','2022-09-15'),(77,'RN013','Alexander Brown','alexander.b@example.com','Male','1998-07-22','Atlanta','Gardening','Botany','Bachelor','Flower Cultivation','2022-01-20','2022-06-20'),(78,'RN014','Madison Taylor','madison.t@example.com','Female','1990-10-08','Boston','Traveling','Geography','Master','World Heritage Sites','2022-02-25','2022-08-25'),(79,'RN015','Mason Hernandez','mason.h@example.com','Male','1985-12-15','Portland','Photography','Fine Arts','Bachelor','Portrait Photography','2022-04-01','2022-09-01'),(80,'RN016','Abigail Lee','abigail.l@example.com','Female','1999-05-28','Minneapolis','Fitness','Sports Science','Bachelor','Yoga','2022-03-12','2022-08-12'),(81,'RN017','Daniel White','daniel.w@example.com','Male','1984-09-10','Philadelphia','Music','Music Composition','Master','Orchestral Composition','2022-01-18','2022-06-18'),(82,'RN018','Chloe Allen','chloe.a@example.com','Female','1992-04-02','Detroit','Hiking','Environmental Science','Bachelor','Mountain Trails','2022-03-28','2022-06-18'),(83,'232','faiz','faiz@gmail.com','male','2020-01-06','Gojra','Dancing','Information Technology','Bachelor','Bio','2021-01-24','2022-05-08'),(84,'2757','zain','zas@gmail.com','male','2022-06-24','lahore','Cooking','Information Technology','Bachelor','Bio','2021-01-24','2022-05-24'),(85,'765','abd','abd@gmail.com','male','2023-12-05','Sahiwal','Coding','Software Engineering','Bachelor','english','2022-06-24','2023-12-27'),(86,'87','shjd','fg@gmail.com','male','2023-12-04','lahore','picnic','Software Engineering','Associate','english','2023-12-10','2023-12-27'),(87,'657','hamza','ham@gmail.com','male','2023-12-04','lahore','Painting','Software Engineering','Bachelor','Bio','2023-12-04','2023-12-19'),(88,'543','hasifa','has@gmail.com','female','2023-11-27','Sahiwal','Music','Computer Science','Associate','Bio','2023-12-03','2023-12-05'),(89,'654','hafiz ahmad','ahmad@gmail.com','male','2023-12-04','islamabad','Coding','Software Engineering','Associate','english','2023-12-10','2023-12-06'),(90,'12345','raza ali','raza@gmail.com','male','2023-12-04','lahore','Painting','Computer Science','Bachelor','science','2021-05-19','2023-12-12'),(92,'BITF20M0100','Shameer','sham@gmail.com','male','2023-12-05','Gujranwala','Politics','Marketing','Master','Artificial Intelligence','2021-01-26','2023-12-12'),(93,'BITF20M0101','Akbar','akbar@gmail.com','male','2023-12-05','Sargodha','Fitness','Computer Science','Associate','Enterprise','2023-12-11','2023-12-22'),(94,'BITF20M0102','Umer Sukhe','um@gmail.com','male','2023-11-28','Gujrat','Photography','Computer Science','Master','Mobile Application','2023-10-31','2023-12-28'),(95,'BITF20M0104','Shahzad','shahzad@gmail.com','male','2023-12-14','Sialkot','Movies','Commerce','Associate','Physics','2023-12-06','2023-12-19');
/*!40000 ALTER TABLE `interest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `username` varchar(255) NOT NULL,
  `password` varchar(45) NOT NULL,
  UNIQUE KEY `email_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('abbas','123'),('abdullah','123'),('ali','123'),('hassan','123');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_activity`
--

DROP TABLE IF EXISTS `user_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `show_count` int DEFAULT NULL,
  `dashboard_count` int DEFAULT NULL,
  `logout_count` int DEFAULT NULL,
  `activity_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `login_count` int DEFAULT '0',
  `submit_count` int DEFAULT NULL,
  `view_count` int DEFAULT NULL,
  `delete_count` int DEFAULT NULL,
  `update_count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_activity`
--

LOCK TABLES `user_activity` WRITE;
/*!40000 ALTER TABLE `user_activity` DISABLE KEYS */;
INSERT INTO `user_activity` VALUES (1,'abbas',3,1,1,'2023-12-23 18:43:50',1,1,0,1,2),(2,'abbas',1,2,1,'2023-12-24 18:43:51',1,2,1,0,1),(3,'hassan',4,2,1,'2023-12-22 18:51:12',1,3,2,1,0),(4,'ali',2,2,1,'2023-12-21 18:52:30',1,2,1,2,1),(5,'abbas',2,1,1,'2023-12-21 19:03:04',1,0,2,1,0),(7,'hassan',1,2,1,'2023-12-19 19:31:12',1,1,2,2,1),(10,'abbas',1,1,1,'2023-12-09 19:42:18',1,1,1,3,2),(11,'abbas',0,0,1,'2023-12-12 19:42:20',1,1,0,0,0),(18,'hassan',1,1,1,'2023-11-24 19:43:24',1,2,1,1,3),(19,'ali',3,4,1,'2023-12-24 19:49:30',1,3,1,1,0),(20,'abdullah',2,2,1,'2023-12-19 20:01:18',1,3,0,2,0),(21,'abbas',1,1,1,'2023-12-24 22:17:51',1,0,0,1,1),(22,'hassan',1,1,1,'2023-12-24 22:20:55',1,1,1,0,2),(23,'ali',1,1,1,'2023-12-20 22:26:24',1,2,1,1,1),(24,'abbas',1,2,1,'2023-12-23 14:04:52',1,1,2,1,1),(25,'abdullah',1,2,1,'2023-12-15 14:11:07',1,2,1,0,3),(26,'john',3,1,1,'2023-12-11 05:15:00',1,1,0,1,2),(27,'jane',1,2,1,'2023-12-13 05:30:00',1,2,1,0,1),(28,'smith',4,2,1,'2023-12-14 06:00:00',1,3,2,1,0),(29,'doe',2,2,1,'2023-12-15 06:30:00',1,2,1,2,1),(30,'mary',2,1,1,'2023-12-20 07:00:00',1,0,2,1,0),(31,'bob',3,1,1,'2023-12-06 07:30:00',1,1,0,1,2),(32,'alice',3,3,1,'2023-12-20 08:00:00',1,2,2,2,2),(33,'charlie',4,2,1,'2023-12-13 08:30:00',1,3,2,1,0),(34,'eve',2,2,1,'2023-12-11 09:00:00',1,2,1,2,1),(35,'alex',2,1,1,'2023-12-12 09:30:00',1,0,2,1,0),(36,'olivia',3,1,1,'2023-12-12 10:00:00',1,1,0,1,2),(37,'liam',1,2,1,'2023-12-13 10:30:00',1,2,1,0,1),(38,'ethan',4,2,1,'2023-12-12 11:00:00',1,3,2,1,0),(39,'ava',2,2,1,'2023-12-11 11:30:00',1,2,1,2,1),(40,'noah',2,1,1,'2023-12-11 12:00:00',1,0,2,1,0),(41,'emma',0,1,1,'2023-12-13 12:30:00',1,1,0,0,0),(42,'william',1,0,1,'2023-12-02 13:00:00',1,2,1,1,0),(43,'sophia',4,2,1,'2023-11-28 13:30:00',1,3,2,2,0),(44,'jack',2,2,1,'2023-11-29 14:00:00',1,2,1,2,1),(45,'oliver',1,1,1,'2023-11-25 14:30:00',1,1,2,1,0),(48,'ali',1,2,1,'2023-12-25 18:56:37',1,2,1,0,2),(49,'abbas',1,0,1,'2023-12-26 10:23:31',1,0,2,2,2),(50,'abbas',1,0,1,'2023-12-26 10:40:04',1,0,3,0,2),(51,'ali',1,2,1,'2023-12-26 12:46:51',1,2,2,3,2),(52,'ali',0,3,1,'2023-12-26 13:02:53',1,1,1,2,3),(53,'ali',4,2,1,'2023-12-26 13:05:18',1,0,2,0,2);
/*!40000 ALTER TABLE `user_activity` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-26 19:55:30
