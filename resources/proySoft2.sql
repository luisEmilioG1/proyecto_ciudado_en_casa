CREATE DATABASE IF NOT EXISTS SOFT2;
USE SOFT2;

CREATE TABLE signosVitales
(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre_signo varchar(20) not null,
unidad varchar(4) not null 
);

CREATE TABLE Diagnostico
(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre_diagnostico varchar(50),
descripcion varchar(100) 
);

CREATE TABLE usuario
(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre varchar(20) not null,
apellido  varchar(20),
cedula int unique not null,
edad int not null,
telefono varchar(10),
email varchar(50) not null unique,
psswd varchar(50) not null,
direccion varchar(50)
);

CREATE TABLE auxiliar
(
id INT PRIMARY KEY AUTO_INCREMENT,
usuario_id INT NOT NULL UNIQUE, -- uno a uno
FOREIGN KEY auxiliar_usuario(usuario_id) REFERENCES usuario(id)
);

CREATE TABLE familiarDesignado
(
id INT PRIMARY KEY AUTO_INCREMENT, 
usuario_id INT NOT NULL UNIQUE, -- uno a uno
CONSTRAINT fk_familiar_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuario(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE personalMedico
(
id INT PRIMARY KEY AUTO_INCREMENT, 
usuario_id INT UNIQUE , -- cero o uno a uno
tarjeta_profecional varchar(10),
especialidad varchar(15),
tipo_personal char,
CONSTRAINT fk_personalMedico_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuario(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE paciente
(
id INT PRIMARY KEY AUTO_INCREMENT, 
familiar_id INT NOT NULL UNIQUE,  -- uno a uno
usuario_id INT NOT NULL UNIQUE, -- uno a uno
CONSTRAINT fk_paciente_familiar
    FOREIGN KEY (familiar_id)
    REFERENCES familiarDesignado(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_paciente_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuario(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

CREATE TABLE historialCuidados
(
id INT PRIMARY KEY AUTO_INCREMENT, 
fecha_inicial DATETIME NOT NULL,
fecha_final DATETIME NOT NULL,
cuidado VARCHAR(50),
paciente_id INT,  -- cero o muchos a uno
profecional_id INT, -- cero o muchos a uno
descripcion VARCHAR(500),
CONSTRAINT fk_historialCuidados_paciente
    FOREIGN KEY (paciente_id)
    REFERENCES paciente(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_historialCuidados_profecional
    FOREIGN KEY (profecional_id)
    REFERENCES personalMedico(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE historialSignoVital
(
id INT PRIMARY KEY AUTO_INCREMENT, 
fecha DATETIME NOT NULL,
valor FLOAT,
signo_id INT NOT NULL, -- muchos a uno
paciente_id INT,  -- cero o muchos a uno
CONSTRAINT fk_historialSignoVital_signosVitales
    FOREIGN KEY (signo_id)
    REFERENCES signosVitales(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_historialSignoVital_paciente
    FOREIGN KEY (paciente_id)
    REFERENCES paciente(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE personalACargo
(
id INT PRIMARY KEY AUTO_INCREMENT, 
paciente_activo BOOL,
profecional_id INT, -- muchos a uno
paciente_id INT, -- muchos a uno
CONSTRAINT fk_personalACargo_presonalMedico
    FOREIGN KEY (profecional_id)
    REFERENCES personalMedico(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_personalACargo_paciente
    FOREIGN KEY (paciente_id)
    REFERENCES paciente(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE historialDiagnostico
(
id INT PRIMARY KEY AUTO_INCREMENT, 
fecha DATETIME,
profecional_id INT, -- cero o muchos a uno
paciente_id INT, -- cero o muchos a uno
diagnostico_id INT NOT NULL,  -- muchos a uno
CONSTRAINT fk_historialDiagnostico_presonalMedico
    FOREIGN KEY (profecional_id)
    REFERENCES personalMedico(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_historialDiagnostico_paciente
    FOREIGN KEY (paciente_id)
    REFERENCES paciente(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
CONSTRAINT fk_historialDiagnostico_diagnostico
    FOREIGN KEY (diagnostico_id)
    REFERENCES diagnostico(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);







