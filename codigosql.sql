create table profesor(
	nombre varchar primary key,
	salario real,
	puesto varchar,
	carrera varchar);

create table materia(
	nrc varchar primary key,
	nombreProfesor varchar,
	clave varchar,
	nombreMateria varchar,
	seccion varchar,
	inicio smallint,
	fin smallint,
	ciclo integer,
	FOREIGN KEY (nombreProfesor) REFERENCES profesor(nombre)
	on update cascade
	on delete cascade);


delete from profesor;
delete from materia;
select *, count(*) from profesor group by nombre having count(*)>1 order by name
insert into profesores select nombre,salario,puesto,carrera from profesor;
insert into profesores select * from profesor group by nombre having count(*)>=1;
