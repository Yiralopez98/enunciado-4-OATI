# Gestion de Tutoriales

Breve descripción del proyecto.

## Requisitos

- Python 3.x
- Asegúrate de tener Python y XAMPP instalados en tu sistema.
- Crea una base de datos en MySQL a través de phpMyAdmin.
- SQLAlchemy

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias ejecutando `pip install sqlalchemy`.

## Uso

1. Ejecuta el script `main.py` para interactuar con la base de datos.

## Base de datos

-- Crear la base de datos 
CREATE DATABASE tutoria_db;

-- Usar la base de dato
USE tutoria_db;

-- Crear la tabla para tutorials
CREATE TABLE tutorials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    published BOOLEAN,
    long_description VARCHAR(255)
);
-- Crear la tabla para tags
CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
-- Crear la tabla para tutorial_tags
CREATE TABLE tutorial_tags (
    tutorial_id INT,
    tag_id INT,
    PRIMARY KEY (tutorial_id, tag_id),
    FOREIGN KEY (tutorial_id) REFERENCES tutorials(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);
