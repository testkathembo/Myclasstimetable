-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2025 at 10:19 PM
-- Server version: 11.5.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myclasstimetable`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add custom user', 6, 'add_customuser'),
(22, 'Can change custom user', 6, 'change_customuser'),
(23, 'Can delete custom user', 6, 'delete_customuser'),
(24, 'Can view custom user', 6, 'view_customuser'),
(25, 'Can add classroom', 7, 'add_classroom'),
(26, 'Can change classroom', 7, 'change_classroom'),
(27, 'Can delete classroom', 7, 'delete_classroom'),
(28, 'Can view classroom', 7, 'view_classroom'),
(29, 'Can add faculty', 8, 'add_faculty'),
(30, 'Can change faculty', 8, 'change_faculty'),
(31, 'Can delete faculty', 8, 'delete_faculty'),
(32, 'Can view faculty', 8, 'view_faculty'),
(33, 'Can add semester', 9, 'add_semester'),
(34, 'Can change semester', 9, 'change_semester'),
(35, 'Can delete semester', 9, 'delete_semester'),
(36, 'Can view semester', 9, 'view_semester'),
(37, 'Can add lecturer', 10, 'add_lecturer'),
(38, 'Can change lecturer', 10, 'change_lecturer'),
(39, 'Can delete lecturer', 10, 'delete_lecturer'),
(40, 'Can view lecturer', 10, 'view_lecturer'),
(41, 'Can add unit', 11, 'add_unit'),
(42, 'Can change unit', 11, 'change_unit'),
(43, 'Can delete unit', 11, 'delete_unit'),
(44, 'Can view unit', 11, 'view_unit'),
(45, 'Can add student', 12, 'add_student'),
(46, 'Can change student', 12, 'change_student'),
(47, 'Can delete student', 12, 'delete_student'),
(48, 'Can view student', 12, 'view_student'),
(49, 'Can add student unit enrollment', 13, 'add_studentunitenrollment'),
(50, 'Can change student unit enrollment', 13, 'change_studentunitenrollment'),
(51, 'Can delete student unit enrollment', 13, 'delete_studentunitenrollment'),
(52, 'Can view student unit enrollment', 13, 'view_studentunitenrollment'),
(53, 'Can add timetable', 14, 'add_timetable'),
(54, 'Can change timetable', 14, 'change_timetable'),
(55, 'Can delete timetable', 14, 'delete_timetable'),
(56, 'Can view timetable', 14, 'view_timetable'),
(57, 'Can add time slot', 15, 'add_timeslot'),
(58, 'Can change time slot', 15, 'change_timeslot'),
(59, 'Can delete time slot', 15, 'delete_timeslot'),
(60, 'Can view time slot', 15, 'view_timeslot'),
(61, 'Can add classroom availability', 16, 'add_classroomavailability'),
(62, 'Can change classroom availability', 16, 'change_classroomavailability'),
(63, 'Can delete classroom availability', 16, 'delete_classroomavailability'),
(64, 'Can view classroom availability', 16, 'view_classroomavailability'),
(65, 'Can add class timetable', 17, 'add_classtimetable'),
(66, 'Can change class timetable', 17, 'change_classtimetable'),
(67, 'Can delete class timetable', 17, 'delete_classtimetable'),
(68, 'Can view class timetable', 17, 'view_classtimetable');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-01-21 07:18:47.681797', '1', 'BBIT', 1, '[{\"added\": {}}]', 8, 1),
(2, '2025-01-21 07:19:03.139292', '2', 'ICS', 1, '[{\"added\": {}}]', 8, 1),
(3, '2025-01-21 07:19:21.879140', '3', 'BCOM', 1, '[{\"added\": {}}]', 8, 1),
(4, '2025-01-21 07:19:28.760096', '1', 'BBIT1001 - Introduction to Programming', 1, '[{\"added\": {}}]', 11, 1),
(5, '2025-01-21 07:21:51.645604', '2', 'dieudonne', 1, '[{\"added\": {}}]', 6, 1),
(6, '2025-01-21 07:22:04.326455', '1', 'Lecturer: Dieudonne Katsodieu', 1, '[{\"added\": {}}]', 10, 1),
(7, '2025-01-21 09:30:37.208836', '1', 'Semester 1', 1, '[{\"added\": {}}]', 9, 1),
(8, '2025-01-21 09:31:01.321226', '2', 'Semester 2', 1, '[{\"added\": {}}]', 9, 1),
(9, '2025-01-21 09:31:22.525631', '3', 'Semester 3', 1, '[{\"added\": {}}]', 9, 1),
(10, '2025-01-21 09:31:33.476636', '4', 'Semester 4', 1, '[{\"added\": {}}]', 9, 1),
(11, '2025-01-21 09:32:38.383708', '4', 'Semester 5', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 1),
(12, '2025-01-21 09:32:42.284356', '4', 'Semester 6', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 1),
(13, '2025-01-21 09:32:47.650667', '4', 'Semester 7', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 1),
(14, '2025-01-21 09:32:51.500158', '4', 'Semester 8', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 1),
(15, '2025-01-21 09:33:19.598106', '5', 'Semester 4', 1, '[{\"added\": {}}]', 9, 1),
(16, '2025-01-21 09:33:25.926870', '6', 'Semester 5', 1, '[{\"added\": {}}]', 9, 1),
(17, '2025-01-21 09:33:35.204606', '7', 'Semester 6', 1, '[{\"added\": {}}]', 9, 1),
(18, '2025-01-21 09:33:44.042956', '8', 'Semester 7', 1, '[{\"added\": {}}]', 9, 1),
(19, '2025-01-21 09:40:42.509666', '2', 'BBIT101 - Database Management Systems', 1, '[{\"added\": {}}]', 11, 1),
(20, '2025-01-21 09:41:11.539079', '3', 'BBIT1002 - Information Systems', 1, '[{\"added\": {}}]', 11, 1),
(21, '2025-01-21 09:42:44.178581', '4', 'BBIT103 - .	Computer Networks', 1, '[{\"added\": {}}]', 11, 1),
(22, '2025-01-21 09:43:16.930436', '5', 'BBIT104 - Business Statistics', 1, '[{\"added\": {}}]', 11, 1),
(23, '2025-01-21 09:43:53.844439', '6', 'BBIT105 - System Analysis and Design', 1, '[{\"added\": {}}]', 11, 1),
(24, '2025-01-21 09:44:06.152063', '3', 'BBIT102 - Information Systems', 2, '[{\"changed\": {\"fields\": [\"Code\"]}}]', 11, 1),
(25, '2025-01-21 09:44:27.028521', '1', 'BBIT106 - Introduction to Programming', 2, '[{\"changed\": {\"fields\": [\"Code\"]}}]', 11, 1),
(26, '2025-01-21 09:47:32.366388', '3', 'claire', 1, '[{\"added\": {}}]', 6, 1),
(27, '2025-01-21 09:47:55.863326', '2', 'Lecturer: Claire Kahindo', 1, '[{\"added\": {}}]', 10, 1),
(28, '2025-01-21 12:25:56.449915', '1', 'Classroom: STMB-10 (Capacity: 40)', 1, '[{\"added\": {}}]', 7, 1),
(29, '2025-01-21 12:26:25.931274', '2', 'Classroom: Ph1-001 (Capacity: 35)', 1, '[{\"added\": {}}]', 7, 1),
(30, '2025-01-21 12:26:49.171314', '3', 'Classroom: Auditorium (Capacity: 45)', 1, '[{\"added\": {}}]', 7, 1),
(31, '2025-01-21 12:27:08.320721', '4', 'Classroom: STMB F-006 (Capacity: 30)', 1, '[{\"added\": {}}]', 7, 1),
(32, '2025-01-21 12:27:32.336331', '5', 'Classroom: Ph1-002 (Capacity: 45)', 1, '[{\"added\": {}}]', 7, 1),
(33, '2025-01-21 12:30:42.891823', '6', 'BBIT105 - System Analysis and Design', 2, '[{\"changed\": {\"fields\": [\"Lecturer\"]}}]', 11, 1),
(34, '2025-01-21 12:33:41.347812', '7', 'klkl - klklk', 1, '[{\"added\": {}}]', 11, 1),
(35, '2025-01-21 12:34:01.880369', '7', 'klkl - klklk', 3, '', 11, 1),
(36, '2025-01-21 12:49:14.850887', '8', 'ghgh - hjhjhj', 1, '[{\"added\": {}}]', 11, 1),
(37, '2025-01-21 12:49:36.378057', '8', 'ghgh - hjhjhj', 3, '', 11, 1),
(38, '2025-01-22 02:39:48.134613', '4', '101001', 1, '[{\"added\": {}}]', 6, 1),
(39, '2025-01-22 02:40:04.305701', '3', 'Lecturer: Musiva Keli', 1, '[{\"added\": {}}]', 10, 1),
(40, '2025-01-22 02:40:50.447006', '5', '101002', 1, '[{\"added\": {}}]', 6, 1),
(41, '2025-01-22 02:40:59.091728', '4', 'Lecturer: Catherine Ndenya', 1, '[{\"added\": {}}]', 10, 1),
(42, '2025-01-22 02:42:14.956111', '6', '101003', 1, '[{\"added\": {}}]', 6, 1),
(43, '2025-01-22 02:42:24.491463', '5', 'Lecturer: Muhindo Syapa', 1, '[{\"added\": {}}]', 10, 1),
(44, '2025-01-22 02:43:18.629226', '7', '101004', 1, '[{\"added\": {}}]', 6, 1),
(45, '2025-01-22 02:44:40.891436', '3', 'claire', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 6, 1),
(46, '2025-01-22 02:44:53.655484', '3', 'claire', 2, '[]', 6, 1),
(47, '2025-01-22 02:45:44.414439', '2', 'Lecturer: Claire Kahindo', 3, '', 10, 1),
(48, '2025-01-22 02:45:44.414527', '1', 'Lecturer: Dieudonne Katsodieu', 3, '', 10, 1),
(49, '2025-01-22 02:47:11.741030', '8', '101005', 1, '[{\"added\": {}}]', 6, 1),
(50, '2025-01-22 02:48:10.333764', '6', 'Lecturer: Kihembo Dieumerci', 1, '[{\"added\": {}}]', 10, 1),
(51, '2025-01-22 02:48:26.705440', '7', 'Lecturer: Kathembo Katsodieu', 1, '[{\"added\": {}}]', 10, 1),
(52, '2025-01-22 06:20:12.198445', '6', 'BBIT105 - System Analysis and Design', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(53, '2025-01-22 06:20:33.678161', '5', 'BBIT104 - Business Statistics', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(54, '2025-01-22 06:20:59.975012', '4', 'BBIT103 - .	Computer Networks', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(55, '2025-01-22 06:21:25.921563', '3', 'BBIT102 - Information Systems', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(56, '2025-01-22 06:22:07.510476', '2', 'BBIT101 - Database Management Systems', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(57, '2025-01-22 06:32:45.485243', '1', 'BBIT106 - Introduction to Programming', 2, '[{\"changed\": {\"fields\": [\"Lecturer\", \"Semester\"]}}]', 11, 1),
(58, '2025-01-22 06:34:04.932564', '2', 'BBIT101 - Database Management Systems', 2, '[{\"changed\": {\"fields\": [\"Lecturer\"]}}]', 11, 1),
(59, '2025-01-22 07:16:33.516321', '6', 'BBIT105 - System Analysis and Design (4 hrs: 2 physical, 2 online)', 2, '[{\"changed\": {\"fields\": [\"Total hours\", \"Physical hours\", \"Online hours\"]}}]', 11, 1),
(60, '2025-01-22 07:17:27.598048', '5', 'BBIT104 - Business Statistics (3 hrs: 2 physical, 1 online)', 2, '[{\"changed\": {\"fields\": [\"Total hours\", \"Physical hours\", \"Online hours\"]}}]', 11, 1),
(61, '2025-01-22 07:17:39.891050', '4', 'BBIT103 - .	Computer Networks (2 hrs: 2 physical, 0 online)', 2, '[]', 11, 1),
(62, '2025-01-22 07:17:52.303039', '3', 'BBIT102 - Information Systems (4 hrs: 2 physical, 2 online)', 2, '[{\"changed\": {\"fields\": [\"Total hours\", \"Physical hours\", \"Online hours\"]}}]', 11, 1),
(63, '2025-01-22 07:18:06.082303', '2', 'BBIT101 - Database Management Systems (3 hrs: 2 physical, 1 online)', 2, '[{\"changed\": {\"fields\": [\"Total hours\", \"Physical hours\", \"Online hours\"]}}]', 11, 1),
(64, '2025-01-22 07:49:37.954784', '5', 'Classroom: Ph1-002 (Capacity: 8)', 2, '[{\"changed\": {\"fields\": [\"Capacity\"]}}]', 7, 1),
(65, '2025-01-22 07:49:58.129783', '4', 'Classroom: STMB F-006 (Capacity: 15)', 2, '[{\"changed\": {\"fields\": [\"Capacity\"]}}]', 7, 1),
(66, '2025-01-22 07:50:06.728431', '3', 'Classroom: Auditorium (Capacity: 20)', 2, '[{\"changed\": {\"fields\": [\"Capacity\"]}}]', 7, 1),
(67, '2025-01-22 07:50:27.849910', '2', 'Classroom: Ph1-001 (Capacity: 5)', 2, '[{\"changed\": {\"fields\": [\"Capacity\"]}}]', 7, 1),
(68, '2025-01-22 07:50:39.406632', '1', 'Classroom: STMB-10 (Capacity: 10)', 2, '[{\"changed\": {\"fields\": [\"Capacity\"]}}]', 7, 1),
(69, '2025-01-22 07:52:43.939964', '9', '1001', 1, '[{\"added\": {}}]', 6, 1),
(70, '2025-01-22 07:53:21.241244', '1', 'Student: Kathembo Tsongo (ID: 1001)', 1, '[{\"added\": {}}]', 12, 1),
(71, '2025-01-22 07:59:49.752121', '9', 'Kathembo', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 6, 1),
(72, '2025-01-22 07:59:57.946824', '1', 'Student: Kathembo Tsongo (ID: 1001)', 2, '[]', 12, 1),
(73, '2025-01-22 08:50:59.490540', '10', 'Donne', 1, '[{\"added\": {}}]', 6, 1),
(74, '2025-01-22 08:51:11.805452', '2', 'Student: Dieudonne Katso (ID: 1002)', 1, '[{\"added\": {}}]', 12, 1),
(75, '2025-01-22 09:13:25.172440', '11', 'clairo', 1, '[{\"added\": {}}]', 6, 1),
(76, '2025-01-22 09:13:42.588735', '3', 'Student: Claire Lilian (ID: 1003)', 1, '[{\"added\": {}}]', 12, 1),
(77, '2025-01-22 12:00:40.023627', '1', '08:00:00 - 10:00:00', 1, '[{\"added\": {}}]', 15, 1),
(78, '2025-01-22 12:15:16.422956', '1', 'STMB-10 on Monday during 08:00:00 - 10:00:00: Available', 1, '[{\"added\": {}}]', 16, 1),
(79, '2025-01-22 12:17:21.940384', '2', 'Ph1-001 on Monday during 08:00:00 - 10:00:00: Available', 1, '[{\"added\": {}}]', 16, 1),
(80, '2025-01-22 12:17:34.668220', '3', 'STMB F-006 on Monday during 08:00:00 - 10:00:00: Available', 1, '[{\"added\": {}}]', 16, 1),
(81, '2025-01-22 12:19:42.435011', '12', 'Dieud', 1, '[{\"added\": {}}]', 6, 1),
(82, '2025-01-22 12:19:56.403093', '4', 'Student: Dido Kathungu (ID: 1004)', 1, '[{\"added\": {}}]', 12, 1),
(83, '2025-01-22 12:22:39.650352', '13', 'Celi', 1, '[{\"added\": {}}]', 6, 1),
(84, '2025-01-22 12:22:51.294139', '5', 'Student: Celile Kahhh (ID: 1005)', 1, '[{\"added\": {}}]', 12, 1),
(85, '2025-01-22 12:23:42.355926', '14', 'clarice', 1, '[{\"added\": {}}]', 6, 1),
(86, '2025-01-22 12:23:53.497851', '6', 'Student: Kathembo Kathu (ID: 1006)', 1, '[{\"added\": {}}]', 12, 1),
(87, '2025-01-22 12:24:46.756842', '15', 'Norb', 1, '[{\"added\": {}}]', 6, 1),
(88, '2025-01-22 12:25:01.316279', '7', 'Student: Kathe Kahhingooo (ID: 1007)', 1, '[{\"added\": {}}]', 12, 1),
(89, '2025-01-22 12:26:42.389762', '16', 'Keyenb', 1, '[{\"added\": {}}]', 6, 1),
(90, '2025-01-22 12:26:55.289834', '8', 'Student: Kiyengo Goretti (ID: 1008)', 1, '[{\"added\": {}}]', 12, 1),
(91, '2025-01-22 12:33:54.389727', '17', 'Mathe', 1, '[{\"added\": {}}]', 6, 1),
(92, '2025-01-22 12:34:31.651280', '9', 'Student: Mathe Syapa (ID: 1009)', 1, '[{\"added\": {}}]', 12, 1),
(93, '2025-01-22 12:34:44.424784', '9', 'Student: Mathe Syapa (ID: 1009)', 2, '[{\"changed\": {\"fields\": [\"Faculty\"]}}]', 12, 1),
(94, '2025-01-22 12:37:00.833501', '18', 'Emmanuel', 1, '[{\"added\": {}}]', 6, 1),
(95, '2025-01-22 12:37:10.634729', '10', 'Student: Emmanuel Kahindo (ID: 1010)', 1, '[{\"added\": {}}]', 12, 1),
(96, '2025-01-22 12:39:12.307849', '19', 'Emm', 1, '[{\"added\": {}}]', 6, 1),
(97, '2025-01-22 12:39:35.800183', '11', 'Student: Kahi EMm (ID: 1011)', 1, '[{\"added\": {}}]', 12, 1),
(98, '2025-01-22 12:40:55.217653', '20', 'kyahwere', 1, '[{\"added\": {}}]', 6, 1),
(99, '2025-01-22 12:41:09.621784', '12', 'Student: KyahwereK Jery (ID: 1012)', 1, '[{\"added\": {}}]', 12, 1),
(100, '2025-01-22 12:43:02.227045', '21', 'Jeannette', 1, '[{\"added\": {}}]', 6, 1),
(101, '2025-01-22 12:43:11.725169', '13', 'Student: Jeanette Kihem (ID: 1013)', 1, '[{\"added\": {}}]', 12, 1),
(102, '2025-01-22 12:44:00.022962', '22', 'Glory', 1, '[{\"added\": {}}]', 6, 1),
(103, '2025-01-22 12:44:09.875330', '14', 'Student: Glory Math (ID: 1014)', 1, '[{\"added\": {}}]', 12, 1),
(104, '2025-01-23 02:32:07.283768', '23', 'Mbusa', 1, '[{\"added\": {}}]', 6, 1),
(105, '2025-01-23 02:32:25.105587', '15', 'Student: Mbusa Katero (ID: 1016)', 1, '[{\"added\": {}}]', 12, 1),
(106, '2025-01-23 02:33:19.799237', '24', 'Katemb', 1, '[{\"added\": {}}]', 6, 1),
(107, '2025-01-23 02:33:30.453436', '16', 'Student: Katembe Kiso (ID: 1015)', 1, '[{\"added\": {}}]', 12, 1),
(108, '2025-01-23 02:39:02.926292', '25', 'Kiroooh', 1, '[{\"added\": {}}]', 6, 1),
(109, '2025-01-23 02:39:12.812336', '17', 'Student: Kirembo Hugu (ID: 1017)', 1, '[{\"added\": {}}]', 12, 1),
(110, '2025-01-23 06:42:57.829169', '26', 'Musu', 1, '[{\"added\": {}}]', 6, 1),
(111, '2025-01-23 06:43:37.310515', '18', 'Student: Musubai Muhi (ID: 1018)', 1, '[{\"added\": {}}]', 12, 1),
(112, '2025-01-23 09:34:14.432288', '9', 'jfhfjfh - jfjfjfjfj (4 hrs: 2 physical, 2 online)', 1, '[{\"added\": {}}]', 11, 1),
(113, '2025-01-23 09:35:29.231601', '9', 'jfhfjfh - jfjfjfjfj (4 hrs: 2 physical, 2 online)', 2, '[{\"changed\": {\"fields\": [\"Semester\"]}}]', 11, 1),
(114, '2025-01-23 15:26:21.557806', '2', '10:30:00 - 12:30:00', 1, '[{\"added\": {}}]', 15, 1),
(115, '2025-01-24 07:18:19.180127', '3', 'Classroom: Auditorium (Capacity: 20)', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 1),
(116, '2025-01-24 07:18:19.199164', '1', 'Classroom: STMB-10 (Capacity: 10)', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 1),
(117, '2025-01-24 07:23:35.856296', '1', '08:00:00 - 10:00:00', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 15, 1),
(118, '2025-01-24 08:20:34.833204', '2', '10:30:00 - 12:30:00', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 15, 1),
(119, '2025-01-27 08:02:31.645115', '7', 'Zoom (Capacity: 0)', 1, '[{\"added\": {}}]', 7, 1),
(120, '2025-01-27 08:02:54.261936', '7', 'Zoom (Capacity: 0)', 3, '', 7, 1),
(121, '2025-01-27 08:07:37.112280', '6', 'Zoom (Capacity: 0)', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 1),
(122, '2025-01-27 12:04:56.080329', '259', 'System Analysis and Design on Tuesday at 13:00:00 (online)', 3, '', 17, 1),
(123, '2025-01-27 12:04:56.080439', '258', 'System Analysis and Design on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(124, '2025-01-27 12:04:56.080497', '257', 'Business Statistics on Thursday at 08:00:00 (online)', 3, '', 17, 1),
(125, '2025-01-27 12:04:56.080547', '256', 'Business Statistics on Wednesday at 10:00:00 (physical)', 3, '', 17, 1),
(126, '2025-01-27 12:04:56.080591', '255', '.	Computer Networks on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(127, '2025-01-27 12:04:56.080633', '254', 'Information Systems on Wednesday at 08:00:00 (online)', 3, '', 17, 1),
(128, '2025-01-27 12:04:56.080675', '253', 'Information Systems on Tuesday at 10:00:00 (physical)', 3, '', 17, 1),
(129, '2025-01-27 12:04:56.080717', '252', 'Database Management Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(130, '2025-01-27 12:04:56.080759', '251', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(131, '2025-01-27 12:04:56.080802', '250', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(132, '2025-01-27 12:18:06.740648', '260', 'Introduction to Programming on Monda at 08:00:00 (online)', 1, '[{\"added\": {}}]', 17, 1),
(133, '2025-01-27 12:18:30.040325', '260', 'Introduction to Programming on Monda at 08:00:00 (online)', 3, '', 17, 1),
(134, '2025-01-27 18:50:01.374031', '362', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(135, '2025-01-27 18:50:01.374073', '361', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(136, '2025-01-27 18:50:01.374101', '360', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(137, '2025-01-27 18:50:01.374117', '359', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(138, '2025-01-27 18:50:01.374132', '358', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(139, '2025-01-27 18:50:01.374146', '357', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(140, '2025-01-27 18:50:01.374165', '356', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(141, '2025-01-27 18:50:01.374178', '355', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(142, '2025-01-27 18:50:01.374190', '354', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(143, '2025-01-27 18:50:01.374204', '353', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(144, '2025-01-27 18:50:01.374216', '352', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(145, '2025-01-27 18:50:01.374228', '351', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(146, '2025-01-27 18:50:01.374240', '350', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(147, '2025-01-27 18:50:01.374253', '349', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(148, '2025-01-27 18:50:01.374265', '348', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(149, '2025-01-27 18:50:01.374277', '347', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(150, '2025-01-27 18:50:01.374288', '346', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(151, '2025-01-27 18:50:01.374301', '345', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(152, '2025-01-27 18:53:05.836939', '380', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(153, '2025-01-27 18:53:05.837148', '379', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(154, '2025-01-27 18:53:05.837250', '378', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(155, '2025-01-27 18:53:05.837329', '377', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(156, '2025-01-27 18:53:05.837392', '376', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(157, '2025-01-27 18:53:05.837516', '375', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(158, '2025-01-27 18:53:05.837580', '374', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(159, '2025-01-27 18:53:05.837639', '373', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(160, '2025-01-27 18:53:05.837698', '372', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(161, '2025-01-27 18:53:05.837757', '371', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(162, '2025-01-27 18:53:05.837817', '370', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(163, '2025-01-27 18:53:05.837878', '369', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(164, '2025-01-27 18:53:05.837937', '368', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(165, '2025-01-27 18:53:05.837998', '367', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(166, '2025-01-27 18:53:05.838072', '366', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(167, '2025-01-27 18:53:05.838134', '365', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(168, '2025-01-27 18:53:05.838194', '364', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(169, '2025-01-27 18:53:05.838254', '363', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(170, '2025-01-27 18:56:13.455527', '398', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(171, '2025-01-27 18:56:13.455652', '397', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(172, '2025-01-27 18:56:13.455716', '396', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(173, '2025-01-27 18:56:13.455773', '395', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(174, '2025-01-27 18:56:13.455803', '394', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(175, '2025-01-27 18:56:13.455830', '393', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(176, '2025-01-27 18:56:13.455857', '392', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(177, '2025-01-27 18:56:13.455884', '391', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(178, '2025-01-27 18:56:13.455909', '390', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(179, '2025-01-27 18:56:13.455935', '389', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(180, '2025-01-27 18:56:13.455961', '388', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(181, '2025-01-27 18:56:13.455988', '387', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(182, '2025-01-27 18:56:13.456014', '386', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(183, '2025-01-27 18:56:13.456040', '385', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(184, '2025-01-27 18:56:13.456077', '384', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(185, '2025-01-27 18:56:13.456117', '383', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(186, '2025-01-27 18:56:13.456143', '382', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(187, '2025-01-27 18:56:13.456170', '381', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(188, '2025-01-27 19:59:45.917356', '416', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(189, '2025-01-27 19:59:45.917450', '415', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(190, '2025-01-27 19:59:45.917499', '414', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(191, '2025-01-27 19:59:45.917550', '413', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(192, '2025-01-27 19:59:45.917591', '412', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(193, '2025-01-27 19:59:45.917630', '411', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(194, '2025-01-27 19:59:45.917666', '410', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(195, '2025-01-27 19:59:45.917701', '409', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(196, '2025-01-27 19:59:45.917735', '408', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(197, '2025-01-27 19:59:45.917772', '407', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(198, '2025-01-27 19:59:45.917808', '406', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(199, '2025-01-27 19:59:45.917845', '405', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(200, '2025-01-27 19:59:45.917871', '404', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(201, '2025-01-27 19:59:45.917894', '403', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(202, '2025-01-27 19:59:45.917916', '402', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(203, '2025-01-27 19:59:45.917937', '401', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(204, '2025-01-27 19:59:45.917970', '400', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(205, '2025-01-27 19:59:45.918001', '399', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(206, '2025-01-27 20:02:14.958964', '434', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(207, '2025-01-27 20:02:14.959010', '433', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(208, '2025-01-27 20:02:14.959028', '432', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(209, '2025-01-27 20:02:14.959043', '431', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(210, '2025-01-27 20:02:14.959057', '430', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(211, '2025-01-27 20:02:14.959070', '429', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(212, '2025-01-27 20:02:14.959083', '428', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(213, '2025-01-27 20:02:14.959095', '427', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(214, '2025-01-27 20:02:14.959106', '426', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(215, '2025-01-27 20:02:14.959119', '425', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(216, '2025-01-27 20:02:14.959131', '424', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(217, '2025-01-27 20:02:14.959144', '423', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(218, '2025-01-27 20:02:14.959155', '422', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(219, '2025-01-27 20:02:14.959167', '421', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(220, '2025-01-27 20:02:14.959179', '420', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(221, '2025-01-27 20:02:14.959191', '419', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(222, '2025-01-27 20:02:14.959204', '418', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(223, '2025-01-27 20:02:14.959216', '417', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(224, '2025-01-27 20:06:41.151446', '452', 'System Analysis and Design on Monday at 15:00:00 (online)', 3, '', 17, 1),
(225, '2025-01-27 20:06:41.151540', '451', 'System Analysis and Design on Monday at 13:00:00 (online)', 3, '', 17, 1),
(226, '2025-01-27 20:06:41.151592', '450', 'System Analysis and Design on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(227, '2025-01-27 20:06:41.151613', '449', 'System Analysis and Design on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(228, '2025-01-27 20:06:41.151632', '448', 'Business Statistics on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(229, '2025-01-27 20:06:41.151656', '447', 'Business Statistics on Tuesday at 08:00:00 (physical)', 3, '', 17, 1),
(230, '2025-01-27 20:06:41.151674', '446', 'Business Statistics on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(231, '2025-01-27 20:06:41.151691', '445', '.	Computer Networks on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(232, '2025-01-27 20:06:41.151708', '444', '.	Computer Networks on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(233, '2025-01-27 20:06:41.151725', '443', 'Information Systems on Tuesday at 10:00:00 (online)', 3, '', 17, 1),
(234, '2025-01-27 20:06:41.151744', '442', 'Information Systems on Tuesday at 08:00:00 (online)', 3, '', 17, 1),
(235, '2025-01-27 20:06:41.151762', '441', 'Information Systems on Monday at 15:00:00 (physical)', 3, '', 17, 1),
(236, '2025-01-27 20:06:41.151781', '440', 'Information Systems on Monday at 13:00:00 (physical)', 3, '', 17, 1),
(237, '2025-01-27 20:06:41.151800', '439', 'Database Management Systems on Monday at 13:00:00 (online)', 3, '', 17, 1),
(238, '2025-01-27 20:06:41.151818', '438', 'Database Management Systems on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(239, '2025-01-27 20:06:41.151836', '437', 'Database Management Systems on Monday at 08:00:00 (physical)', 3, '', 17, 1),
(240, '2025-01-27 20:06:41.151854', '436', 'Introduction to Programming on Monday at 10:00:00 (physical)', 3, '', 17, 1),
(241, '2025-01-27 20:06:41.151877', '435', 'Introduction to Programming on Monday at 08:00:00 (physical)', 3, '', 17, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'school', 'classroom'),
(16, 'school', 'classroomavailability'),
(17, 'school', 'classtimetable'),
(8, 'school', 'faculty'),
(10, 'school', 'lecturer'),
(9, 'school', 'semester'),
(12, 'school', 'student'),
(13, 'school', 'studentunitenrollment'),
(15, 'school', 'timeslot'),
(14, 'school', 'timetable'),
(11, 'school', 'unit'),
(5, 'sessions', 'session'),
(6, 'users', 'customuser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-01-21 07:16:20.376760'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-01-21 07:16:20.425877'),
(3, 'auth', '0001_initial', '2025-01-21 07:16:20.564486'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-01-21 07:16:20.594461'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-01-21 07:16:20.603267'),
(6, 'auth', '0004_alter_user_username_opts', '2025-01-21 07:16:20.611817'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-01-21 07:16:20.620081'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-01-21 07:16:20.624240'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-01-21 07:16:20.630996'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-01-21 07:16:20.637065'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-01-21 07:16:20.644732'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-01-21 07:16:20.666465'),
(13, 'auth', '0011_update_proxy_permissions', '2025-01-21 07:16:20.675265'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-01-21 07:16:20.680596'),
(15, 'users', '0001_initial', '2025-01-21 07:16:20.845520'),
(16, 'admin', '0001_initial', '2025-01-21 07:16:20.901548'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-01-21 07:16:20.912207'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-21 07:16:20.920032'),
(19, 'school', '0001_initial', '2025-01-21 07:16:21.239656'),
(20, 'school', '0002_remove_unit_lecturer_studentunitenrollment', '2025-01-21 07:16:21.673325'),
(21, 'sessions', '0001_initial', '2025-01-21 07:16:21.703126'),
(22, 'users', '0002_alter_customuser_faculty_id_and_more', '2025-01-21 07:16:21.727880'),
(23, 'school', '0003_remove_semester_end_date_remove_semester_start_date', '2025-01-21 09:30:19.696284'),
(24, 'school', '0004_remove_student_enrolled_units_unit_lecturer', '2025-01-21 12:23:56.696731'),
(25, 'school', '0005_unit_online_hours_unit_physical_hours_and_more', '2025-01-22 06:53:27.670111'),
(26, 'school', '0006_alter_unit_online_hours_alter_unit_physical_hours_and_more', '2025-01-22 06:56:03.542909'),
(27, 'school', '0002_timeslot_timetable', '2025-01-22 11:58:28.783319'),
(28, 'school', '0003_classroomavailability', '2025-01-22 12:13:23.630468'),
(29, 'school', '0004_remove_unit_semester', '2025-01-23 09:51:01.350060'),
(30, 'school', '0005_alter_unit_online_hours_alter_unit_physical_hours_and_more', '2025-01-23 15:05:51.286778'),
(31, 'school', '0006_classtimetable_delete_timetable', '2025-01-23 15:16:53.173126'),
(32, 'school', '0007_timeslot_is_available', '2025-01-23 15:30:09.338699'),
(33, 'school', '0008_alter_classroomavailability_is_available', '2025-01-24 05:04:29.005982'),
(34, 'school', '0009_classroom_is_available_delete_classroomavailability', '2025-01-24 07:17:18.684898'),
(35, 'school', '0010_classtimetable_duration_classtimetable_lecturer_and_more', '2025-01-24 07:51:52.962117'),
(36, 'school', '0002_alter_classtimetable_duration', '2025-01-27 05:43:40.438594'),
(37, 'school', '0003_alter_classtimetable_duration', '2025-01-27 07:25:56.721729');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('43kp6gpmat2cvtuktqlhtztgyx1gxjc3', '.eJxVjEEOwiAQRe_C2pABBIpL9z0DmTKDVA0kpV0Z765NutDtf-_9l4i4rSVunZc4k7gIJU6_24TpwXUHdMd6azK1ui7zJHdFHrTLsRE_r4f7d1Cwl28NkJzxCrP1flCodNYpOc5o9ADOe9AcVKAMDEaDpZADEaAD0smeEcX7A8mrN4s:1tcUAU:vd3ASAY-s3HOj2v19258OovDjA4LRlOBP9nXJe5d2KM', '2025-02-10 18:49:06.061847'),
('q1wov5ow6gkian9bd943rlzf9jygz8pm', '.eJxVjEEOwiAQRe_C2pABBIpL9z0DmTKDVA0kpV0Z765NutDtf-_9l4i4rSVunZc4k7gIJU6_24TpwXUHdMd6azK1ui7zJHdFHrTLsRE_r4f7d1Cwl28NkJzxCrP1flCodNYpOc5o9ADOe9AcVKAMDEaDpZADEaAD0smeEcX7A8mrN4s:1taDGz:MCPce55p6_Tx_kyUlyP-pgpwaDnS9WLtnTes8GQIDBg', '2025-02-04 12:22:25.110022');

-- --------------------------------------------------------

--
-- Table structure for table `school_classroom`
--

CREATE TABLE `school_classroom` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `capacity` int(11) NOT NULL,
  `is_available` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_classroom`
--

INSERT INTO `school_classroom` (`id`, `name`, `capacity`, `is_available`) VALUES
(1, 'STMB-10', 10, 0),
(2, 'Ph1-001', 5, 1),
(3, 'Auditorium', 20, 0),
(4, 'STMB F-006', 15, 1),
(5, 'Ph1-002', 8, 1),
(6, 'Zoom', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `school_classtimetable`
--

CREATE TABLE `school_classtimetable` (
  `id` bigint(20) NOT NULL,
  `day` varchar(10) NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(10) NOT NULL,
  `classroom_id` varchar(100) NOT NULL,
  `unit_id` bigint(20) NOT NULL,
  `duration` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_classtimetable`
--

INSERT INTO `school_classtimetable` (`id`, `day`, `time`, `status`, `classroom_id`, `unit_id`, `duration`) VALUES
(723, 'Monday', '08:00:00.000000', 'physical', '2', 1, '2 hours'),
(724, 'Monday', '08:00:00.000000', 'physical', '4', 2, '2 hours'),
(725, 'Wednesday', '08:00:00.000000', 'online', '6', 2, '1 hour'),
(726, 'Monday', '10:00:00.000000', 'physical', '4', 3, '2 hours'),
(727, 'Wednesday', '08:00:00.000000', 'online', '6', 3, '2 hours'),
(728, 'Monday', '08:00:00.000000', 'physical', '5', 4, '2 hours'),
(729, 'Monday', '13:00:00.000000', 'physical', '4', 5, '2 hours'),
(730, 'Wednesday', '10:00:00.000000', 'online', '6', 5, '1 hour'),
(731, 'Monday', '15:00:00.000000', 'physical', '4', 6, '2 hours'),
(732, 'Wednesday', '08:00:00.000000', 'online', '6', 6, '2 hours');

-- --------------------------------------------------------

--
-- Table structure for table `school_faculty`
--

CREATE TABLE `school_faculty` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_faculty`
--

INSERT INTO `school_faculty` (`id`, `name`, `description`) VALUES
(1, 'BBIT', 'What is BBIT.....'),
(2, 'ICS', 'What is ICS'),
(3, 'BCOM', 'What is BCOM');

-- --------------------------------------------------------

--
-- Table structure for table `school_lecturer`
--

CREATE TABLE `school_lecturer` (
  `id` bigint(20) NOT NULL,
  `faculty_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_lecturer`
--

INSERT INTO `school_lecturer` (`id`, `faculty_id`, `user_id`) VALUES
(3, 1, 4),
(4, 1, 5),
(5, 1, 6),
(6, 1, 7),
(7, 1, 8);

-- --------------------------------------------------------

--
-- Table structure for table `school_semester`
--

CREATE TABLE `school_semester` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_semester`
--

INSERT INTO `school_semester` (`id`, `name`) VALUES
(1, 'Semester 1'),
(2, 'Semester 2'),
(3, 'Semester 3'),
(5, 'Semester 4'),
(6, 'Semester 5'),
(7, 'Semester 6'),
(8, 'Semester 7'),
(4, 'Semester 8');

-- --------------------------------------------------------

--
-- Table structure for table `school_student`
--

CREATE TABLE `school_student` (
  `id` bigint(20) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `faculty_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_student`
--

INSERT INTO `school_student` (`id`, `student_id`, `faculty_id`, `user_id`) VALUES
(1, '1001', 1, 9),
(2, '1002', 1, 10),
(3, '1003', 1, 11),
(4, '1004', 1, 12),
(5, '1005', 1, 13),
(6, '1006', 1, 14),
(7, '1007', 1, 15),
(8, '1008', 1, 16),
(9, '1009', 1, 17),
(10, '1010', 1, 18),
(11, '1011', 1, 19),
(12, '1012', 1, 20),
(13, '1013', 1, 21),
(14, '1014', 1, 22),
(15, '1016', 1, 23),
(16, '1015', 1, 24),
(17, '1017', 1, 25),
(18, '1018', 1, 26);

-- --------------------------------------------------------

--
-- Table structure for table `school_studentunitenrollment`
--

CREATE TABLE `school_studentunitenrollment` (
  `id` bigint(20) NOT NULL,
  `semester_id` bigint(20) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  `unit_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_studentunitenrollment`
--

INSERT INTO `school_studentunitenrollment` (`id`, `semester_id`, `student_id`, `unit_id`) VALUES
(10, 2, 1, 3),
(11, 2, 1, 4),
(6, 1, 2, 1),
(7, 1, 2, 2),
(8, 1, 3, 1),
(9, 1, 3, 2),
(12, 1, 4, 1),
(13, 1, 4, 2),
(20, 2, 5, 3),
(21, 2, 5, 4),
(18, 2, 6, 3),
(19, 2, 6, 4),
(16, 2, 7, 3),
(17, 2, 7, 4),
(14, 2, 8, 3),
(15, 2, 8, 4),
(22, 2, 9, 3),
(23, 2, 9, 4),
(24, 3, 10, 5),
(25, 3, 10, 6),
(26, 3, 11, 5),
(27, 3, 11, 6),
(28, 3, 12, 5),
(29, 3, 12, 6),
(30, 3, 13, 5),
(31, 3, 13, 6),
(32, 3, 14, 5),
(33, 3, 14, 6),
(34, 3, 15, 5),
(35, 3, 15, 6),
(36, 3, 16, 5),
(37, 3, 16, 6),
(38, 3, 17, 5),
(39, 3, 17, 6),
(40, 3, 18, 5),
(41, 3, 18, 6);

-- --------------------------------------------------------

--
-- Table structure for table `school_timeslot`
--

CREATE TABLE `school_timeslot` (
  `id` bigint(20) NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `is_available` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_timeslot`
--

INSERT INTO `school_timeslot` (`id`, `start_time`, `end_time`, `is_available`) VALUES
(1, '08:00:00.000000', '10:00:00.000000', 1),
(2, '10:30:00.000000', '12:30:00.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `school_unit`
--

CREATE TABLE `school_unit` (
  `id` bigint(20) NOT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `faculty_id` bigint(20) NOT NULL,
  `lecturer_id` bigint(20) DEFAULT NULL,
  `online_hours` int(11) NOT NULL,
  `physical_hours` int(11) NOT NULL,
  `total_hours` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `school_unit`
--

INSERT INTO `school_unit` (`id`, `code`, `name`, `description`, `faculty_id`, `lecturer_id`, `online_hours`, `physical_hours`, `total_hours`) VALUES
(1, 'BBIT106', 'Introduction to Programming', 'Computer programming or coding is the composition of sequences of instructions, called programs, that computers can follow to perform tasks. It involves designing and implementing algorithms, step-by-step', 1, 7, 0, 2, 2),
(2, 'BBIT101', 'Database Management Systems', 'what is db.........', 1, 5, 1, 2, 3),
(3, 'BBIT102', 'Information Systems', 'what is Info..............', 1, 7, 2, 2, 4),
(4, 'BBIT103', '.	Computer Networks', 'o	Basics of computer networks, network protocols, and infrastructure design and implementation.', 1, 6, 0, 2, 2),
(5, 'BBIT104', 'Business Statistics', 'o	Applying statistical methods to solve business problems and analyze data.', 1, 5, 1, 2, 3),
(6, 'BBIT105', 'System Analysis and Design', 'o	Techniques for analyzing business requirements and designing IT systems to meet those needs.', 1, 4, 2, 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser`
--

CREATE TABLE `users_customuser` (
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `role` varchar(10) NOT NULL,
  `faculty_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users_customuser`
--

INSERT INTO `users_customuser` (`last_login`, `is_superuser`, `id`, `password`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `role`, `faculty_id`) VALUES
('2025-01-27 18:49:06.054499', 1, 1, 'pbkdf2_sha256$870000$M9lMT3iRkDFIH7Inba667Y$CQj4Afc3FPFYM63pPdrfL/7LzQumZDk8oKy9z0PLEiA=', '112721', 'Kathembo', 'Tsongo', 'dieudonnetsongo@gmail.com', 1, 1, '2025-01-21 07:17:30.862946', '', '', NULL),
(NULL, 0, 2, 'pbkdf2_sha256$870000$BxoJAUQlV61t1ZE7VdKrtC$lwYRBpLsdyfmvTARG90o0xV9HlJ56WZhrDH2FIbVJaE=', 'dieudonne', 'Dieudonne', 'Katsodieu', 'dieudonne@gmail.com', 0, 1, '2025-01-21 07:21:51.640991', '0758886411', 'lecturer', NULL),
(NULL, 0, 3, 'pbkdf2_sha256$870000$6Na2TBOsnS8MYXMRxqX7PU$Cebi12qp22nf5JYsYtZG3eFDJBfj2xqzPYsd2Gdu1D8=', 'claire', 'Claire', 'Kahindo', 'clair@gmail.com', 0, 1, '2025-01-21 09:47:32.363504', '075888641', 'lecturer', NULL),
(NULL, 0, 4, 'pbkdf2_sha256$870000$IcFJrAX1U2xgpqpH67Ykx7$TCGGAyuH5AuQH0pLFJRUzF5DdXa5OaJ+Xln2QNiw1sc=', '101001', 'Musiva', 'Keli', 'nusiva@gmail.com', 0, 1, '2025-01-22 02:39:48.130780', '07558987745', 'lecturer', NULL),
(NULL, 0, 5, 'pbkdf2_sha256$870000$u8N4Pdyk9G8JYGEXPEKbCf$8tJUErxwnqShjyhvx2Vs+OS2IuIZJDTbbiOcYEERb+0=', '101002', 'Catherine', 'Ndenya', 'cate@gmail.com', 0, 1, '2025-01-22 02:40:50.442938', '0758886418', 'lecturer', NULL),
(NULL, 0, 6, 'pbkdf2_sha256$870000$w7RsgdZwdwdICeEipoIYz6$WtH2K15z2Rgj6gd5jwLhiAuSuAcAO16PVfEnSJV+7WQ=', '101003', 'Muhindo', 'Syapa', 'Muhindo@gmail.com', 0, 1, '2025-01-22 02:42:14.953436', '0758886410', 'lecturer', NULL),
(NULL, 0, 7, 'pbkdf2_sha256$870000$L31mF0MOVchskNXTNKP1un$UGlRYGsEHwd8Hvu8z+9hhCvQCApXF5vY4qKZ9s17Gkk=', '101004', 'Kihembo', 'Dieumerci', 'hembo@gmail.com', 0, 1, '2025-01-22 02:43:18.626735', '0755898775', 'lecturer', NULL),
(NULL, 0, 8, 'pbkdf2_sha256$870000$NQqlHkwPRoFBHnIlUZyfRo$JwJiA5VwgfWFZH8dwmnJYlxnovkXE3+UUph85uC62ak=', '101005', 'Kathembo', 'Katsodieu', 'kathembo@gmail.com', 0, 1, '2025-01-22 02:47:11.737834', '075888648', 'lecturer', NULL),
(NULL, 0, 9, 'pbkdf2_sha256$870000$BOA2xKqvKEumDy7Ko17PAH$CBd2yZLz/z/V2ydaVcDq2bLIMVi0TjIAOVkg+6KdCdI=', 'Kathembo', 'Kathembo', 'Tsongo', 'testkathembo@gmail.com', 0, 1, '2025-01-22 07:52:43.935629', '0055898745', 'student', NULL),
(NULL, 0, 10, 'pbkdf2_sha256$870000$E84GstINkgtNe6TI1tlV7W$yNtnBcH5/mj27MvNISsdJW2NTqArOQwtbhaFnNCjebs=', 'Donne', 'Dieudonne', 'Katso', 'testkathemb@gmail.com', 0, 1, '2025-01-22 08:50:59.488305', '075589745', 'student', NULL),
(NULL, 0, 11, 'pbkdf2_sha256$870000$dRi6Fso99arKZ2xcnI8bKx$t5yvuCbnfjgEeOEiWF0UjMWEQMLjgzFFkX5vUSu3LNs=', 'clairo', 'Claire', 'Lilian', 'testkathem@gmail.com', 0, 1, '2025-01-22 09:13:25.168428', '07558987', 'student', NULL),
(NULL, 0, 12, 'pbkdf2_sha256$870000$R4BTAzHrP7oXkHcRQyb2FP$rsBAaT6Lsl9TMz46SdYPNHvqIj2JuBS8WxenNPSDJeA=', 'Dieud', 'Dido', 'Kathungu', 'testkthem@gmail.com', 0, 1, '2025-01-22 12:19:42.430712', '0755898745', 'student', NULL),
(NULL, 0, 13, 'pbkdf2_sha256$870000$wr76iMvMLWGxEPdqc6EJos$JiU6gyyrMKhg2n2imumDLSAW9+1jNBRpmt+IkC8JdP8=', 'Celi', 'Celile', 'Kahhh', 'testthembo@gmail.com', 0, 1, '2025-01-22 12:22:39.646801', '00558985', 'student', NULL),
(NULL, 0, 14, 'pbkdf2_sha256$870000$y1y89k6bhprNTIquMy1ArL$ooWYr1Mz25r2Lu8uV1HviMEe+j1+oGnytHVxon4Ky+s=', 'clarice', 'Kathembo', 'Kathu', 'clarisse@gmail.com', 0, 1, '2025-01-22 12:23:42.352516', '075888640', 'student', NULL),
(NULL, 0, 15, 'pbkdf2_sha256$870000$G8vwr46df7lnB703yvcMds$r3l2xtuuYiqk7nyCMPEi8ApANuZ4psSYXnR8RufdGuQ=', 'Norb', 'Kathe', 'Kahhingooo', 'tembo@gmail.com', 0, 1, '2025-01-22 12:24:46.753048', '07588418', 'student', NULL),
(NULL, 0, 16, 'pbkdf2_sha256$870000$krJWG8B2JgNAOpmWSl2nyV$RLVc74ovexrrKCXd98Cxm8rgn91fjDFudx/2t2m0NQI=', 'Keyenb', 'Kiyengo', 'Goretti', 'Kmbo@gmail.com', 0, 1, '2025-01-22 12:26:42.386000', '0755898', 'student', NULL),
(NULL, 0, 17, 'pbkdf2_sha256$870000$5sE4GnRjQ0llvgtixjTLHM$L1qHKOIddkx0ungvJmzkdhICyIaCVIcq3d9opBLKhz0=', 'Mathe', 'Mathe', 'Syapa', 'mathebo@gmail.com', 0, 1, '2025-01-22 12:33:54.385778', '0758886444', 'student', NULL),
(NULL, 0, 18, 'pbkdf2_sha256$870000$bi2tqg8HCyhtqji54UHf19$f6KhfHG8HM5P2nvySRDAHjyJqZFDY+AxQT1tF97mmKU=', 'Emmanuel', 'Emmanuel', 'Kahindo', 'emman@gmail.com', 0, 1, '2025-01-22 12:37:00.830059', '075587745', 'student', NULL),
(NULL, 0, 19, 'pbkdf2_sha256$870000$1JkFBQUbRgQBWlAK0zsd7Q$isrS/vfa283IdyOEFI2CyMVd8V+qSxqMOjs89ThAD2g=', 'Emm', 'Kahi', 'EMm', 'emmbo@gmail.com', 0, 1, '2025-01-22 12:39:12.301363', '0755898701', 'student', NULL),
(NULL, 0, 20, 'pbkdf2_sha256$870000$Ww0ghG4EFMu2A5jJi37aES$rTkQHYaS68Jwwu8HAg0e3jiGwaHxzEzLLw49PvHW9Z8=', 'kyahwere', 'KyahwereK', 'Jery', 'kyahwere@gmail.com', 0, 1, '2025-01-22 12:40:55.214473', '0755845', 'student', NULL),
(NULL, 0, 21, 'pbkdf2_sha256$870000$8GGUldmfWGPkQ4ytWkoVih$kN1og6nTXjEb9cFIs9BwCPCUAv1HEx8Gv9OZAgAhP2M=', 'Jeannette', 'Jeanette', 'Kihem', 'jean@gmail.com', 0, 1, '2025-01-22 12:43:02.223387', '0755897745', 'student', NULL),
(NULL, 0, 22, 'pbkdf2_sha256$870000$5V4PaVMjbIsUrogPUrRemy$WTXbbYe+VACr+UdujUY9AjSQ+CHcnKr3CSYbsjWe9Ek=', 'Glory', 'Glory', 'Math', 'Golo@gmail.com', 0, 1, '2025-01-22 12:44:00.020098', '058987745', 'student', NULL),
(NULL, 0, 23, 'pbkdf2_sha256$870000$vQ4uCN35a8FtN5oX7LSler$BnXegGtGrSOpGjGmjRg0BA1vB765EJbjzIRzKSK1UJ8=', 'Mbusa', 'Mbusa', 'Katero', 'mbusa@gmail.com', 0, 1, '2025-01-23 02:32:07.280483', '075987745', 'student', NULL),
(NULL, 0, 24, 'pbkdf2_sha256$870000$KxPEqRNIxkDo3LNNCtC1MQ$FietSMQqgPonLwZRjqAXAgj/UjLMq2udVVJMczhNltk=', 'Katemb', 'Katembe', 'Kiso', 'tesathembo@gmail.com', 0, 1, '2025-01-23 02:33:19.796321', '0755898700', 'student', NULL),
(NULL, 0, 25, 'pbkdf2_sha256$870000$BIBH3YgCVU3G5rFg22RXfA$mOaSrEaD1Q24dLnORwtp5hOZufmzyCaIYGxGh4TI6xw=', 'Kiroooh', 'Kirembo', 'Hugu', 'Kirembo@gmail.com', 0, 1, '2025-01-23 02:39:02.921373', '0755877987', 'student', NULL),
(NULL, 0, 26, 'pbkdf2_sha256$870000$7C8ZH1XXjc5yMlZh0CvPhE$OA0LCNlr3N+/dB1HBfGO441skdr7vwVzVLIM8dLLSx0=', 'Musu', 'Musubai', 'Muhi', 'testkat@gmail.com', 0, 1, '2025-01-23 06:42:57.825936', '0155898745', 'student', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_groups`
--

CREATE TABLE `users_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_user_permissions`
--

CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `school_classroom`
--
ALTER TABLE `school_classroom`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `school_classtimetable`
--
ALTER TABLE `school_classtimetable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `school_classtimetable_unit_id_5ca91a95_fk_school_unit_id` (`unit_id`);

--
-- Indexes for table `school_faculty`
--
ALTER TABLE `school_faculty`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `school_lecturer`
--
ALTER TABLE `school_lecturer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `school_lecturer_faculty_id_57dec89d_fk_school_faculty_id` (`faculty_id`);

--
-- Indexes for table `school_semester`
--
ALTER TABLE `school_semester`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `school_student`
--
ALTER TABLE `school_student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `school_student_faculty_id_b8c3cac8_fk_school_faculty_id` (`faculty_id`);

--
-- Indexes for table `school_studentunitenrollment`
--
ALTER TABLE `school_studentunitenrollment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `school_studentunitenroll_student_id_unit_id_semes_214c63c2_uniq` (`student_id`,`unit_id`,`semester_id`),
  ADD KEY `school_studentuniten_semester_id_5cdff784_fk_school_se` (`semester_id`),
  ADD KEY `school_studentunitenrollment_unit_id_b18dfd09_fk_school_unit_id` (`unit_id`);

--
-- Indexes for table `school_timeslot`
--
ALTER TABLE `school_timeslot`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `school_unit`
--
ALTER TABLE `school_unit`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `school_unit_faculty_id_52a821ab_fk_school_faculty_id` (`faculty_id`),
  ADD KEY `school_unit_lecturer_id_182eae9a_fk_school_lecturer_id` (`lecturer_id`);

--
-- Indexes for table `users_customuser`
--
ALTER TABLE `users_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=242;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `school_classroom`
--
ALTER TABLE `school_classroom`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `school_classtimetable`
--
ALTER TABLE `school_classtimetable`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=733;

--
-- AUTO_INCREMENT for table `school_faculty`
--
ALTER TABLE `school_faculty`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `school_lecturer`
--
ALTER TABLE `school_lecturer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `school_semester`
--
ALTER TABLE `school_semester`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `school_student`
--
ALTER TABLE `school_student`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `school_studentunitenrollment`
--
ALTER TABLE `school_studentunitenrollment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `school_timeslot`
--
ALTER TABLE `school_timeslot`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `school_unit`
--
ALTER TABLE `school_unit`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users_customuser`
--
ALTER TABLE `users_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `school_classtimetable`
--
ALTER TABLE `school_classtimetable`
  ADD CONSTRAINT `school_classtimetable_unit_id_5ca91a95_fk_school_unit_id` FOREIGN KEY (`unit_id`) REFERENCES `school_unit` (`id`);

--
-- Constraints for table `school_lecturer`
--
ALTER TABLE `school_lecturer`
  ADD CONSTRAINT `school_lecturer_faculty_id_57dec89d_fk_school_faculty_id` FOREIGN KEY (`faculty_id`) REFERENCES `school_faculty` (`id`),
  ADD CONSTRAINT `school_lecturer_user_id_b39c4f64_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `school_student`
--
ALTER TABLE `school_student`
  ADD CONSTRAINT `school_student_faculty_id_b8c3cac8_fk_school_faculty_id` FOREIGN KEY (`faculty_id`) REFERENCES `school_faculty` (`id`),
  ADD CONSTRAINT `school_student_user_id_d99a8e54_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `school_studentunitenrollment`
--
ALTER TABLE `school_studentunitenrollment`
  ADD CONSTRAINT `school_studentuniten_semester_id_5cdff784_fk_school_se` FOREIGN KEY (`semester_id`) REFERENCES `school_semester` (`id`),
  ADD CONSTRAINT `school_studentuniten_student_id_51d74beb_fk_school_st` FOREIGN KEY (`student_id`) REFERENCES `school_student` (`id`),
  ADD CONSTRAINT `school_studentunitenrollment_unit_id_b18dfd09_fk_school_unit_id` FOREIGN KEY (`unit_id`) REFERENCES `school_unit` (`id`);

--
-- Constraints for table `school_unit`
--
ALTER TABLE `school_unit`
  ADD CONSTRAINT `school_unit_faculty_id_52a821ab_fk_school_faculty_id` FOREIGN KEY (`faculty_id`) REFERENCES `school_faculty` (`id`),
  ADD CONSTRAINT `school_unit_lecturer_id_182eae9a_fk_school_lecturer_id` FOREIGN KEY (`lecturer_id`) REFERENCES `school_lecturer` (`id`);

--
-- Constraints for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
