from encodings import utf_8
from urllib import response
from bokeh.plotting import figure, show, output_file
import pandas as pd

# p = figure(plot_witdh = 300, plot_height = 300, tools = 'pan')

# p.title = 'Earthquake'
# p.title_text_color = 'Orange'
# p.title_text_font = 'times'
# p.title_text_style = 'italic'

# p.yaxis.minor_tick_line_color='Yellow'

# p.axis.axis_label ='Times'
# p.yaxis.axis_label='Value'

# p.line([1,2,3,4,5],[5,6,6,5,3],line_width=2, color='red',alpha=0.5)

# output_file('Scatter_plotting.html')

df = pd.read_csv('C:\\Users\\Wisdom Aklamati\\Documents\\HFT\\Semester 2\\Internet GIS\\CIV_visualization\\Python expert\\adbe.csv', parse_dates =['Date'])
p = figure(width =500, height = 300, x_axis_type = 'datetime', sizing_mode= 'scale_both')
p.line(df['Date'], df['Close'],color = 'Orange', alpha=0.5)

output_file('Timeseries.html')

show(p)

show(p)
