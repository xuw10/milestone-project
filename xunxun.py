from flask import Flask, render_template, request, redirect
from jinja2 import Template
import pandas as pd
from bokeh.plotting import figure,output_notebook,show
from bokeh import embed
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
import time
from datetime import *
import numpy as np
from bokeh.plotting import *
from bokeh.resources import CDN
from bokeh.embed import file_html,components 
from bokeh.palettes import Spectral11
output_file('figures.html')
app = Flask(__name__)

@app.route('/')
def main():
   return redirect('/index')
#@app.route('/')
#def indexPage():
#    df = pd.read_csv("YAHOO-INDEX_GSPC.csv",header=None,names=['Date','Open','High','Low','Close','Volume','Adj Close'],index_col='Date')
#    numlines=len(df.columns)
#    mypalette=Spectral11[0:numlines]
#    yys = []
#    for name in df:
#        yy = df[name].values
#        yys.append(yy)
#    TOOLS = "pan,wheel_zoom,box_zoom,reset,resize"
#    p = figure(data_frame,tools=TOOLS,width=300,height=300,title='Data from Quandle WIKI set',x_axis_label='date',x_axis_type='datetime')
#    my_d_np=[datetime.strptime(x, '%m/%d/%y') for x in df.index.values]
#    p.line(my_d_np,yys[0],legend="Open",line_width=2,line_color="red")
#    #p.line(my_d_np,yys[1],legend="High",line_width=2,line_color="blue")
#    #p.line(my_d_np,yys[2],legend="Low",line_width=2,line_color="green")
#    #p.line(my_d_np,yys[3],legend="Close",line_width=2,line_color="orange")
#    #p.line(my_d_np,yys[5],legend="Adj Close",line_width=2,line_color="black")
#    #figJS,figDiv = components(p,CDN)
#    script,div=embed.components(p)
#    return render_template('figures.html',script=script,div=div)
@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
