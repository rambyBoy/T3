-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-10-2019 a las 06:14:02
-- Versión del servidor: 10.1.21-MariaDB
-- Versión de PHP: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyectotopico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autobuses`
--

CREATE TABLE `autobuses` (
  `Id` int(7) NOT NULL,
  `Modelo` varchar(100) NOT NULL,
  `Marca` varchar(100) NOT NULL,
  `Año` int(7) NOT NULL,
  `Precio` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `autobuses`
--

INSERT INTO `autobuses` (`Id`, `Modelo`, `Marca`, `Año`, `Precio`) VALUES
(1, 'ST45', 'Mercedez', 450000, 2010);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aviones`
--

CREATE TABLE `aviones` (
  `Id` int(7) NOT NULL,
  `Modelo` varchar(100) NOT NULL,
  `Marca` varchar(100) NOT NULL,
  `Año` int(10) NOT NULL,
  `Precio` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `aviones`
--

INSERT INTO `aviones` (`Id`, `Modelo`, `Marca`, `Año`, `Precio`) VALUES
(3, 'People', 'as', 123456, 6555),
(4, 'qwerty', 'qwerty', 213, 2015);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carros`
--

CREATE TABLE `carros` (
  `Id` int(7) NOT NULL,
  `Modelo` varchar(100) NOT NULL,
  `Marca` varchar(100) NOT NULL,
  `Año` int(10) NOT NULL,
  `Precio` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `carros`
--

INSERT INTO `carros` (`Id`, `Modelo`, `Marca`, `Año`, `Precio`) VALUES
(2, 'Modelo S', 'Tesla', 2156, 500000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `Id` int(11) NOT NULL,
  `categoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`Id`, `categoria`) VALUES
(1, 'Aviones'),
(2, 'Motos'),
(3, 'Carros'),
(4, 'Autobuses');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `motos`
--

CREATE TABLE `motos` (
  `Id` int(7) NOT NULL,
  `Modelo` varchar(200) NOT NULL,
  `Marca` varchar(200) NOT NULL,
  `Año` int(10) NOT NULL,
  `Precio` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `motos`
--

INSERT INTO `motos` (`Id`, `Modelo`, `Marca`, `Año`, `Precio`) VALUES
(2, 'People', 'Tesla', 2022, 500000),
(3, 'People', 'Susuki', 12000, 2015),
(4, 'Modelo L', 'Tesla', 450000, 2019);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `privilegios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `contraseña`, `email`, `privilegios`) VALUES
(10, 'Poncho', 'ZUmano', '$2b$12$cz1cf2HtDuUdnZoc3v65L.xEDxkoGuJDngzMR3tDof44JvU8ORT0O', 'ZUMAN@UAQ.COM', 3),
(11, 'Hugo Hiram', 'Villafuerte', '$2b$12$y1iG670H8aRVRWY/0CbXf.GeCLMJNoLzrCymCLXwrTi5xM4TWnsUa', 'hhav213@gmail.com', 2),
(14, 'Ramby', 'USD', '$2b$12$isWmHQD9gsXIvj64jQyDhenPAIusQo3NiTnc997fXe4GqkKthjFvW', 'ramby@gmail.com', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `id` int(11) NOT NULL,
  `modelo` varchar(255) NOT NULL,
  `marca` varchar(255) NOT NULL,
  `precio` varchar(255) NOT NULL,
  `año` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`id`, `modelo`, `marca`, `precio`, `año`) VALUES
(2, 'Jetta', 'Wagen', '25000', '2002'),
(3, 'Mustang', 'Ford', '30000', '2017'),
(7, 'Model S', 'Tesla', '120000', '2001'),
(9, 'Model S', 'Tesla', '120000', '2001'),
(10, 'Model S', 'Tesla', '120000', '2001'),
(11, 'Model S', 'Tesla', '120000', '2001'),
(12, 'Model S', 'Tesla', '120000', '2001'),
(16, 'Model T', 'Tesla', '120000', '2001');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autobuses`
--
ALTER TABLE `autobuses`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `aviones`
--
ALTER TABLE `aviones`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `motos`
--
ALTER TABLE `motos`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autobuses`
--
ALTER TABLE `autobuses`
  MODIFY `Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `aviones`
--
ALTER TABLE `aviones`
  MODIFY `Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `carros`
--
ALTER TABLE `carros`
  MODIFY `Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `motos`
--
ALTER TABLE `motos`
  MODIFY `Id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
