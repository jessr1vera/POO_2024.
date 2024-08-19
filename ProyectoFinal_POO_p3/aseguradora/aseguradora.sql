-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 15-08-2024 a las 17:44:17
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
-- Base de datos: `aseguradora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agente`
--

CREATE TABLE `agente` (
  `idAgente` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `idCliente` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`idCliente`, `nombre`, `direccion`, `telefono`, `correo`) VALUES
(1, 'jess', 'e', NULL, NULL),
(2, 'si', 'mi  casa', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE `pago` (
  `idPago` int(11) NOT NULL,
  `fechaPago` date DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `metodoPago` varchar(50) DEFAULT NULL,
  `idPoliza` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `poliza`
--

CREATE TABLE `poliza` (
  `numeroPoliza` int(11) NOT NULL,
  `fechaInicio` date DEFAULT NULL,
  `fechaFin` date DEFAULT NULL,
  `cobertura` varchar(255) DEFAULT NULL,
  `prima` decimal(10,2) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `idAgente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `siniestro`
--

CREATE TABLE `siniestro` (
  `idSiniestro` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `montoReclamo` decimal(10,2) DEFAULT NULL,
  `idPoliza` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE `vehiculo` (
  `idVehiculo` int(11) NOT NULL,
  `numeroPlaca` varchar(20) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `año` int(11) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `idPoliza` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculo`
--

INSERT INTO `vehiculo` (`idVehiculo`, `numeroPlaca`, `marca`, `modelo`, `año`, `tipo`, `idPoliza`) VALUES
(1, NULL, 'si', 'si', NULL, NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agente`
--
ALTER TABLE `agente`
  ADD PRIMARY KEY (`idAgente`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`idCliente`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`idPago`),
  ADD KEY `idPoliza` (`idPoliza`);

--
-- Indices de la tabla `poliza`
--
ALTER TABLE `poliza`
  ADD PRIMARY KEY (`numeroPoliza`),
  ADD KEY `idCliente` (`idCliente`),
  ADD KEY `idAgente` (`idAgente`);

--
-- Indices de la tabla `siniestro`
--
ALTER TABLE `siniestro`
  ADD PRIMARY KEY (`idSiniestro`),
  ADD KEY `idPoliza` (`idPoliza`);

--
-- Indices de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD PRIMARY KEY (`idVehiculo`),
  ADD KEY `idPoliza` (`idPoliza`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agente`
--
ALTER TABLE `agente`
  MODIFY `idAgente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pago`
--
ALTER TABLE `pago`
  MODIFY `idPago` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `poliza`
--
ALTER TABLE `poliza`
  MODIFY `numeroPoliza` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `siniestro`
--
ALTER TABLE `siniestro`
  MODIFY `idSiniestro` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  MODIFY `idVehiculo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pago`
--
ALTER TABLE `pago`
  ADD CONSTRAINT `pago_ibfk_1` FOREIGN KEY (`idPoliza`) REFERENCES `poliza` (`numeroPoliza`);

--
-- Filtros para la tabla `poliza`
--
ALTER TABLE `poliza`
  ADD CONSTRAINT `poliza_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`),
  ADD CONSTRAINT `poliza_ibfk_2` FOREIGN KEY (`idAgente`) REFERENCES `agente` (`idAgente`);

--
-- Filtros para la tabla `siniestro`
--
ALTER TABLE `siniestro`
  ADD CONSTRAINT `siniestro_ibfk_1` FOREIGN KEY (`idPoliza`) REFERENCES `poliza` (`numeroPoliza`);

--
-- Filtros para la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD CONSTRAINT `vehiculo_ibfk_1` FOREIGN KEY (`idPoliza`) REFERENCES `poliza` (`numeroPoliza`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
