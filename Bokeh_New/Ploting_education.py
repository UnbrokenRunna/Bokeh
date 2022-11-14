import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure

#example
#p = figure(plot_width=500,plot_height=400, tools='pan',logo=None)

#p.title.text = 'Education data'


df = pd.read_excel('bachelors.csv')
eng = df['Engineering']
Yr = df['Year']

output_file('Education.html')

f = figure(plot_width=500,plot_height=500,tools='pan')
f.title.text ='Education Data'
f.title.text_color='Green'
f.title.text_font='times'
f.title.text_font_style='bold'
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label='Year'
f.xaxis.axis_label_text_color='Red'
f.yaxis.axis_label_text_color='Red'
f.yaxis.axis_label='Engineering'

f.line(Yr,eng)

show(f)