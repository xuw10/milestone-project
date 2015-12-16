import flask

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

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
    args = flask.request.args
    color = colors[getitem(args, 'color', 'Black')]
    
    #####NEED TO MODIFY THIS PART!!!###########
    _from = int(getitem(args, '_from', 0))
    to = int(getitem(args, 'to', 200))
    x = list(range(_from, to + 1))
    fig = figure(title="Historical prices of different stocks")
    fig.line(x, [i ** 3 for i in x], color=color, line_width=2)
    #######END MODIFIED PART!####################
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
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
    )
    return encode_utf8(html)
def main():
    #app.debug = True
    app.run()
if __name__ == "__main__":
    main()
