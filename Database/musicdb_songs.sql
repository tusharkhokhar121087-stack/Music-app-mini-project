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
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `artist` varchar(100) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `audio_file` varchar(255) DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_category` (`category_id`),
  CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,'Safar','Arijit Singh, Pritam','\\static\\images\\safar.jpeg','Safar_Full_Video_-_Jab_Harry_Met_Sejal__Shah_Rukh_Khan_Anushka_Sharma__Arijit_Singh__Pritam.mp3',1),(2,'Aasman Ko Chukar Dekha','Daler Mehndi','\\static\\images\\aasman.jpeg','Aasman_Ko_Chukar_Dekha_Return_Of_Hanuman_Animation_I_Daler_Mehndi_I_Tuesday_Tracks_-_Daler_Mehndi_youtube.mp3',1),(3,'Zaalima','Arijit Singh & Harshdeep K','\\static\\images\\zaalima.jpeg','Zaalima_-_Lyrical_Raees_Shah_Rukh_Khan_Arijit_Singh__Harshdeep_K_JAM8-Pritam_-_Zee_Music_Company_youtube.mp3',1),(4,'O Meri Laila','Atif Aslam, Jyotica Tangri','\\static\\images\\laila.jpeg','O_Meri_Laila_-_Lyrical__Laila_Majnu__Jyotica_Tangri__Avinash_Tiwary__Tripti_Dimri.mp3',1),(5,'Kaise Hua',' Vishal Mishra','\\static\\images\\kaisehua.jpeg','LYRICAL_Kaise_Hua__Kabir_Singh__Shahid_K_Kiara_A_Sandeep_V__Vishal_Mishra_Manoj_Muntashir.mp3',1),(6,'Chitta','Manan Bhardwaj','\\static\\images\\chitta.jpeg','Chitta_Full_Video_Shiddat_Sunny_Kaushal_Radhika_Madan_Mohit_R_Diana_P_Manan_Bhardwaj_-_T-Series_youtube.mp3',1),(7,'Moti Veraana',' Amit Trivedi feat. Osman Mir','\\static\\images\\motiverana.jpeg','Moti_Veraana__New_Navratri_Song_2020__Songs_of_Faith__Amit_Trivedi_feat._Osman_Mir__AT_Azaad.mp3',4),(9,'I Think They Call This Love','Elliot James Reay','\\static\\images\\ithink.jpeg','I_Think_They_Call_This_Love_Cover.mp3',3),(10,'Line Without a Hook','Ricky Montgomery','\\static\\images\\line.jpeg','Ricky_Montgomery_-_Line_Without_a_Hook_Official_Lyric_Video.mp3',3),(11,'Old Town Road','Lil Nas X','\\static\\images\\old.jpeg','youtubeGetPOT_video_r7qovpFAGrQ.mp3',3),(12,'Naagar Nandji Na Laal ','Aditya Gadhvi','\\static\\images\\ag.jpeg','Naagar_Nandji_Na_Laal__Aditya_Gadhvi__Ft._Kinjal_Rajpriya.mp3',4),(14,'We Rollin','Shubh','\\static\\images\\rollin.jpeg','We_Rollin_Official_Audio_-_Shubh_-_SHUBH_youtube.mp3',2);
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
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
