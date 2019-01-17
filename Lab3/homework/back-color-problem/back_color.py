from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = []
    color = []
    for dic in shapes:
        text.append(dic['text'])
        color.append(dic['color'])
    return  [
                choice(text).upper(),
                choice(color),
                randint(0, 1),
    ]

import sys
sys.path.append(r'C:\Users\dhuye\Desktop\C4E25\labs\lab3\homework')

from part_7_12 import is_inside

def mouse_press(a, b, text, color, quiz_type):
    for dic in shapes:
        if quiz_type == 0:
            if dic['text'] == text.lower():
                h = is_inside([a, b], dic['rect'])
        else:
            if dic['color'] == color:
                h = is_inside([a, b], dic['rect'])
    return h