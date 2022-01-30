#!/usr/bin/env python

""" Ejercicio de profundización [Python]"""

__author__ = "malcardona"
__email__ = "acardona@unc.edu.ar"

import sqlite3
import numpy as np
import matplotlib.pyplot as plt



def fetch():
    """lee el valor de la columna "pulso" de todas las filas
     de la tabla "sensor" de la base de datos "heart.db" """

    with sqlite3.connect("chinook.db") as db:
        c = db.cursor() 
        
    c.execute('SELECT * FROM "albums"')
    query = c.fetchall()
    print(query)
    
    return pulso

def line_plot(x, y, title, fx):
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    ax = fig.add_subplot()

    ax.plot(x, y, c='darkgreen', label=fx)
    ax.legend()
    ax.grid()
    plt.show()
   

if __name__ == '__main__':
    print("Ejercicio de profundización SQL")

pulso = fetch()

x = len(pulso)

#line_plot(x, pulso, "Ritmo Cardiaco", " ")
