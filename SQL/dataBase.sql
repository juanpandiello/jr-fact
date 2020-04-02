CREATE TABLE `cliente` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `razonSocial` varchar(255) NOT NULL,
  `NIF` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `pais` varchar(255) NOT NULL,
  `codigoPostal` varchar(255) NOT NULL
);

CREATE TABLE `factura` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `idCliente` int NOT NULL,
  `fecha` datetime NOT NULL,
  `idConcepto` int NOT NULL,
  `total` integer NOT NULL,
  `iva` integer NOT NULL,
  `baseImponible` integer NOT NULL
);

CREATE TABLE `producto` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `concepto` varchar(255) NOT NULL,
  `precioUnidad` int NOT NULL,
  `cantidad` int NOT NULL,
  `total` int NOT NULL
);

ALTER TABLE `factura` ADD FOREIGN KEY (`idConcepto`) REFERENCES `producto` (`id`);

ALTER TABLE `factura` ADD FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`id`);
