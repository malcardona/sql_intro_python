#!/usr/bin/env python

""" Ejercicio de profundización [Python]"""

#__author__ = "malcardona"
#__email__ = "acardona@unc.edu.ar"

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import os.path



def fetch():
    """lee el valor de la columna "pulso" de todas las filas
     de la tabla "sensor" de la base de datos "heart.db" """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "heart.db")
    with sqlite3.connect(db_path) as db:
        c = db.cursor() 
        
    query =c.execute('SELECT pulso FROM "sensor"').fetchall()
    
    return query

def line_plot(x, y, title):
    fig = plt.figure()
    fig.suptitle(title, fontsize=16)
    ax = fig.add_subplot()

    ax.plot(x, y, c='darkgreen')
    plt.show(block=False)

def show(data):
    x = list(range(1,len(data)+1, 1))
    line_plot(x, data, "Ritmo Cardiaco")

def estadistica(data):
    estat = np.asanyarray(data)
    print("valor medio {:.2f}".format(estat.mean()))
    print("valor máximo {}".format(estat.max()))
    print("valor mínimo {}".format(estat.min()))
    print("desvio estandar {:.2f}".format(estat.std()))

def plot_3in1(x1, x2, x3, y1, y2, y3) :    
    fig = plt.figure()
    # ax = fig.add_subplot(nrows, ncols, index)
    ax = fig.add_subplot()
    
    ax.scatter(x1, y1, s = 1, color='b', marker='^', label='Aburrida')
    ax.scatter(x2, y2, s = 1, color='r', marker='+', label='Entusiasmada')
    ax.scatter(x3, y3, s = 1, color='g', marker='.', label='Tranquila')
    ax.set_facecolor('whitesmoke')
    ax.set_title("Ritmo Cardiaco") 
    ax.set_xlabel("[i]")
    ax.set_ylabel("Pulso")
    ax.set_ylim([50, 140])
    ax.set_xlim([0, 14800])
    ax.legend()
    plt.show(block=None)   

def regiones(data):
    estat = np.asanyarray(data)
    mean = (estat.mean())
    std = (estat.std())
    x1 = []
    y1 = []
    for i in range(len(data)):
        if data[i] <= (mean-std):
            x1.append(i)
            y1.append(data[i])
    x2 = []
    y2 = []
    for i in range(len(data)):
        if data[i] >= (mean+std):
            x2.append(i)
            y2.append(data[i])
    x3 = []
    y3 = []
    for i in range(len(data)):
        if data[i] < (mean+std) and data[i] > (mean-std):
            x3.append(i)
            y3.append(data[i])
    plot_3in1(x1, x2, x3, y1, y2, y3)

if __name__ == '__main__':
    print("Ejercicio de profundización SQL")

# Leer la DB
data= fetch()

# Data analytics
show(data)
estadistica(data)
regiones(data)

