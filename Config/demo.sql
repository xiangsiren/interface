/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : 127.0.0.1:3306
Source Database       : demo

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-01-02 10:59:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for blogs
-- ----------------------------
DROP TABLE IF EXISTS `blogs`;
CREATE TABLE `blogs` (
  `id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `summary` varchar(200) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blogs
-- ----------------------------

-- ----------------------------
-- Table structure for case
-- ----------------------------
DROP TABLE IF EXISTS `case`;
CREATE TABLE `case` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `case_name` varchar(255) DEFAULT NULL COMMENT '接口名称',
  `path` varchar(255) NOT NULL COMMENT '请求接口',
  `method` enum('post','get') DEFAULT NULL COMMENT '请求类型',
  `request_data` text COMMENT '请求数据',
  `response_data` text COMMENT '响应数据',
  `time` datetime DEFAULT NULL COMMENT '录制时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of case
-- ----------------------------
INSERT INTO `case` VALUES ('1', '测试用例', '/bmc_hb/1.0/cate/list', 'post', '{\"type\":\"all\",\"belong_to\":\"1794900159\",\"group_type\":\"service\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/cate/list?&user_id=1794900158&ts=1577518073&nonce=937063&menu_id=1810207793&sig=e8275aa2113e26413533bd7e711a4cddb93a9d97', '2019-12-28 15:27:53');
INSERT INTO `case` VALUES ('2', '测试用例', '/bmc_hb/1.0/account/supplier_list', 'post', '{\"supplier_type\":\"supplier\",\"page\":1,\"pagesize\":10000,\"origin\":\"directly\",\"type\":\"all\",\"search\":\"\",\"sort\":\"desc\",\"belong_to\":\"1794900159\",\"group_type\":\"service\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/account/supplier_list?&user_id=1794900158&ts=1577518073&nonce=928973&menu_id=1810207793&sig=66a29e14036bd55e0a9f20ee7f7ce5095726a4e5', '2019-12-28 15:27:53');
INSERT INTO `case` VALUES ('3', '测试用例', '/bmc_hb/1.0/unit/list_all', 'post', '{\"type_group\":[\"brand\"],\"belong_to\":\"1794900159\",\"group_type\":\"service\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/unit/list_all?&user_id=1794900158&ts=1577518073&nonce=327380&menu_id=1810207793&sig=5d57174b3ebb8d0f77c580f07ffae3e6b52537e2', '2019-12-28 15:27:53');
INSERT INTO `case` VALUES ('4', '测试用例', '/bmc_hb/1.0/unit/list_label', 'post', '{\"group_type\":\"service\",\"belong_to\":\"1794900159\",\"page\":1,\"pagesize\":10000,\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/unit/list_label?&user_id=1794900158&ts=1577518073&nonce=793269&menu_id=1810207793&sig=f663769ad4690797ae329ac52ed2bd720f26e99a', '2019-12-28 15:27:53');
INSERT INTO `case` VALUES ('5', '测试用例', '/bmc_hb/1.0/goods/goods_list', 'post', '{\"belong_to\":\"1794900159\",\"create_type\":\"service\",\"status\":0,\"brand\":\"\",\"cate_id\":\"\",\"supplier_id\":\"\",\"level\":\"\",\"origin\":\"directly\",\"sort\":\"-ctime\",\"page\":1,\"pagesize\":10,\"name\":\"\",\"group_type\":\"service\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/goods/goods_list?&user_id=1794900158&ts=1577518073&nonce=199052&menu_id=1810207793&sig=f33520c7e81caaaca31d18ceb2c02bafe8f98689', '2019-12-28 15:27:53');
INSERT INTO `case` VALUES ('6', '测试用例', '/bmc_hb/1.0/account/login', 'post', '{\"account\":\"13296712612\",\"password\":\"2ae849ff090b7205566e268123473e700d6957ce\",\"belong_to\":0,\"group_type\":0,\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', 'https://saas-test.banmacang.com/bmc_hb/1.0/account/login?&user_id=0&ts=1577518324&nonce=771079&menu_id=1&sig=d898057dbc802d72e040e5b73e5ee68a330474f0', '2019-12-28 15:32:04');
INSERT INTO `case` VALUES ('7', '测试用例', '/bmc_app/v1/auth/auth_list', 'get', '', 'https://saas-test.banmacang.com/bmc_app/v1/auth/auth_list?&belong_to=1794900159&group_type=service&sys_source=PC&sys_version=V2.2.1&user_id=1794900158&ts=1577518324&nonce=483753&menu_id=1&sig=a5f5d678615b221f44edbe6d8ed55f46c2a91822', '2019-12-28 15:32:05');
INSERT INTO `case` VALUES ('8', '测试用例', '/bmc_app/v1/welcome/get_info', 'get', '', 'https://saas-test.banmacang.com/bmc_app/v1/welcome/get_info?&belong_to=1794900159&group_type=service&sys_source=PC&sys_version=V2.2.1&user_id=1794900158&ts=1577518324&nonce=584659&menu_id=1&sig=3733e1f221cdc48888b442dee03bac73e7a96f33', '2019-12-28 15:32:05');

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` varchar(50) NOT NULL,
  `blog_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments
-- ----------------------------

-- ----------------------------
-- Table structure for hibernate_sequence
-- ----------------------------
DROP TABLE IF EXISTS `hibernate_sequence`;
CREATE TABLE `hibernate_sequence` (
  `next_val` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of hibernate_sequence
-- ----------------------------
INSERT INTO `hibernate_sequence` VALUES ('2');

-- ----------------------------
-- Table structure for model_user
-- ----------------------------
DROP TABLE IF EXISTS `model_user`;
CREATE TABLE `model_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of model_user
-- ----------------------------
INSERT INTO `model_user` VALUES ('1', '22');
INSERT INTO `model_user` VALUES ('2', '33');
INSERT INTO `model_user` VALUES ('3', '44');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'renren', 'admin', 'admin');
INSERT INTO `users` VALUES ('3', 'ss', '123', 'muirng');
