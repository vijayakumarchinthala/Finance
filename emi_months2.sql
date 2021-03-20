-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: emi
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `months2`
--

DROP TABLE IF EXISTS `months2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `months2` (
  `Acc_no` bigint NOT NULL,
  `Name` char(50) NOT NULL,
  `Fi_Mo` char(50) DEFAULT 'NOT PAID',
  `Se_Mo` char(50) DEFAULT 'NOT PAID',
  `Thi_Mo` char(50) DEFAULT 'NOT PAID',
  `Fo_Mo` char(50) DEFAULT 'NOT PAID',
  `Fiv_Mo` char(50) DEFAULT 'NOT PAID',
  `Si_MO` char(50) DEFAULT 'NOT PAID',
  PRIMARY KEY (`Acc_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `months2`
--

LOCK TABLES `months2` WRITE;
/*!40000 ALTER TABLE `months2` DISABLE KEYS */;
INSERT INTO `months2` VALUES (1000,'Vijayakrishna','Paid','Paid','NOT PAID','NOT PAID','NOT PAID','Paid'),(1003,'Budha Prabhas','NOT PAID','Paid','NOT PAID','NOT PAID','NOT PAID','NOT PAID'),(1004,'Ravi Kumar','Paid','NOT PAID','NOT PAID','NOT PAID','NOT PAID','NOT PAID');
/*!40000 ALTER TABLE `months2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-15 16:06:24
