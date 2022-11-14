import pandas as pd
from bokeh.io import output_file,show
from bokeh.plotting import figure

df = pd.read_excel('verlegenhuken.xlsx')

Temp = df['Temperature']/10
Pascal = df['Pressure']/10
output_file('Weather Data.html')

p =figure(plot_width = 500, plot_height=500, tools ='pan')
p.title.text ='Weather Data'
p.title.text_color='Green'
p.title.text_font='times'
p.title.text_font_style='bold'
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label='Temp (°C)'
p.xaxis.axis_label_text_color='Red'
p.yaxis.axis_label_text_color='Red'
p.yaxis.axis_label='Pascal (hPa)'

p.circle(Temp, Pascal, size=0.5)

show(p)
