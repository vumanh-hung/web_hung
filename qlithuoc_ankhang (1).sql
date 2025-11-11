-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 05:47 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlithuoc_ankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `categories`
--

INSERT INTO `categories` (`category_id`, `name`, `description`, `created_at`) VALUES
(1, 'Hot Sale', NULL, '2025-11-04 03:22:06'),
(2, 'Thuốc - Cập nhật', 'Danh mục chứa các loại thuốc kê đơn và OTC.', '2025-11-04 03:22:06'),
(3, 'Thực phẩm chức năng', NULL, '2025-11-04 03:22:06'),
(4, 'Thiết bị, dụng cụ y tế', NULL, '2025-11-04 03:22:06'),
(5, 'Dược mỹ phẩm', NULL, '2025-11-04 03:22:06'),
(6, 'Chăm sóc cá nhân', NULL, '2025-11-04 03:22:06'),
(7, 'cham soc nguoi gia', NULL, '2025-11-04 03:22:06');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount_percent` int(11) DEFAULT 0,
  `stock` int(11) DEFAULT 0,
  `image_url` varchar(255) DEFAULT NULL,
  `old_price` decimal(10,2) DEFAULT NULL,
  `slots_used` int(11) DEFAULT 0,
  `slots_total` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `products`
--

INSERT INTO `products` (`product_id`, `category_id`, `name`, `price`, `discount_percent`, `stock`, `image_url`, `old_price`, `slots_used`, `slots_total`, `created_at`) VALUES
(5, 5, 'Nước tẩy trang Bioderma Sensibio H2O', 398750.00, 25, 20, 'bioderma.jpg', 535000.00, 20, 20, '2025-11-04 03:22:18'),
(6, 6, 'Tăm chỉ nha khoa Okamura 734503', 18000.00, 18, 20, 'okamura.jpg', 22000.00, 20, 20, '2025-11-04 03:22:18'),
(7, 6, 'Nước súc miệng Listerine Cool Mint', 81000.00, 52, 20, 'listerine.jpg', 169000.00, 20, 20, '2025-11-04 03:22:18'),
(8, 6, 'Nước Yến Collagen Green Bird Nutrient', 22500.00, 25, 60, 'greenbird.jpg', 30000.00, 60, 60, '2025-11-04 03:22:18');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Chỉ mục cho bảng `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `category_id` (`category_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
