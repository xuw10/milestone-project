import os
import Quandl
import requests
import pandas as pd
from datetime import *
import numpy as np
import flask
from flask import request,url_for
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.plotting import *
app = flask.Flask(__name__)

colors = {
    'Black': '#000000',
    'Red':   '#FF0000',
    'Green': '#00FF00',
    'Blue':  '#0000FF',
}
def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]

@app.route("/")
def polynomial():
    """ Very simple embedding of a polynomial chart"""
    # Grab the inputs arguments from the URL
    # This is automated by the button
    args = flask.request.args
    color = colors[getitem(args, 'color', 'Black')]
    typeP = int(getitem(args,'typeP',1))
    ticker = str(getitem(args,'ticker','AAPL')) 
    #ticker='AAPL'
    sa = "WIKI/"
    myS=""
    myS = sa+ticker
    data = Quandl.get(myS,collapse='weekly')
    TOOLS = "pan,wheel_zoom,box_zoom,reset,resize"
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
   # Get all the form arguments in the url with defaults
    #_from = int(getitem(args, '_from', 0))
    #to = int(getitem(args, 'to', 10)) #need to transfrom datetime type to int??? 
    # Create a polynomial line graph
    x = list(range(_from, to + 1))
    fig = figure(title="Historical price of a stock(from Quandl API)",tools=TOOLS,x_axis_label='date',x_axis_type='datetime',legend=ticker)
    #fig.line(x, [i ** 2 for i in x], color=color, line_width=2)
    if typeP == 1:
        fig.line(dates,pOpen,legend="Opening price",line_width=5,line_color=color)
    elif typeP == 2:
        fig.line(dates,pHigh,legend='Highest price',line_width=5,line_color=color)
    elif typeP == 3:
        fig.line(dates,pLow,legend='Lowest price',line_width=5,line_color=color)
    elif typeP == 4:
        fig.line(dates,pClose,legend="Closing price",line_width=5,line_color=color)
    elif typeP == 5:
        fig.line(dates,pVolume,legend="Volume", line_width=5,line_color=color)
    # Configure resources to include BokehJS inline in the document.
    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#bokeh-embed
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/user_guide/embedding.html#components
    script, div = components(fig, INLINE)
    html = flask.render_template(
        'embed.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        color=color,
        _from=_from,
        to=to
        ticker=ticker
    )
    return encode_utf8(html)


def main():
	#port = int(os.environ.get("PORT", 5000))    
	#app.run(host='0.0.0.0',port=5000)
    app.run()
if __name__ == "__main__":
    main()
