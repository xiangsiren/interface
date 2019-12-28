/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50553
Source Host           : 127.0.0.1:3306
Source Database       : demo

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2019-12-28 15:35:10
*/

SET FOREIGN_KEY_CHECKS=0;

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
