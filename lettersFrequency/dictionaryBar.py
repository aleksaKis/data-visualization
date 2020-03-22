import pygal
from letterFrequency import get_dictionary
from pygal.style import NeonStyle

line_chart = pygal.HorizontalBar(fill=True, nterpolate='cubic')
line_chart.title = 'Letter Frequency in English Dictionary\n'

dictionary = get_dictionary()

for i in dictionary:
    line_chart.add(i.upper(), dictionary[i])

line_chart.render_to_file('letterFrequency.svg')
line_chart.render_to_png("letterFrequency.png")