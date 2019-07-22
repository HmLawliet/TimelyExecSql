/*
 Navicat MySQL Data Transfer

 Source Server         : wpwl
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : rm-wz9dawn1azrwj5789to.mysql.rds.aliyuncs.com:3306
 Source Schema         : wpwl_web_pre

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 22/07/2019 11:51:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sql_review_applications
-- ----------------------------
DROP TABLE IF EXISTS `sql_review_applications`;
CREATE TABLE `sql_review_applications`  (
  `id` bigint(20) UNSIGNED NOT NULL,
  `host` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `database` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sentence` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `submit_time` datetime(0) NOT NULL,
  `submit_dur_time` datetime(0) NOT NULL,
  `confirmed` tinyint(4) DEFAULT 0,
  `reviewer` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `review_time` datetime(0) DEFAULT NULL,
  `run` tinyint(4) DEFAULT 0,
  `run_time` datetime(0) DEFAULT NULL,
  `run_duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'sql语句review申请' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
