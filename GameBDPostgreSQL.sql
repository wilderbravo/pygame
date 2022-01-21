--
-- ER/Studio 8.0 SQL Code Generation
-- Company :      IIB
-- Project :      Modelo BD Juegos Batalla.DM1
-- Author :       wilder
--
-- Date Created : Thursday, January 20, 2022 19:29:18
-- Target DBMS : PostgreSQL 8.0
--

-- 
-- TABLE: "Armamento" 
--

CREATE TABLE "Armamento"(
    arma_id        int4              NOT NULL,
    nombre         varchar(100)      NOT NULL,
    precio         decimal(10, 4)    NOT NULL,
    tipo           char(1)           NOT NULL,
    resistencia    decimal(10, 4)    NOT NULL,
    CONSTRAINT "PK4" PRIMARY KEY (arma_id)
)
;



-- 
-- TABLE: "ArmamentoCaracteristica" 
--

CREATE TABLE "ArmamentoCaracteristica"(
    armamentocaracteristica_id    int4              NOT NULL,
    poder                         decimal(10, 4)    NOT NULL,
    balas                         decimal(10, 4),
    rapidez                       decimal(10, 4)    NOT NULL,
    arma_id                       int4              NOT NULL,
    CONSTRAINT "PK6" PRIMARY KEY (armamentocaracteristica_id)
)
;



-- 
-- TABLE: "Enemigo" 
--

CREATE TABLE "Enemigo"(
    enemigo_id    int4              NOT NULL,
    nombre        varchar(80)       NOT NULL,
    tipo          char(1),
    nivel         decimal(10, 4),
    CONSTRAINT "PK7" PRIMARY KEY (enemigo_id)
)
;



-- 
-- TABLE: "EnemigoArmamento" 
--

CREATE TABLE "EnemigoArmamento"(
    enemigoarmamento_id    int4       NOT NULL,
    estado                 char(1)    NOT NULL,
    enemigo_id             int4       NOT NULL,
    arma_id                int4       NOT NULL,
    CONSTRAINT "PK8" PRIMARY KEY (enemigoarmamento_id)
)
;



-- 
-- TABLE: "Jugador" 
--

CREATE TABLE "Jugador"(
    jugador_id          int4              NOT NULL,
    usuario             varchar(50)       NOT NULL,
    password            varchar(50)       NOT NULL,
    fecha_nacimiento    timestamp,
    email               varchar(100)      NOT NULL,
    nivel               int2              NOT NULL,
    recompensa          decimal(10, 4)    NOT NULL,
    estado              char(1)           NOT NULL,
    victoria            decimal(10, 4),
    derrota             decimal(10, 4),
    puntaje             decimal(10, 4),
    CONSTRAINT "PK1" PRIMARY KEY (jugador_id)
)
;



-- 
-- TABLE: "JugadorArmamento" 
--

CREATE TABLE "JugadorArmamento"(
    jugadorarmamento_id    int4       NOT NULL,
    jugador_id             int4       NOT NULL,
    arma_id                int4       NOT NULL,
    estado                 char(1)    NOT NULL,
    CONSTRAINT "PK5" PRIMARY KEY (jugadorarmamento_id)
)
;



-- 
-- TABLE: "Partida" 
--

CREATE TABLE "Partida"(
    partida_id    int4    NOT NULL,
    vida          int4    NOT NULL,
    jugador_id    int4    NOT NULL,
    CONSTRAINT "PK3" PRIMARY KEY (partida_id)
)
;



-- 
-- TABLE: "Puntaje" 
--

CREATE TABLE "Puntaje"(
    puntaje_id    int4              NOT NULL,
    cantidad      decimal(10, 4)    NOT NULL,
    partida_id    int4              NOT NULL,
    CONSTRAINT "PK2" PRIMARY KEY (puntaje_id)
)
;



-- 
-- TABLE: "ArmamentoCaracteristica" 
--

ALTER TABLE "ArmamentoCaracteristica" ADD CONSTRAINT "RefArmamento9" 
    FOREIGN KEY (arma_id)
    REFERENCES "Armamento"(arma_id)
;


-- 
-- TABLE: "EnemigoArmamento" 
--

ALTER TABLE "EnemigoArmamento" ADD CONSTRAINT "RefEnemigo10" 
    FOREIGN KEY (enemigo_id)
    REFERENCES "Enemigo"(enemigo_id)
;

ALTER TABLE "EnemigoArmamento" ADD CONSTRAINT "RefArmamento11" 
    FOREIGN KEY (arma_id)
    REFERENCES "Armamento"(arma_id)
;


-- 
-- TABLE: "JugadorArmamento" 
--

ALTER TABLE "JugadorArmamento" ADD CONSTRAINT "RefJugador7" 
    FOREIGN KEY (jugador_id)
    REFERENCES "Jugador"(jugador_id)
;

ALTER TABLE "JugadorArmamento" ADD CONSTRAINT "RefArmamento8" 
    FOREIGN KEY (arma_id)
    REFERENCES "Armamento"(arma_id)
;


-- 
-- TABLE: "Partida" 
--

ALTER TABLE "Partida" ADD CONSTRAINT "RefJugador5" 
    FOREIGN KEY (jugador_id)
    REFERENCES "Jugador"(jugador_id)
;


-- 
-- TABLE: "Puntaje" 
--

ALTER TABLE "Puntaje" ADD CONSTRAINT "RefPartida6" 
    FOREIGN KEY (partida_id)
    REFERENCES "Partida"(partida_id)
;


