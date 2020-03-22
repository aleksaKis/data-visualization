import pygal
from pygal.style import NeonStyle
from letterFrequency import get_dictionary
from serbianLetterFrequency import get_serbian_dictionary

bar_chart = pygal.Bar(fill=True, nterpolate='cubic', style=NeonStyle)
bar_chart.title = 'Comparison Between Serbian and English Letter Frequency\n'

english = get_dictionary()
serbian = get_serbian_dictionary()

# Empty lists for the loop
srb = []
eng = []
labels = []

# Compare only letters that are in both dictionaries
for c in english:
    try:
        # bar_chart.add(c, [{'value': serbian[c], 'label': 'Serbian'}])
        # bar_chart.add(c, [{'value': english[c], 'label': 'English'}])
        srb.append(serbian[c])
        eng.append(english[c])
        labels.append(c.upper())
    except KeyError:
        pass

bar_chart.x_labels = labels
bar_chart.add('Serbian', srb)
bar_chart.add('English', eng)

bar_chart.render_to_file("dictionaryComparisonChart.svg")
bar_chart.render_to_png('dictionaryComparisonChart.png')