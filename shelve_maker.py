import shelve
import contextlib
import datetime


s = shelve.open('data')

s['time'] = datetime.datetime.now()
s['talst'] = {'Version Control': 0, 'Agile Methodology': 0, 'Programming Logic': 0}


s.close()
