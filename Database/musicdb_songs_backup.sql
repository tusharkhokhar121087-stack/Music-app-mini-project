-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: musicdb
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `songs_backup`
--

DROP TABLE IF EXISTS `songs_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs_backup` (
  `id` int NOT NULL DEFAULT '0',
  `title` varchar(100) DEFAULT NULL,
  `artist` varchar(100) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `audio_file` varchar(255) DEFAULT NULL,
  `category_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs_backup`
--

LOCK TABLES `songs_backup` WRITE;
/*!40000 ALTER TABLE `songs_backup` DISABLE KEYS */;
INSERT INTO `songs_backup` VALUES (1,'Starboy','Daft Punk','\\static\\images\\starboy.JPG','The Weeknd - Starboy ft. Daft Punk (Official Video).mp3',NULL),(2,'Waka Waka','Shakira','\\static\\images\\wakawaka.jpeg','Shakira - Waka Waka (This Time for Africa) (The Official 2010 FIFA World Cup™ Song).mp3',NULL),(3,'Gangnam Style','PSY','\\static\\images\\gangnam_style.jpeg','PSY - GANGNAM STYLE(강남스타일) M⧸V.mp3',NULL),(4,'Old Town Road','Lil Nas X','\\static\\images\\oldtownroad.jpeg','youtube+GetPOT video #r7qovpFAGrQ.mp3',NULL),(5,'Gangsta\'s Paradise','Coolio','\\static\\images\\gp.jpeg','Coolio_-_Gangstas_Paradise_feat._L.V._Official_Music_Video.mp3',NULL);
/*!40000 ALTER TABLE `songs_backup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-03 22:36:08
