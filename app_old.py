import flask
import Quandl
import requests
import pandas as pd
from flask import Flask
import os
from datetime import *
import numpy as np

from bokeh.embed import components
from bokeh.plotting import *
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.palettes import Spectral11
app = flask.Flask(__name__)
colors = {
    'Black': '#000000',
    'Red':   '#FF0000',
    'Green': '#00FF00',
    'Blue':  '#0000FF',
}
def getitem(obj,item,default):
	if item not in obj:
		return default
	else:
		return obj[item]
@app.route("/")
def myPlot():
	args = flask.request.args
	color = colors[getitem(args, 'color', 'Black')]
    _from = int(getitem(args, '_from', 0))
    to = int(getitem(args, 'to', 10))
	x = list(range(_from, to + 1))
    fig = figure(title="Polynomial")
    fig.line(x, [i ** 2 for i in x], color=color, line_width=2)
	js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
	#output_file('stocks.html',title='Welcome to Xun Wangs stock price query system!')
	data = Quandl.get('GOOG/NYSE_IBM', collapse='weekly')
	TOOLS = "pan,wheel_zoom,box_zoom,reset,resize"
	numlines=5
	mypalette=Spectral11[0:numlines]
	plot = figure(tools=TOOLS,width=800,height=350, title='Data from Quandle WIKI set', x_axis_label='date', x_axis_type='datetime')
	names=['Open','High','Low','Close','Volume']
	yys = []
	for name in data:
		yy = data[name].values
 		yys.append(yy)
	my_d_np=[]
	for x in data.index.values:
 		my_d_np.append(x)
	dates = np.array(my_d_np)
	pOpen = np.array(yys[0])
	pHigh = np.array(yys[1])
	pLow = np.array(yys[2])
	pClose = np.array(yys[3])
	pVolume = np.array(yys[4])
	plot.line(dates,pOpen,legend="Open",line_width=5,line_color="red")
	plot.line(dates,pHigh,legend="High",line_width=5,line_color="green")
	plot.line(dates,pLow,legend="Low",line_width=5,line_color="blue")
	plot.line(dates,pClose,legend="Close",line_width=5,line_color="orange")
	#return plot
	script, div = components(fig, INLINE)
    html = flask.render_template('embed.html', 
            plot_script=script,plot_div=div, 
            js_resources=js_resources,
            css_resources=css_resources,
            color=color,
            _from=_from,
            to=to)
    return encode_utf8(html)
def main():
    #app.debug = True
    app.run()

if __name__ == "__main__":
    main()
