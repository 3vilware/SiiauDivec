import sqlite3

class administrador():
    def __init__(self):
        self.db = sqlite3.connect("divec.db")
        self.c = self.db.cursor()

    def buscar_profesor_nombre(self, patron):
          self.c.execute("SELECT * FROM profesor WHERE \
          nombre LIKE ?", ("%"+patron+"%",))
          lista=[]
          for e in self.c:
              resultado = {
                          "nombre": e[0],\
                          "salario": e[1],\
                          "puesto": e[2],\
                          "carrera": e[3],\
                          }
              lista.append(resultado)
          return lista

    def buscar_materia_profesor(self, patron, cicle):
          self.c.execute("SELECT nrc,nombreProfesor,clave,nombreMateria,seccion,inicio,fin,\
          CASE \
          WHEN ciclo=201310 THEN '2013A' \
          WHEN ciclo=201320 THEN '2013B' \
          WHEN ciclo=201410 THEN '2014A' \
          WHEN ciclo=201420 THEN '2014B' \
          WHEN ciclo=201510 THEN '2015A' \
          WHEN ciclo=201520 THEN '2015B' \
          WHEN ciclo=201610 THEN '2016A' \
          WHEN ciclo=201620 THEN '2016B' \
          WHEN ciclo=201710 THEN '2017A' \
          END AS ciclo FROM materia WHERE \
          nombreProfesor LIKE ? AND ciclo = ?", ("%"+patron+"%",cicle,))
          lista=[]
          for e in self.c:
              resultado = {
                          "nrc": e[0],\
                          "nombreProfesor": e[1],\
                          "clave": e[2],\
                          "nombreMateria": e[3],\
                          "seccion": e[4],\
                          "inicio": e[5],\
                          "fin": e[6],\
                          "ciclo": e[7],\
                          }
              lista.append(resultado)
          return lista

    def buscar_profesor_materia(self,patron,cicle):
        self.c.execute("SELECT * FROM profesor WHERE nombre IN \
        (SELECT nombreProfesor FROM materia WHERE nombreMateria LIKE ? AND ciclo = ?)", ("%"+patron+"%",cicle))
        lista=[]
        for e in self.c:
            resultado = {
                        "nombre": e[0],\
                        "salario": e[1],\
                        "puesto": e[2],\
                        "carrera": e[3],\
                        }
            lista.append(resultado)
        return lista

    def buscar_profesor_puesto(self, patron):
          self.c.execute("SELECT * FROM profesor WHERE \
          puesto LIKE ?", ("%"+patron+"%",))
          lista=[]
          for e in self.c:
              resultado = {
                          "nombre": e[0],\
                          "salario": e[1],\
                          "puesto": e[2],\
                          "carrera": e[3],\
                          }
              lista.append(resultado)
          return lista
