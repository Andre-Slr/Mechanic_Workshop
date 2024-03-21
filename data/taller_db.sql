-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-03-2024 a las 09:16:46
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `car_plate` varchar(25) NOT NULL,
  `client_ID` int(11) NOT NULL,
  `brand` varchar(25) NOT NULL,
  `model` varchar(25) NOT NULL,
  `date_enter` date NOT NULL,
  `time_enter` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cars`
--

INSERT INTO `cars` (`id`, `car_plate`, `client_ID`, `brand`, `model`, `date_enter`, `time_enter`) VALUES
(1, 'JJB-03-02', 5, 'Toyota', 'Corolla', '2024-03-15', '15:30:00'),
(2, 'BC-030-A7', 8, 'Honda', 'Civic', '2024-01-25', '13:20:00'),
(3, 'KLM-42-87', 12, 'Ford', 'Focus', '2024-03-08', '12:00:00'),
(4, 'NZZ-91-24', 15, 'Chevrolet', 'Cruze', '2024-01-30', '09:30:00'),
(5, 'LOP-78-50', 16, 'Volkswagen', 'Jetta', '2024-02-12', '11:00:00'),
(6, 'XVC-29-16', 11, 'Hyundai', 'Elantra', '2024-01-17', '10:30:00'),
(7, 'HJK-05-73', 4, 'Nissan', 'Sentra', '2024-03-03', '14:00:00'),
(8, 'WER-62-34', 8, 'Mazda', '3', '2024-01-25', '13:20:00'),
(9, 'QWE-39-05', 7, 'Kia', 'Forte', '2024-04-18', '11:45:00'),
(10, 'TYU-14-28', 2, 'Subaru', 'Impreza', '2024-02-05', '10:15:00'),
(11, 'UIO-87-09', 1, 'Mercedes-Benz', 'C-Class', '2024-01-10', '08:30:00'),
(12, 'PLL-20-47', 6, 'BMW', '3 Series', '2024-04-02', '09:00:00'),
(13, 'ZXC-54-61', 10, 'Audi', 'A4', '2024-04-05', '08:00:00'),
(14, 'NBV-36-82', 13, 'Lexus', 'IS', '2024-03-20', '14:45:00'),
(15, 'QAZ-73-01', 3, 'Infiniti', 'Q50', '2024-02-20', '12:45:00'),
(16, 'WSD-12-55', 9, 'Tesla', 'Model 3', '2024-02-08', '16:10:00'),
(17, 'EDC-88-19', 17, 'Porsche', '911', '2024-03-05', '13:40:00'),
(18, 'RFV-09-44', 14, 'Jaguar', 'XE', '2024-04-10', '16:20:00'),
(19, 'VFR-25-96', 18, 'Land Rover', 'Range Rover Evoque', '2024-04-22', '15:15:00'),
(20, 'DCB-48-73', 20, 'Jeep', 'Wrangler', '2024-04-01', '10:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clients`
--

CREATE TABLE `clients` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `lastname` varchar(25) NOT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_enter` date NOT NULL,
  `time_enter` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clients`
--

INSERT INTO `clients` (`id`, `name`, `lastname`, `phone`, `user_id`, `date_enter`, `time_enter`) VALUES
(1, 'Juan', 'García López', '3356487522', 1, '2024-01-10', '08:30:00'),
(2, 'María', 'Fernández Rodríguez', '3357649281', 2, '2024-02-05', '10:15:00'),
(3, 'José', 'Martínez Pérez', '3358891254', 3, '2024-02-20', '12:45:00'),
(4, 'Laura', 'Hernández Gómez', '3359732648', 4, '2024-03-03', '14:00:00'),
(5, 'Carlos', 'González Sánchez', '3360321475', 5, '2024-03-15', '15:30:00'),
(6, 'Ana', 'Rodríguez Martínez', '3361789356', 2, '2024-04-02', '09:00:00'),
(7, 'Francisco', 'López Torres', '3362938475', 2, '2024-04-18', '11:45:00'),
(8, 'Andrea', 'Díaz Ruiz', '3364175893', 3, '2024-01-25', '13:20:00'),
(9, 'Patricia', 'Ramírez Vázquez', '3365837291', 1, '2024-02-08', '16:10:00'),
(10, 'Miguel', 'Sánchez Pérez', '3366978153', 4, '2024-04-05', '08:00:00'),
(11, 'Susana', 'Vázquez López', '3367123849', 5, '2024-01-17', '10:30:00'),
(12, 'Luis', 'Martínez García', '3368264912', 5, '2024-03-08', '12:00:00'),
(13, 'Rosa', 'Pérez Hernández', '3369412378', 1, '2024-03-20', '14:45:00'),
(14, 'Javier', 'Gómez Rodríguez', '3370539267', 3, '2024-04-10', '16:20:00'),
(15, 'Carmen', 'Torres Martínez', '3371673826', 4, '2024-01-30', '09:30:00'),
(16, 'Daniel', 'Ruiz González', '3372819473', 2, '2024-02-12', '11:00:00'),
(17, 'Mariana', 'López Sánchez', '3373965182', 4, '2024-03-05', '13:40:00'),
(18, 'Jorge', 'Ramírez García', '3374125896', 5, '2024-04-22', '15:15:00'),
(19, 'Alejandra', 'Flores Pérez', '3375281946', 3, '2024-01-14', '08:45:00'),
(20, 'David', 'Gutiérrez Rodríguez', '3376439815', 1, '2024-04-01', '10:00:00'),
(21, 'Miguel', 'Arias Frías', '3372240500', 1, '2024-03-19', '14:28:02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `det_repairs`
--

CREATE TABLE `det_repairs` (
  `folio_detail` varchar(60) DEFAULT NULL,
  `folio` int(11) NOT NULL,
  `part_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `det_repairs`
--

INSERT INTO `det_repairs` (`folio_detail`, `folio`, `part_id`, `amount`) VALUES
('Batería dañada', 1, 9, 1),
('No funcionan los embragues', 2, 19, 2),
('Falta de aceite de motor', 3, 5, 1),
('Frenos en mal estado', 4, 15, 3),
('Falta de catalizadores', 5, 25, 1),
('Amortiguadores dañados', 6, 6, 2),
('Batería dañada', 7, 9, 1),
('Bujías dañadas', 8, 2, 3),
('Golpeteo en las ruedas delanteras al girar', 9, 21, 1),
('Dificultades para cambiar la marcha, cambios irregulares', 10, 19, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parts`
--

CREATE TABLE `parts` (
  `id` int(11) NOT NULL,
  `description` varchar(64) NOT NULL,
  `stock` int(11) NOT NULL,
  `date_enter` date NOT NULL,
  `time_enter` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `parts`
--

INSERT INTO `parts` (`id`, `description`, `stock`, `date_enter`, `time_enter`) VALUES
(1, 'Llantas', 28, '2024-01-05', '08:00:00'),
(2, 'Bujías', 10, '2024-01-10', '09:30:00'),
(3, 'Filtros de Aceite', 20, '2024-01-15', '10:45:00'),
(4, 'Pastillas de Freno', 12, '2024-01-20', '11:15:00'),
(5, 'Aceite de Motor', 38, '2024-01-25', '13:00:00'),
(6, 'Amortiguadores', 7, '2024-02-05', '14:30:00'),
(7, 'Discos de Freno', 10, '2024-02-10', '15:45:00'),
(8, 'Filtros de Aire', 18, '2024-02-15', '16:00:00'),
(9, 'Baterías', 6, '2024-02-20', '08:30:00'),
(10, 'Correas de Distribución', 14, '2024-02-25', '09:45:00'),
(11, 'Limpiaparabrisas', 30, '2024-03-05', '11:00:00'),
(12, 'Refrigerante', 25, '2024-03-10', '12:15:00'),
(13, 'Termostatos', 6, '2024-03-15', '13:30:00'),
(14, 'Filtros de Combustible', 20, '2024-03-20', '14:45:00'),
(15, 'Escobillas de Freno', 5, '2024-03-25', '15:00:00'),
(16, 'Radiadores', 10, '2024-04-05', '08:00:00'),
(17, 'Aceite de Transmisión', 15, '2024-04-10', '09:15:00'),
(18, 'Bombillas', 40, '2024-04-15', '10:30:00'),
(19, 'Embragues', 9, '2024-04-20', '11:45:00'),
(20, 'Barras Estabilizadoras', 8, '2024-04-25', '13:00:00'),
(21, 'Juntas Homocinéticas', 14, '2024-05-05', '14:15:00'),
(22, 'Silenblocks', 10, '2024-05-10', '15:30:00'),
(23, 'Terminales de Dirección', 18, '2024-05-15', '16:45:00'),
(24, 'Sensores de Oxígeno', 6, '2024-05-20', '08:30:00'),
(25, 'Catalizadores', 8, '2024-05-25', '09:45:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `repairs`
--

CREATE TABLE `repairs` (
  `folio` int(11) NOT NULL,
  `car_id` int(11) NOT NULL,
  `date_enter` date NOT NULL,
  `time_enter` varchar(25) NOT NULL,
  `date_out` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `repairs`
--

INSERT INTO `repairs` (`folio`, `car_id`, `date_enter`, `time_enter`, `date_out`) VALUES
(1, 2, '2024-01-02', '18:32:27', '2024-01-03'),
(2, 20, '2024-02-06', '23:50:42', '2024-02-08'),
(3, 17, '2024-01-02', '23:51:10', '2024-01-02'),
(4, 7, '2024-01-24', '23:51:55', '2024-01-31'),
(5, 13, '2024-02-08', '23:52:31', '2024-02-10'),
(6, 6, '2024-03-01', '23:52:55', '2024-03-03'),
(7, 16, '2024-03-05', '23:53:21', '2024-03-06'),
(8, 19, '2024-03-13', '23:53:52', '2024-03-13'),
(9, 9, '2024-03-05', '01:44:11', '2024-03-06'),
(10, 2, '2024-02-29', '01:46:38', '2024-03-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `profile` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `profile`) VALUES
(1, 'André Solórzano', 'andre_slr', 'Pw123', 'Admin'),
(2, 'María Gutiérrez', 'maria_gtz', 'Pass456', 'Secretary'),
(3, 'Luis Martínez', 'luis_mtz', 'Secure789', 'Mechanic'),
(4, 'Laura Sánchez', 'laura_schz', 'Secret123', 'Secretary'),
(5, 'Carlos Rodríguez', 'carlos_rdrgz', 'Pwd567', 'Mechanic');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_ID` (`client_ID`);

--
-- Indices de la tabla `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indices de la tabla `det_repairs`
--
ALTER TABLE `det_repairs`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `part_id` (`part_id`);

--
-- Indices de la tabla `parts`
--
ALTER TABLE `parts`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `repairs`
--
ALTER TABLE `repairs`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `car_id` (`car_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `parts`
--
ALTER TABLE `parts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `repairs`
--
ALTER TABLE `repairs`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cars`
--
ALTER TABLE `cars`
  ADD CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`client_ID`) REFERENCES `clients` (`id`);

--
-- Filtros para la tabla `clients`
--
ALTER TABLE `clients`
  ADD CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Filtros para la tabla `det_repairs`
--
ALTER TABLE `det_repairs`
  ADD CONSTRAINT `det_repairs_ibfk_1` FOREIGN KEY (`folio`) REFERENCES `repairs` (`folio`),
  ADD CONSTRAINT `det_repairs_ibfk_2` FOREIGN KEY (`part_id`) REFERENCES `parts` (`id`);

--
-- Filtros para la tabla `repairs`
--
ALTER TABLE `repairs`
  ADD CONSTRAINT `repairs_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
