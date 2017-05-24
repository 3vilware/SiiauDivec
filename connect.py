import sqlite3

class db():
	conectar= sqlite3.connect('divec.db')
	c = conectar.cursor()
	#c.execute("PRAGMA foreign_keys = '1'")

	def insertarProfesor(self,arg):
		self.c.execute("INSERT INTO profesor(nombre,salario,puesto,carrera) VALUES(?,?,?,?)", (arg[0],arg[1],arg[2],arg[3]))
		self.conectar.commit()    		 
		
	def insertarMateria(self,arg):
		self.c.execute("INSERT INTO materia(nrc,nombreProfesor,clave,nombreMateria,seccion,inicio,fin,ciclo) VALUES(?,?,?,?,?,?,?,?)", (arg[0], \
											arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7]))
		self.conectar.commit()

	def mostrarProfesor(self):
		self.c.execute("SELECT * FROM profesor")
		for e in self.c:
			lista = []
			profesor = {
					'nombre':e[0],
					'salario':e[1],
					'puesto':e[2],
					'carrera':e[3]
			}
			lista.append(profesor)
		return lista

	def mostrarMateria(self):
		self.c.execute("SELECT * FROM materia")
		for e in self.c:
			lista = []
			materia = {
					'nrc':e[0],
					'nombreProfesor':e[1],
					'clave':e[2],
					'nombreMateria':e[3],
					'seccion':e[4],
					'inicio':e[5],
					'fin':e[6],
					'ciclo':e[7]
			}
			lista.append(materia)
		return lista

	def inicializarDB(self):
		self.c.execute("DELETE FROM profesor")
		self.c.execute("DELETE FROM materia")
		self.c.execute("DROP TABLE profesor")
		self.c.execute("CREATE TABLE profesor(nombre varchar, salario real, puesto varchar, carrera varchar)")


	def anularRepetidos(self):
		self.c.execute("CREATE TABLE profesorAux(nombre varchar primary key, salario real, puesto varchar, carrera varchar)")
		self.c.execute("INSERT INTO profesorAux SELECT * FROM profesor GROUP BY nombre HAVING count(*)>=1")
		self.c.execute("DELETE FROM profesor")
		self.c.execute("INSERT  INTO profesor SELECT * FROM profesorAux")
		self.c.execute("DELETE FROM profesorAux")
		self.c.execute("DROP TABLE profesorAux")
		self.c.execute("CREATE TABLE materiaAux(nrc varchar primary key,nombreProfesor varchar,clave varchar,nombreMateria varchar,seccion varchar,inicio smallint,fin smallint,ciclo integer,FOREIGN KEY (nombreProfesor) REFERENCES profesor(nombre)on update cascadeon delete cascade)")
		self.c.execute("INSERT INTO materiaAux SELECT * FROM materia GROUP BY nrc HAVING count(*)>=1")
		self.c.execute("DELETE from materia")
		self.c.execute("INSERT INTO materia SELECT * FROM materiaAux")
		self.c.execute("DROP TABLE materiaAux")


#db = db()
#db.insertarMateria(['981273', 'Boites', 'I5888', 'EDA','D05','1700','1900','201710'])
#db.insertarProfesor(['Hassem', 10000, 'auxiliar', 'INNI'])
#db.mostrar()
#conectar.close()