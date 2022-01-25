-- Armamento
select * from armamento as a;

insert into armamento values (1, 'Escudo Mágico', 25,'A', 3);
insert into armamento values (2, 'Escudo Mágico', 25,'A', 3);
insert into armamento values (3, 'Martillo brillante', 20,'A', 8);
insert into armamento values (4, 'Espada del Augurio', 35,'B', 7);
insert into armamento values (5, 'Escudo del Castillo', 50,'B', 10);
insert into armamento values (6, 'Arco Enigma', 15,'C', 4);
insert into armamento values (7, 'Flechas x 10', 40,'B', 5);
insert into armamento values (8, 'Flechas x 20', 50,'A', 7);
insert into armamento values (9, 'Guantes de Box', 8,'C', 2);
insert into armamento values (10, 'Bomba Molotov', 25,'B', 7);

-- Armamento Característica
select * from armamentocaracteristica as a;

insert into armamentocaracteristica values (1, 25, 100, 50, 10);
insert into armamentocaracteristica values (2, 20, 80, 50, 10);
insert into armamentocaracteristica values (3, 35, 70, 50, 10);
insert into armamentocaracteristica values (4, 45, 100, 50, 10);
insert into armamentocaracteristica values (5, 25, 50, 50, 10);

-- Enemigo
select * from enemigo as e;

insert into enemigo values (1, 'Monster Bad', 'A', 1);
insert into enemigo values (2, 'Great Sun', 'B', 2);
insert into enemigo values (3, 'Bad boy', 'A', 3);
insert into enemigo values (4, 'Big insect', 'B', 4);
insert into enemigo values (5, 'New way', 'A', 5);

-- Enemigo Armamento
select * from enemigoarmamento as e;

insert into enemigoarmamento values (1, 'A', 1, 2);
insert into enemigoarmamento values (2, 'A', 2, 3);
insert into enemigoarmamento values (3, 'A', 3, 3);
insert into enemigoarmamento values (4, 'A', 2, 2);
insert into enemigoarmamento values (5, 'A', 4, 1);
insert into enemigoarmamento values (6, 'A', 5, 5);


-- Jugador
select * from jugador as j;

insert into jugador values (1, 'wilder', 'wilder25', '1983-06-30', 'wilbravo@gmail.com', 0, 0, 'A', 0, 0, 0);
insert into jugador values (2, 'ariosto', 'arvin85', '2000-04-25', 'arvin@gmail.com', 0, 0, 'A', 0, 0, 0);
insert into jugador values (3, 'gamer25', 'remag', '1990-02-12', 'gamer25@gmail.com', 0, 0, 'A', 0, 0, 0);
insert into jugador values (4, 'tony85', 'tonyxxx', '1999-12-10', 'tonybc@gmail.com', 0, 0, 'A', 0, 0, 0);
insert into jugador values (5, 'movi10', 'movimovi', '1988-05-15', 'movigamer@gmail.com', 0, 0, 'A', 0, 0, 0);

-- Jugador Armamento

select * from jugadorarmamento as j;

insert into jugadorarmamento values (1, 1, 3, 'A');
insert into jugadorarmamento values (2, 2, 5, 'A');
insert into jugadorarmamento values (3, 3, 2, 'A');
insert into jugadorarmamento values (4, 2, 1, 'A');
insert into jugadorarmamento values (5, 1, 4, 'A');
insert into jugadorarmamento values (6, 3, 3, 'A');
insert into jugadorarmamento values (7, 4, 5, 'A');
insert into jugadorarmamento values (8, 4, 6, 'A');
insert into jugadorarmamento values (9, 1, 2, 'A');

-- Partida
select * from partida as p;

insert into partida values (1, 0, 1);
insert into partida values (2, 0, 2);
insert into partida values (3, 0, 3);
insert into partida values (4, 0, 4);
insert into partida values (5, 0, 5);
insert into partida values (6, 0, 6);
insert into partida values (7, 0, 1);

-- Puntaje

select * from puntaje as pu;

insert into puntaje values (1, 2, 1);
insert into puntaje values (2, 4, 2);
insert into puntaje values (3, 6, 3);
insert into puntaje values (4, 8, 2);
insert into puntaje values (5, 2, 4);
insert into puntaje values (6, 10, 4);
insert into puntaje values (7, 10.25, 5);


-- Querys de consultas
select * from jugador;

-- Query 1
select 
	j.jugador_id, 
	j.usuario, 
	j.nivel,
	ar.nombre,
	ar.precio
from 
	jugador as j
	inner join jugadorarmamento as ja on j.jugador_id=ja.jugador_id
	inner join armamento as ar on ar.arma_id=ja.arma_id
where 
	j.estado = 'A'
order by
	1
;

-- Query 2
select 
	j.jugador_id, 
	j.usuario,
	sum(pu.cantidad) as puntaje
from
	jugador as j
	inner join partida as pa on j.jugador_id=pa.jugador_id
	inner join puntaje as pu on pu.partida_id=pa.partida_id
where
	j.estado='A'
group by
	j.jugador_id, 
	j.usuario
order by
	puntaje desc
;

-- Query 3
select 
	j.jugador_id, 
	j.usuario,
	count(ja.arma_id) as "Cantidad de armas"
from
	jugador as j
	inner join jugadorarmamento as ja on ja.jugador_id=j.jugador_id
where
	j.estado='A'
group by
	j.jugador_id, 
	j.usuario
order by
	1 
;

-- Query 4

select 
	j.jugador_id, 
	j.usuario,
	count(pa.partida_id) as "Cantidad de partidas"
from
	jugador as j
	inner join partida as pa on j.jugador_id=pa.jugador_id
where
	j.estado='A'
	and j.usuario='wilder'
group by
	j.jugador_id, 
	j.usuario
order by
	1 
;

-- Query 5
select * from jugador as j;
select * from enemigo as e;

select 
	j.jugador_id, 
	j.usuario,
	j.nivel,
	sum(pu.cantidad) as puntaje
from
	jugador as j
	inner join partida as pa on j.jugador_id=pa.jugador_id
	inner join puntaje as pu on pu.partida_id=pa.partida_id
where
	j.estado='A'
	and j.nivel = 1
group by
	j.jugador_id, 
	j.usuario,
	j.nivel
order by
	puntaje desc
;

-- Query 6
select
-- 	concat(j.usuario,' y ', en.nombre) "Jugador y Enemigo",
    j.usuario as Jugador,
	en.nombre as Enemigo,
	ar.nombre as "Arma que comparten"
from 
	jugador as j
	inner join jugadorarmamento as ja on j.jugador_id = ja.jugador_id
	inner join armamento as ar on ar.arma_id = ja.arma_id
	inner join enemigoarmamento as ea on ea.arma_id = ar.arma_id
	inner join enemigo as en on en.enemigo_id = ea.enemigo_id
where
	j.estado='A'
;	

-- Query 6: 
select * from armamentocaracteristica as a;
select * from armamento as a;

select 
	*
from 
	armamento as a
	inner join armamentocaracteristica as ac on a.arma_id = ac.arma_id
;