# coding=utf-8
import numpy as PI
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.graph_objects as go

# Import modules
from orbitPhysics import OrbitPhysics
from plotController import PlotController

def print_plot(xPositions, yPositions):
    figure = plt.figure()
    axes1 = figure.add_axes([0,0,1,1])
    axes1.plot(xPositions,yPositions)
    axes1.set(title='An incomplete simulation',xlabel='X',ylabel='Y')
    axes1.axis('equal')
    circle1 = plt.Circle((0, 0), .08, color='orange')
    axes1.add_artist(circle1)
    plt.show()

def main():
    # Initialize necessary classes
    orbits = OrbitPhysics()

    # DEFNINIM LES VARIABLES INCICIALS
    distanceFromHoleToStar = 1.49e+11 # Distància del forat negre a l'estrella en astronomical units
    starPeriod = 3.1514e+7 # Període en segons de l'estrella al voltant del forat negre
    blackHoleMass = 1.89928438e+14 # Massa en Kg del forat negre
    blackHoleRadius = 0.235974 # Radi del forat negre en astronomical units

    blackHoleIsXTimesStar = 4 # Quantes vegades més gran es el forat negre respecte l'estrella

    starMassInBlackHoleRelation = 1 / blackHoleIsXTimesStar

    # Definim perheli
    perihelionX0 = 0.8982049
    perihelionY0 = 0

    # Perihelion velocities
    perihelionVX0 = 0
    perihelionVY0 = 30.29/1.496e+8*3.154e+7 # Velocitat en el eix Y al periheli de la obrita, quina V ha de ser?

    # Inicialitzem els vectors
    xPos = [perihelionX0]
    yPos = [perihelionY0]
    xvels = [perihelionVX0]
    yvels = [perihelionVY0]

    totalEnergy = orbits.euler_method(perihelionX0, perihelionY0, perihelionVX0, perihelionVY0, 1, starMassInBlackHoleRelation, xPos, yPos)
    print_plot(xPos, yPos)


if __name__ == "__main__":
    main()