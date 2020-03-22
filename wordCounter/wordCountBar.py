import pygal
import wordCount
from pygal.style import DarkStyle

line_chart = pygal.Pie(style=DarkStyle)
line_chart.title = "Word Usage of Shakespeare's Romeo and Juliet"

# Romeo and juliet
book = wordCount.sorted_dict('rj.txt')
for i in range(25):
    line_chart.add(book[i][0].upper(), book[i][1])

line_chart.render_to_file('most_used_word_of_rj.svg')
line_chart.render_to_png('most_used_word_of_rj.png')

# Hamlet
line_chart = pygal.Pie(style=DarkStyle)
line_chart.title = "Spanish Word Usage of Shakespeare's Hamlet"

book = wordCount.sorted_dict('hamlet.txt')
for i in range(25):
    line_chart.add(book[i][0].upper(), book[i][1])

line_chart.render_to_file('most_used_words_of_hamlet.svg')
line_chart.render_to_png('most_used_words_of_hamlet.png')
