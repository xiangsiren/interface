/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : 127.0.0.1:3306
Source Database       : demo

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-01-08 17:13:26
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
  `request_url` text,
  `request_data` text COMMENT '请求数据',
  `response_data` text COMMENT '响应数据',
  `time` datetime DEFAULT NULL COMMENT '录制时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of case
-- ----------------------------
INSERT INTO `case` VALUES ('1', '测试用例', '/bmc_hb/1.0/account/add_supplier', 'post', 'https://saas-test.banmacang.com/bmc_hb/1.0/account/add_supplier?&user_id=1818700001&ts=1578450811&nonce=148151&menu_id=1810207805&sig=a653d422b22c8d52cd1514a65e89bc6136c704ce', '{\"account\":\"xiaoyan\",\"password\":\"2ae849ff090b7205566e268123473e700d6957ce\",\"supplier_name\":\"陈永建材批发\",\"phone\":\"15355009365\",\"region\":1271,\"province\":11,\"city\":123,\"address\":\"浙江省杭州市余杭区梦想小镇\",\"supplier_type\":\"service\",\"belong_to\":\"1818700002\",\"bank\":\"\",\"bank_name\":\"\",\"bank_num\":\"\",\"alipay_account\":\"\",\"weixin_account\":\"\",\"remark\":\"\",\"supplier_img\":\"\",\"contact_name\":\"陈永\",\"login_phone\":\"15355009365\",\"area_type\":\"\",\"regional\":[],\"group_type\":\"coc\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', null, '2020-01-08 10:33:31');
INSERT INTO `case` VALUES ('2', '测试用例', '/bmc_hb/1.0/account/get_supplier_list', 'post', 'https://saas-test.banmacang.com/bmc_hb/1.0/account/get_supplier_list?&user_id=1818700001&ts=1578450817&nonce=976101&menu_id=1810207805&sig=0350263f6663a0b62d8cb421970335fd0df3edab', '{\"page\":1,\"pagesize\":10,\"sort\":\"desc\",\"role\":\"coc\",\"belong_to\":\"1818700002\",\"group_type\":\"coc\",\"sys_source\":\"PC\",\"sys_version\":\"V2.2.1\"}', null, '2020-01-08 10:33:37');

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
