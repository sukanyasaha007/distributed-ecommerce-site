-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: mysql
-- ------------------------------------------------------
-- Server version	5.7.32-google-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `onlineshopping`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `onlineshopping` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `onlineshopping`;

--
-- Table structure for table `addproduct`
--

DROP TABLE IF EXISTS `addproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `addproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount` int(11) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `colors` text NOT NULL,
  `desc` text NOT NULL,
  `pub_date` datetime NOT NULL,
  `category_id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `image_1` varchar(150) NOT NULL,
  `image_2` varchar(150) NOT NULL,
  `image_3` varchar(150) NOT NULL,
  `keywords` text,
  `condition` text,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `addproduct_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `addproduct_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4953 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addproduct`
--

LOCK TABLES `addproduct` WRITE;
/*!40000 ALTER TABLE `addproduct` DISABLE KEYS */;
INSERT INTO `addproduct` VALUES (1,'macbook pro',1200.99,0,15,'gray,white,black,pink','In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 19:48:55',2,1,'492392c9a1d80c65f3c3.jpg','68e0b733e736307b0cba.jpeg','870b6e7fe62f69b1b811.jpeg','laptop',NULL),(2,'iphone x',1150.99,0,20,'gray,white,black','In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:09:15',1,1,'1b6b45a578914ed1fde8.jpg','f7a5a4ca49273d1ca481.jpeg','adf5364b9edb107fcc91.jpg','phone',NULL),(3,'imac',1950.99,10,20,'gray,white,black','In that case, the MacBook Pro is most certainly worth it because it may be the only laptop that can do the job. Plus, the MacBook Pro can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:10:20',3,1,'fcd9f839069f478205ca.jpeg','c3434dc04ae9b08a1a62.jpg','f0f100021cc040042e55.jpg','laptop',NULL),(4,'sony laptop',880.50,15,20,'gray,white,black','In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:11:43',2,2,'1a8f02a703d918008306.jpg','64ee0289b5a406f5bcf9.jpg','1bb91dfc4629c7adcd2c.jpg','laptop',NULL),(5,'sony tv',980.50,0,99,'pink,gray,white,black,blue','In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:14:20',4,2,'87fcab43cab157ab14b7.jpg','34942c9898c611980859.jpg','02448be8f85e3555bbd3.jpeg','tv',NULL),(6,'sony mobile',780.50,10,20,'blue,gray,white,black','In that case, the Sony is most certainly worth it because it may be the only laptop that can do the job. Plus, the Sony  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:15:54',1,2,'040f3c7cb7d97ac64e6e.jpeg','24929353ddc0bafa0446.jpg','33db0031a633112aee3a.jpeg','phone',NULL),(7,'HP',780.50,5,20,'blue,gray,white,black','In that case, the HP is most certainly worth it because it may be the only laptop that can do the job. Plus, the PH  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:18:25',2,4,'fb152ad7428856fb1a92.jpg','f30553a2120ecde23684.jpeg','397833603b0ea0762805.jpg','laptop',NULL),(8,'Dell',780.50,5,20,'blue,gray,white,black','In that case, the HP is most certainly worth it because it may be the only laptop that can do the job. Plus, the PH  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:19:50',2,3,'c8cd10e2fd79892fd1f1.jpeg','7b3f6dcc218945581199.jpg','16cfef10d24fe04f54ac.jpeg','lapop',NULL),(9,'Samsang mobile',780.50,15,25,'blue,gray,white,black','In that case, the Samsang is most certainly worth it because it may be the only laptop that can do the job. Plus, the Samsang  can also be configured to boot Windows if that is needed for certain software available only on Windows','2020-02-16 20:21:55',1,6,'b93a85f9a61f2a7856d8.png','36506d32d97d01c298a1.jpeg','b691bc6172599269eed1.jpg','mobile',NULL),(10,'Rado watch',1200.99,0,25,'golden,white,black','Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In \"How to Win Friends and Influence People\", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity','2020-02-17 18:21:24',7,5,'b85904527fd0cea93c90.jpeg','c1c37e487199c78c64d3.jpg','ee42709e4fe53e241762.jpeg','watch',NULL),(11,'Canon camera ',560.89,0,25,'gray,white,black','Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In \"How to Win Friends and Influence People\", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity','2020-02-17 18:22:57',6,7,'dc900c380baf7d227ef0.png','21b85a9bc4f7b8ef21fc.jpeg','3e2be726a5b063a2cfe1.jpeg','camera',NULL),(12,'Apple watch',450.89,10,9,'blue,gray,white,black','Millions of people around the world have - and continue to - improve their lives based on the teachings of Dale Carnegie. In \"How to Win Friends and Influence People\", Carnegie offers practical advice and techniques, in his exuberant and conversational style, for how to get out of a mental rut and make life more rewarding. His advice has stood the test of time and will teach you how to: make friends quickly and easily; increase your popularity','2020-02-17 18:29:29',7,1,'09f788f8cb89c480faa7.png','87bf0baeab6af4239466.jpg','62f2f68db7286cbbd58a.jpeg','watch',NULL),(13,'Galaxy',400.00,10,19,'red','Sony Galaxy cheap good fast','2021-02-20 19:20:01',3,2,'21d278cd3fcbd593c7df.jpeg','fabaf16b5eb8f789c4b3.jpeg','907de7caf1b8f84d8e69.jpeg','phone',NULL),(14,'Galaxy M1',500.00,0,42,'black','sony galaxy mobile m1 phone','2021-02-22 17:28:04',1,2,'8cfca12051ae41a5221c.jpeg','a65071fa04cd6ed83c95.jpeg','46f2b03774913420b6dc.jpeg','phone',NULL),(15,'mango',2.00,0,3,'yellow','fruit which is yellow in colour','2021-02-25 18:15:05',7,1,'677420a03d91ad29378e.png','48289f60a3137ace4aa8.png','749ee2da67065adc38a1.png','product','product'),(1125,'Ferrari',20000.00,0,0,'red','car automobile which runs very fast','2021-03-01 01:21:48',560,7100,'5df14d16d538db52809a.jpg','731b45327bc9290df425.jpeg','641a067957426005706a.jpg','product','product'),(1360,'Ferrari',300000.00,0,0,'red','car','2021-03-01 04:43:00',560,7100,'eec8ab4ce281d32aeba4.jpg','e9b681d6aeceb7b2bbec.jpeg','3ba3c9e087d78b06ce0f.jpg','product','product'),(4041,'Ferrari',300000.00,0,1,'red','car which runs fast','2021-03-01 04:07:51',560,7100,'8bf40e37d841617d62b6.jpg','bf4868a78488c66704c2.jpeg','978d6945202e4bf8616b.jpg','product','product'),(4952,'car',300000.00,0,100,'red','car is fast','2021-03-01 20:14:20',560,7100,'fceb59da274cf12c7fc8.jpg','3fd159c6437bc957aa9f.jpeg','58feab323b886d3c4604.jpg','product','product');
/*!40000 ALTER TABLE `addproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'Apple'),(7,'Canon'),(7100,'car'),(3,'Dell'),(4,'HP'),(5,'Rado'),(6,'samsung'),(2,'Sony');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `name` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount` int(11) DEFAULT NULL,
  `stock` int(11) NOT NULL,
  `colors` text NOT NULL,
  `descp` text NOT NULL,
  `pub_date` datetime NOT NULL,
  `image_1` varchar(150) NOT NULL,
  `image_2` varchar(150) NOT NULL,
  `image_3` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,15,1141,'mango',2.00,0,3,'yellow','fruit which is yellow in colour','2021-02-25 18:15:05','677420a03d91ad29378e.png','48289f60a3137ace4aa8.png','749ee2da67065adc38a1.png');
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (560,'automobile'),(6,'Camera'),(3,'Desktop'),(5,'Ipad'),(2,'Laptop'),(1,'Mobile'),(4,'TV'),(7,'Watch');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_order`
--

DROP TABLE IF EXISTS `customer_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_order` (
  `id` int(11) NOT NULL,
  `invoice` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `date_created` datetime NOT NULL,
  `orders` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice` (`invoice`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_order`
--

LOCK TABLES `customer_order` WRITE;
/*!40000 ALTER TABLE `customer_order` DISABLE KEYS */;
INSERT INTO `customer_order` VALUES (1,'5cb3282fd9','Pending',1,'2020-05-05 19:08:39','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(2,'a6e8a7bf3b','Pending',2,'2020-05-06 11:31:18','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(3,'2c1dba9580','Pending',2,'2020-05-06 11:31:27','{\"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(4,'09fefc3d3c','Pending',2,'2020-05-06 11:36:28','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": \"2\"}}'),(5,'9bb1b9c3d5','Pending',2,'2020-05-06 11:39:05','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": \"2\"}}'),(6,'31b57e2fef','Pending',2,'2020-05-11 18:06:30','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}}'),(7,'ebdbf60f1b','Paid',2,'2020-05-11 18:42:52','{\"10\": {\"color\": \"golden\", \"discount\": 0, \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"discount\": 10, \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}, \"9\": {\"color\": \"blue\", \"discount\": 15, \"name\": \"Samsang mobile\", \"price\": 780.5, \"quantity\": 1}}'),(8,'347bcdf796','Paid',2,'2020-05-11 18:56:24','{\"12\": {\"color\": \"blue\", \"discount\": 10, \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": \"1\"}}'),(9,'49278fe361','Pending',3,'2021-02-20 19:22:25','{\"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}, \"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(10,'32a3611a02','Pending',3,'2021-02-20 19:29:43','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"phone\", \"price\": 400.0, \"quantity\": 1}}'),(11,'daa115646f','Pending',3,'2021-02-20 20:27:00','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"phone\", \"price\": 400.0, \"quantity\": 1}}'),(12,'66e99d657b','Pending',3,'2021-02-20 23:15:16','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"phone\", \"price\": 400.0, \"quantity\": 1}}'),(13,'f6f3e66e6d','Pending',3,'2021-02-20 23:40:34','{\"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(14,'572f1fed8d','Pending',3,'2021-02-20 23:47:49','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 1}}'),(15,'5934b1a930','Pending',3,'2021-02-20 23:53:03','{\"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(16,'d611e1fd00','Pending',3,'2021-02-21 00:07:17','{\"11\": {\"color\": \"gray\", \"colors\": \"gray,white,black\", \"discount\": 0, \"image\": \"dc900c380baf7d227ef0.png\", \"name\": \"Canon camera \", \"price\": 560.89, \"quantity\": 1}}'),(17,'ec4926b0d2','Pending',3,'2021-02-22 03:02:28','{\"10\": {\"color\": \"golden\", \"colors\": \"golden,white,black\", \"discount\": 0, \"image\": \"b85904527fd0cea93c90.jpeg\", \"name\": \"Rado watch\", \"price\": 1200.99, \"quantity\": 2}, \"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"phone\", \"price\": 400.0, \"quantity\": 1}}'),(18,'57911d89ca','Pending',3,'2021-02-22 16:44:23','{\"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(19,'b707747939','Paid',3,'2021-02-22 16:46:24','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(20,'52fa92c2f5','Paid',3,'2021-02-22 17:13:11','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(21,'81c9c6bb56','Paid',3,'2021-02-22 17:35:50','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(22,'98c4f68beb','Paid',3,'2021-02-22 17:37:17','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(23,'da8c1b1b04','Paid',3,'2021-02-22 17:38:06','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(24,'f9bc34c817','Paid',3,'2021-02-22 17:39:41','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(25,'6d9243cbfd','Paid',3,'2021-02-22 17:41:02','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(26,'2dc5024e4a','Paid',3,'2021-02-22 17:42:27','{\"12\": {\"color\": \"blue\", \"colors\": \"blue,gray,white,black\", \"discount\": 10, \"image\": \"09f788f8cb89c480faa7.png\", \"name\": \"Apple watch\", \"price\": 450.89, \"quantity\": 1}}'),(27,'79c0329f49','Paid',3,'2021-02-22 17:43:01','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(28,'dc4aa68378','Paid',3,'2021-02-22 17:45:07','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(29,'e12023f448','Paid',3,'2021-02-22 17:46:30','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(30,'47c201ad4e','Paid',3,'2021-02-22 17:47:40','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(31,'4e9a3c3553','Paid',3,'2021-02-22 17:51:23','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(32,'ed246fb795','Paid',3,'2021-02-22 17:52:53','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(33,'dcc9bbe842','Paid',3,'2021-02-22 17:53:38','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(34,'37845d25d7','Paid',3,'2021-02-22 17:55:15','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(35,'ae72ba2ac4','Paid',3,'2021-02-22 17:57:01','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(36,'0016a7f5c8','Paid',3,'2021-02-22 17:58:07','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(37,'526296e40f','Paid',3,'2021-02-22 18:02:53','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(38,'d84463f260','Paid',3,'2021-02-22 18:03:23','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(39,'87d095a0c8','Paid',3,'2021-02-22 18:05:32','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(40,'fc3a1faeb9','Paid',3,'2021-02-22 18:06:42','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}}'),(41,'f1ab023c7c','Paid',3,'2021-02-22 18:08:40','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(42,'a7181525ce','Paid',3,'2021-02-22 18:19:33','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(43,'23e9810f4c','Paid',3,'2021-02-22 18:21:44','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(44,'9f1227ce2c','Paid',3,'2021-02-22 18:22:38','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(45,'b047ba3bdb','Paid',3,'2021-02-22 18:23:29','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(46,'b1aaf08bff','Paid',3,'2021-02-22 18:29:57','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(47,'2cc2db8af1','Paid',3,'2021-02-22 18:32:01','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(48,'65194d7c90','Paid',3,'2021-02-22 18:33:53','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(49,'9476b9de7d','Paid',3,'2021-02-22 18:36:58','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(50,'9883bfc5c2','Paid',3,'2021-02-22 18:37:36','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(51,'11547029ec','Paid',3,'2021-02-22 18:39:15','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(52,'0ebede258d','Paid',3,'2021-02-22 18:40:33','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(53,'a52068bd22','Paid',3,'2021-02-22 18:41:56','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(54,'f3d71b5d61','Paid',3,'2021-02-22 18:50:43','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(55,'909230853e','Paid',3,'2021-02-22 18:53:53','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(56,'81ec229409','Paid',3,'2021-02-22 18:54:29','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 2}}'),(57,'931eb75553','Pending',3,'2021-02-22 18:55:22','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 2}}'),(58,'896e52afac','Paid',3,'2021-02-22 18:55:32','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 4}}'),(59,'2e30a409aa','Paid',3,'2021-02-22 19:19:23','{\"1\": {\"color\": \"gray\", \"colors\": \"gray,white,black,pink\", \"discount\": 0, \"image\": \"492392c9a1d80c65f3c3.jpg\", \"name\": \"macbook pro\", \"price\": 1200.99, \"quantity\": 2}}'),(60,'caf906ebd3','Paid',3,'2021-02-22 19:22:33','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(61,'1ca7f012ed','Paid',3,'2021-02-22 19:25:19','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(62,'990235a68d','Paid',3,'2021-02-22 19:29:21','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(63,'134f5d5c0c','Paid',3,'2021-02-22 19:31:42','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(64,'350b73c8c8','Paid',3,'2021-02-22 19:32:42','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 5}}'),(65,'100ae607a5','Pending',3,'2021-02-22 19:56:37','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(66,'b6a4461def','Paid',3,'2021-02-22 20:08:42','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(67,'b12c52aecb','Paid',3,'2021-02-22 20:19:31','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 2}}'),(68,'d2d36a0319','Paid',3,'2021-02-22 20:25:19','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 4}}'),(69,'dffa523d74','Paid',3,'2021-02-22 20:27:20','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 2}}'),(70,'6d3775854e','Paid',3,'2021-02-23 01:10:04','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 3}}'),(71,'94e7f78ee7','Paid',3,'2021-02-23 01:12:37','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(72,'edd7251c56','Paid',3,'2021-02-23 01:13:25','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 2}}'),(73,'e5d5ed9b74','Paid',3,'2021-02-23 01:14:23','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(74,'d91e89d1aa','Paid',3,'2021-02-23 01:15:31','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(75,'36f3040d2e','Paid',3,'2021-02-23 01:17:26','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(1141,'6f01d58a96','Paid',1141,'2021-02-27 05:04:03','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(1490,'9165e87b93','Paid',1141,'2021-03-01 20:06:22','{\"5\": {\"color\": \"pink\", \"colors\": \"pink,gray,white,black,blue\", \"discount\": 0, \"image\": \"87fcab43cab157ab14b7.jpg\", \"name\": \"sony tv\", \"price\": 980.5, \"quantity\": 1}}'),(5225,'9e79afc73e','Paid',1141,'2021-03-01 00:46:00','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(5267,'58215d22a9','Paid',5267,'2021-02-27 18:47:16','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(10052,'c569ffd8c2','Paid',1141,'2021-03-01 00:54:36','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(20845,'113c45c052','Pending',1141,'2021-03-01 02:01:34','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(34023,'951e4442eb','Paid',1141,'2021-03-01 04:09:31','{\"4041\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"8bf40e37d841617d62b6.jpg\", \"name\": \"Ferrari\", \"price\": 300000.0, \"quantity\": 1}}'),(45820,'66d7f1e57d','Paid',1141,'2021-03-01 00:41:38','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(46403,'42ffaa93b5','Paid',1141,'2021-03-01 02:06:32','{\"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}}'),(72672,'ba4485aa06','Paid',1141,'2021-03-01 02:21:20','{\"13\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 10, \"image\": \"21d278cd3fcbd593c7df.jpeg\", \"name\": \"Galaxy\", \"price\": 400.0, \"quantity\": 1}, \"14\": {\"color\": \"black\", \"colors\": \"black\", \"discount\": 0, \"image\": \"8cfca12051ae41a5221c.jpeg\", \"name\": \"Galaxy M1\", \"price\": 500.0, \"quantity\": 1}, \"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(83455,'82c1e39ac1','Paid',1141,'2021-03-01 00:49:03','{\"15\": {\"color\": \"yellow\", \"colors\": \"yellow\", \"discount\": 0, \"image\": \"677420a03d91ad29378e.png\", \"name\": \"mango\", \"price\": 2.0, \"quantity\": 1}}'),(94156,'4394bdf806','Paid',1141,'2021-03-01 04:45:56','{\"4041\": {\"color\": \"red\", \"colors\": \"red\", \"discount\": 0, \"image\": \"8bf40e37d841617d62b6.jpg\", \"name\": \"Ferrari\", \"price\": 300000.0, \"quantity\": 1}}');
/*!40000 ALTER TABLE `customer_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rating` (
  `id` int(11) NOT NULL,
  `sellername` varchar(50) DEFAULT NULL,
  `product` varchar(50) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
INSERT INTO `rating` VALUES (323,'Namratha Mysore Keshavaprakash','Ferrari',0),(3843,'Namratha Mysore Keshavaprakash','Clothes',5),(6115,'Namratha Mysore Keshavaprakash','Ferrari',1),(6546,'Namratha Mysore Keshavaprakash','Ferrari',1),(9272,'Namratha Mysore Keshavaprakash','Clothes',5),(9532,'Namratha Mysore Keshavaprakash','Ferrari',1);
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `zipcode` varchar(50) DEFAULT NULL,
  `profile` varchar(200) DEFAULT NULL,
  `date_created` datetime NOT NULL,
  `itemspurchased` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (1,'bugti','jamal','bugti@gmail.com','$2b$12$/YhdxLPfEKKSHyyy7BO4ZeKCPrMjAvit67uuWxVtPR5yGYUvL.yAi','pakistan','quetta','2345325','new street','3468','profile.jpg','2020-04-04 15:29:18',NULL),(2,'jamal','baloch','admin@site.com','$2b$12$r7pK/282Lzg4hnbGs8rRiOmloTuYKj4UhCTmUIt63CAUiXANC18uu','Pakistan','Quetta','2345325','new street','3468','profile.jpg','2020-04-04 16:49:09',NULL),(3,'Sukanya Saha','sukanyasaha007','sukanyasaha007@gmail.com','$2b$12$B8wIBFj.Mg8ge0RGEqk3veNg3qHOud8PzoTeeMcTo48Fn6sZhaozm','India','Howrah','09038416059','21 Munshi Zeller Rahim Lane Salkia, ','711106','profile.jpg','2021-02-20 19:20:45',NULL),(4,'Dipa Saha','dipasaha','dipa.saha5922@gmail.com','$2b$12$NROAJlL/pUsJk.4NqxsG/uMnDuc/xsTQazRT4iNK6AQR1718rm2US','India','Howrah','09830360264','21, Munshi Zeller Rahim Lane Salkia','711106','profile.jpg','2021-02-23 04:15:44',NULL),(1141,'Namratha Mysore Keshavaprakash','namratha2404','nmk002@gmail.com','1234','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-25 18:45:07',0),(3691,'Namratha Mysore Keshavaprakash','nmysorek','nmk003@gmail.com','1234','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-26 22:02:13',0),(4748,'Namratha Mysore Keshavaprakash','nmk1','nmk001@gmail.com','1234','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-25 18:41:13',0),(5267,'Namratha Mysore Keshavaprakash','nmysorek1','nmk004@gmail.com','1234','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-27 18:46:58',0),(8503,'Namratha Mysore Keshavaprakash','nmk','nmk433@gmail.com','$2b$12$4plS3pYPyDECGWlCMZOsL.qO6POEy0SbJc5GWKS06fqnpv5qMpjHS','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-25 18:39:02',0),(9463,'Namratha MK','namratha2403','nmk344@gmail.com','$2b$12$cs/IgvSGOE8FAwnWb.vVVOKs72H/sc7mLjdxHyOR9b1hKKI5nEqQm','India','Bengaluru','7209103801','203, Gangothri Palmgrove, 22 A Main,','560070','profile.jpg','2021-02-24 01:27:02',NULL);
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller_products`
--

DROP TABLE IF EXISTS `seller_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller_products` (
  `id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `products` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller_products`
--

LOCK TABLES `seller_products` WRITE;
/*!40000 ALTER TABLE `seller_products` DISABLE KEYS */;
INSERT INTO `seller_products` VALUES (1,'Dipa Saha','dipa.saha5922@gmail.com','watch tv phone'),(2,'Manisha Saha','manishasaha504@gmail.com','watch tv phone'),(3,'Sukanya Saha','sukanyasaha003@gmail.com','watch tv phone'),(1590,'Namratha','nmk344@gmail.com','tv');
/*!40000 ALTER TABLE `seller_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sold_products`
--

DROP TABLE IF EXISTS `sold_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sold_products` (
  `id` int(11) NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `product` varchar(500) NOT NULL,
  `quantity_sold` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sold_products`
--

LOCK TABLES `sold_products` WRITE;
/*!40000 ALTER TABLE `sold_products` DISABLE KEYS */;
INSERT INTO `sold_products` VALUES (1,'Sukanya Saha','sukanyasaha007@gmail.com','Galaxy M1',13,0),(1360,'Namratha Mysore Keshavaprakash','nmk002@gmail.com','Ferrari',1,-1);
/*!40000 ALTER TABLE `sold_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(180) NOT NULL,
  `profile` varchar(180) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'jamal','jamalbaloch','baloch@gmail.com','$2b$12$lttlMinn6Z0rLRcngqvIUOzEKGjsTQOY6ujKPLNtfcFoDoWKikSHm','profile.jpg'),(2,'jamal','baloch','bugti@gmail.com','$2b$12$6v..i7vr29OWbWnD/YdAt.2njiT8jUytF8pM6ZbiPNRWlHjibFhHS','profile.jpg'),(3,'jamal','jamal','test@test.com','$2b$12$I.TBBC2MUHOVPcY10UUUGu8LVYg/vZdQ8raUwb.ecCWGY5Pu.uf7e','profile.jpg'),(4,'bugti','baloch1','admin@site.com','$2b$12$5dJuBBajeGcB6XESLfWR9uafSXDhtibRhUomWLsy3cGo7jIKNlyGm','profile.jpg'),(5,'Sukanya Saha','sukanyasaha007','sukanyasaha007@gmail.com','$2b$12$9eZvJn3A7DkYk70hPr906e4s1mbDZ1drKZAE/BFsX22iGMLodFDUG','profile.jpg'),(6,'Dipa Saha','dipasaha','dipa.saha5922@gmail.com','$2b$12$GjrWilcVnfe39sqCOpLxs.KfcbqvYnxzAHBZ.LVDuIuuOY0FyG2pe','profile.jpg'),(7,'Manisha Saha','manisha','manishasaha504@gmail.com','$2b$12$RBooYs.2C7nmwwemYAMimuloiaLTEGoAsFZP03O1si/ccJ1ZeqClq','profile.jpg'),(8,'Sukanya Saha','sukanyasaha003','sukanyasaha003@gmail.com','$2b$12$XKohNprcm3h54okmMSEii.03W/5pXHHDEsK14xkqhUA7IRFNDrcbG','profile.jpg'),(1590,'Namratha','nmk1','nmk344@gmail.com','$2b$12$bzV0/2LaBSj1aEm8kJ3XieRSrQpZvARr7h6wxdLM.HR3EBx4F2r3S','profile.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-04  3:48:22
