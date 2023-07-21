-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2022 at 07:45 PM
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
-- Database: `bbmsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `schedule_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `number_of_seats` int(2) NOT NULL,
  `fare_amount` int(11) NOT NULL,
  `total_amount` int(11) NOT NULL,
  `date_of_booking` date NOT NULL,
  `booking_status` varchar(100) NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `schedule_id`, `customer_id`, `number_of_seats`, `fare_amount`, `total_amount`, `date_of_booking`, `booking_status`, `users_id`) VALUES
(315141, 68421616, 16146161, 14, 451, 624, '2022-11-29', 'Not Booked', 1654864);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `bus_id` int(11) NOT NULL,
  `bus_number` varchar(15) NOT NULL,
  `bus_plate_number` varchar(15) NOT NULL,
  `bus_type` int(1) NOT NULL,
  `capacity` int(3) NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`bus_id`, `bus_number`, `bus_plate_number`, `bus_type`, `capacity`, `users_id`) VALUES
(794154, '124512', 'KL124123', 2, 4, 1654864),
(1546461, '6431431', 'KA13214', 2, 5, 3446731);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `customer_contact` varchar(15) NOT NULL,
  `customer_email` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `cust_password` varchar(30) NOT NULL,
  `account_status` varchar(100) NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_name`, `customer_contact`, `customer_email`, `username`, `cust_password`, `account_status`, `users_id`) VALUES
(16146161, 'aevev', '16503216', 'afwawf@', '131616', 'asfef213', '0', 3446731),
(681704010, 'Darshi', '41646106', 'sdfbsegf@', 'Dargs', 'WR554asd', '4', 3446731);

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(11) NOT NULL,
  `driver_name` varchar(50) NOT NULL,
  `driver_contact` varchar(15) NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`driver_id`, `driver_name`, `driver_contact`, `users_id`) VALUES
(151604, 'Faroes', '3154123', 3446731);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `amount_paid` int(11) NOT NULL,
  `payment_date` date NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `booking_id`, `amount_paid`, `payment_date`, `users_id`) VALUES
(241416, 315141, 789, '2022-11-30', 1654864),
(4651647, 315141, 782, '2022-11-29', 4754812);

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL,
  `bus_id` int(11) NOT NULL,
  `driver_id` int(11) NOT NULL,
  `starting_point` varchar(30) NOT NULL,
  `destination` varchar(30) NOT NULL,
  `schedule_date` date NOT NULL,
  `departure_time` varchar(100) NOT NULL,
  `estimated_arrival_time` varchar(100) NOT NULL,
  `fare_amount` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `users_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`schedule_id`, `bus_id`, `driver_id`, `starting_point`, `destination`, `schedule_date`, `departure_time`, `estimated_arrival_time`, `fare_amount`, `remarks`, `users_id`) VALUES
(68421616, 794154, 151604, 'awwaeq', 'awqe', '2022-11-29', '02:30:00', '07:00:00', 457, 'WRCEWVRVRA', 134416);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `users_id` int(11) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `contact_no` varchar(15) NOT NULL,
  `email_address` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `userpassword` varchar(30) NOT NULL,
  `account_category` int(1) NOT NULL,
  `account_status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`users_id`, `full_name`, `contact_no`, `email_address`, `username`, `userpassword`, `account_category`, `account_status`) VALUES
(134416, 'ewsfcvwe', '26510654.0', 'aefcqw@', 'esrgvwe', 'cawerge2', 4, 2),
(1654864, 'Yash', '464162521.0', 'yash@kbf', 'Yashas', 'Yasgas', 1, 5),
(3446731, 'florid', '13731367.0', 'florid#rb', 'Flroids', 'asrwrac', 1, 0),
(4754812, 'Darshan', '47686134.0', 'darsh@gse', 'darshans', 'dfjgajwdgjb', 2, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `schedule_id` (`schedule_id`,`customer_id`,`users_id`),
  ADD KEY `user_id` (`users_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`bus_id`),
  ADD KEY `user_id` (`users_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD KEY `user_id` (`users_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`),
  ADD KEY `user_id` (`users_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `booking_id` (`booking_id`,`users_id`),
  ADD KEY `user_id` (`users_id`);

--
-- Indexes for table `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`schedule_id`),
  ADD KEY `bus_id` (`bus_id`,`driver_id`,`users_id`),
  ADD KEY `user_id` (`users_id`),
  ADD KEY `driver_id` (`driver_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`users_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`schedule_id`) REFERENCES `schedule` (`schedule_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `driver`
--
ALTER TABLE `driver`
  ADD CONSTRAINT `driver_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `schedule`
--
ALTER TABLE `schedule`
  ADD CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`users_id`) REFERENCES `user` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `schedule_ibfk_2` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `schedule_ibfk_3` FOREIGN KEY (`bus_id`) REFERENCES `bus` (`bus_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
