-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS itr;
USE itr;
-- Eliminar la tabla si ya existe (para evitar errores de duplicación si regenerás)
DROP TABLE IF EXISTS usuario;
-- Crear tabla de usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    colegio VARCHAR(50) NOT NULL,
    rol VARCHAR(20) NOT NULL,
    disciplina VARCHAR(20),     -- Solo obligatorio si es jugador
    categoria VARCHAR(20),      -- Solo obligatorio si es jugador
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contraseña VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS producto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    imagen VARCHAR(100) NOT NULL
);

INSERT INTO producto (nombre, precio, imagen) VALUES
('Gaseosa 500ml', 150, 'producto1.jpeg'),
('Empanada', 200, 'producto2.jpg'),
('Chocolatada', 180, 'producto3.jpg'),
('Alfajor', 120, 'producto4.jpg'); 
-- Jugadores (con disciplina y categoría)
INSERT INTO usuario (colegio, rol, disciplina, categoria, usuario, contraseña) VALUES
('Instituto Técnico Renault', 'jugador', 'voley', 'menor', 'Jitr123', 'Jitr123'),
('Instituto Técnico Renault', 'jugador', 'futbol', 'mayor', 'Jitr123b', 'Jitr123b'),
('Esclavas', 'jugador', 'basquet', 'intermedia', 'Jesclavas123', 'Jesclavas123');

-- Organizadores
INSERT INTO usuario (colegio, rol, disciplina, categoria, usuario, contraseña) VALUES
('Sol de Mayo', 'organizador', NULL, NULL, 'Orgsoldemayo123', 'Orgsoldemayo123'),
('San Patricio', 'organizador', NULL, NULL, 'Orgsanpatricio123', 'Orgsanpatricio123');

-- Espectadores
INSERT INTO usuario (colegio, rol, disciplina, categoria, usuario, contraseña) VALUES
('Instituto Técnico Renault', 'expectador', NULL, NULL, 'Expitr123', 'Expitr123'),
('Esclavas', 'expectador', NULL, NULL, 'Expesclavas123', 'Expesclavas123');

select * from usuario;