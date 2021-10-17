import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.graph_objects as go

class PlotController:
    def __init__(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis.age = yAxis

    def draw_2_axes_plot(self, xPositions, yPositions):
        figure = plt.figure()
        axes1 = figure.add_axes([0,0,1,1])
        axes1.plot(xPositions,yPositions)
        axes1.axis('equal')
        circle1 = plt.Circle((0, 0), .08, color='orange')
        axes1.add_artist(circle1)
        plt.show()
