-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2022 at 06:01 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `matcherdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_candidate`
--

CREATE TABLE `api_candidate` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `skills` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `api_candidate`
--

INSERT INTO `api_candidate` (`id`, `title`, `name`, `skills`) VALUES
(1, 'Software Engineer', 'Almog Lev', '[\n    1,\n    4,\n    5\n]'),
(2, 'Software Developer', 'Moshe Cohen', '[\n    1,\n    4\n]'),
(3, 'Marketing Specialist', 'Dana Levy', '[\n    3,\n    5\n]'),
(4, 'Software Developer', 'Ben Israeli', '[\n    3\n]'),
(5, 'Marketing Specialist', 'Or Gal', '[]'),
(6, 'VP R&D', 'Sarah Dan', '[\n    1,\n    2,\n    3,\n    4,\n    5\n]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_candidate`
--
ALTER TABLE `api_candidate`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `api_candidate`
--
ALTER TABLE `api_candidate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
