#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    db.commit()

    

def fill(group):
    print(' Agregando ... {}'.format(group))
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    c.executemany("""
        INSERT INTO estudiante (name, age, grade, tutor)
        VALUES (?,?,?,?);""", group)

    db.commit()
    

def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    for row in c.execute('SELECT * FROM estudiante'):
        print(row)
    

def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    c.execute("SELECT id, name, age FROM estudiante WHERE grade =?", (grade,))
    query = c.fetchall()
    print(query)
    

def insert(v1, v2 , v3):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    c.executemany("""
        INSERT INTO estudainte (name, age, grade)
        VALUES (?,?,?);""", v1, v2, v3)
   

def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    with sqlite3.connect('secundaria.db') as db:
        # Crear el cursor para poder ejecutar las querys
        c = db.cursor()

    c.execute("UPDATE estudiante SET name =? WHERE id =?", ( name, id, ))
    db.commit()
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset querybase (DB)

    group1 = [('SALMAN, Facundo', 5, 1, 'Max',),
             ('ASTUDILLO, Luciano', 7, 1, 'Max'),
             ('CASTRO, Emmanuel', 6, 1,'Max'),
             ]

    group2 = [('AYBAR, Ana', 8, 1, 'Lewis',),
             ('ALBORNOZ, Julieta', 8, 1, 'Lewis'),
             ('BRUNO, Laura', 9, 1,'Lewis'),
             ]

    group3 = [('CABRAL, Jazmin', 10, 3, 'Valteri',),
             ('FERLAUTO, Petra', 11, 3, 'Valteri'),
             ('FLORES, Marcela', 12, 3,'Valteri'),
             ]           

    group4 = [('FRESCO, Adriana', 13, 4, 'Lando',),
             ('MERCADO, Yamila', 13, 4, 'Lando'),
             ('GONZALEZ, Miguel', 12, 4,'Lando'),
             ]

    group5 = [('GONZALEZ, Nadia', 14, 5, 'Checo',),
             ('CARDENAS, Gaston', 14, 5, 'Checo'),
             ('HERRERA, Jose', 15, 5,'Checo'),
             ]

    group6 = [('PUITA, Jonatha', 14, 5, 'Carlos',),
             ('LORENZI, Fausto', 14, 5, 'Carlos'),
             ('ALTAMIRANO, Sofia', 15, 5,'Carlos'),
             ]

    fill(group1)
    fill(group2)
    fill(group3)
    fill(group4)
    fill(group5)
    fill(group6)

    fetch()

    grade = 3
    search_by_grade(grade)

    new_student = ['You', 16, 4 ] 
    # insert(new_student)

    name = 'ASTUDILLO, Juan'
    id = 2
    modify(id, name)

    fetch()

