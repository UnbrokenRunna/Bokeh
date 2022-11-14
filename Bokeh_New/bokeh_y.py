from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare sonme data
df = pandas.read_csv
x=[]
y =[]

#prepare the output file
output_file('triangle.html')

#create a figure object
f=figure()

#create the line plot
f.circle(x,y)

#write the plot in the figure object
show(f)