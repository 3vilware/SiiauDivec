import sqlite3
import urllib.request
import requests
import pandas
import re
import html
import unicodedata
from bs4 import BeautifulSoup
from decimal import Decimal
from connect import db

cmd = db()
ciclos = ['201310', '201320', '201410', '201420', '201510', '201520', '201610', '201620', '201710'] # ciclos a buscar
secc = ['INCO', 'INNI'] 

cmd.inicializarDB()

for the_ciclo in ciclos: 
    for the_sec in secc: 
        print(the_ciclo,"\t",the_sec)
        cucei = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop="+the_ciclo+"&cup=D&majrp="+the_sec+"&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000"
        
        page = urllib.request.urlopen(cucei)

        soup = BeautifulSoup(page, "lxml") 
        datag = soup.find_all("tr", style="background-color:#e5e5e5;")
        datag2 = soup.find_all("tr", style="background-color:#FFFFFF;")
       
        items = soup.find_all("td", class_="tdprofesor") 

        url = "http://148.202.105.181/transd/ptqnomi_responsive.PTQNOMI_D" 

        flag = 1 
        limit = 0 
        bandera = 0 
        count = 0 #Contador para intercalar entre datag y datag2
        if the_ciclo == '201520' and the_sec=="INCO":
            dato_usado = 172 #Para saber el "index" de datag que usaremos
            dato2_usado = 172 # Igual que arriba pero con datag2
        else:
            dato_usado = 0 #Para saber el "index" de datag que usaremos
            dato2_usado = 0
        #for x, h, w in zip(items, datag, datag2):
        for x in items: 
            if(flag == 0):
                limit += 0 # Para el limite
                if(limit > 4):
                    break # Rompe el ciclo del limite
                flag = 1

                getname = re.search(r'([\S]+)\s([\S]+)\,\s([\S]+)', x.string, re.M|re.I) # Obtenemos con regex el nombre del profe
                
                if getname:
                    if len(getname.group(3)) > 0:
                        pname = getname.group(3) 
                    else:
                        pname=""

                    if len(getname.group(2)) > 0:
                        pmater = getname.group(2) 
                    else:
                        pmater=""

                    if len(getname.group(1)) > 0:
                        ppater = getname.group(1) 
                    else:
                        ppater=""
                else:
                    ppater=""
                    pmater=""
                    pname=""

                finalName = pname+" "+ppater+" "+pmater

                p = {"pDepen":"",            "pDepenDesc":"", 
                "pMaterno":pmater,
                "pNombre":pname,
                "pPaterno":ppater,
                "pTabu":"",            "p_selMes":"201703",            "p_selMonto":"0",            "p_selQui":"1"}
                resp = requests.post(url, params=p) 
                    
                newurl = re.sub(r'\%\C3\%91', '%D1', resp.url) 
                resp = urllib.request.urlopen(newurl)
                nomina = BeautifulSoup(resp, "lxml")
                el_puesto="" 
                el_puesto = nomina.find('td', {'data-title': 'PUESTO'}) 

                los_sueldos = nomina.find_all('td', {'data-title': 'SUELDO NETO'}) 

                if los_sueldos: 
                    for y in los_sueldos: # A veces son mas de uno, entonces hacemos un for
                        valor = float(Decimal(re.sub(r'[^\d.]', '', y.a.string))) # Los convertimos a float (Original era un string)
                       
                if el_puesto:
                    cmd.insertarProfesor([finalName,valor,el_puesto.string,the_sec])    
                else:
                    cmd.insertarProfesor([finalName,valor,"Desconocido",the_sec])

                if(count % 2 == 0): # Par
                    print("index dato_usado=",dato_usado)
                    try:
                        usar = datag[dato_usado]
                    except IndexError:
                        break
                    dato_usado += 1 # se aumenta en uno para que el siguiente ciclo use el siguiente index
                else:
                    print("index dato2_usado=",dato2_usado)
                    try:
                        usar = datag2[dato2_usado]
                    except IndexError:
                        break
                    dato2_usado += 1
                count+=1               

                e = usar.find_all("td", class_="tddatos") 
                nrc = e[0].string # El primero es nrc
                Clave = e[1].string # El segundo la clave
                Materia = e[2].string # El tercer la materia
                Sec = e[3].string # El cuarto la Sec

                cmd.insertarMateria([nrc,finalName,Clave,Materia,Sec,1,1,the_ciclo])
                print("\t\t\t",nrc,"\t",Clave,"\t",Materia,"\t",Sec)

            else: # Bandera para saltar un td del nombre profe
                flag = 0
                #
            #
cmd.anularRepetidos()
