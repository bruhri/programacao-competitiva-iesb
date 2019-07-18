# -*- coding: utf-8 -*-

# Maratona IESB Theme for beampy

# version: 0.1.0
# Author: Rodrigo Guimarães Araújo

from beampy.geometry import bottom
from beampy.document import document
from beampy.commands import group, text, figure, rectangle, box

THEME = {}

colors = {
    'yellow':'#F6B801',
    'red':'#DA251C',
    'blue':'#01458E',
    'shadded_blue':'#557ca6'
}

lead_color = colors['red']
standard_text_color = colors['blue']
shaded_text_color = colors['shadded_blue']


THEME['document'] = {
    'format': 'html5',
    'width': 800,
    'height': 600
}

THEME['slide'] = {
    'background': "#ffffff"   
}

THEME['text'] = {
    'size':20,
    'font':'CMR',
    'color': standard_text_color,
    'align':'',
    'x':'center',
    'y':'auto',
    'width':None,
    'usetex':True,
    'va': ''
}

THEME['title'] = {
    'size': 30,
    'font': 'CMR',
    'color': lead_color,
    'x': 'center',
    'y': {'shift':1.2, 'unit':'cm'},
    'reserved_y': '1.5cm',
    'align': '',
    'va': 'baseline'
}


THEME['maketitle'] = {
    'title_size':40,
    'title_color':THEME['title']['color'],
    'author_size':THEME['text']['size'],
    'date_color':standard_text_color,
    'subtitle_color':shaded_text_color,
}


THEME['link'] = {
    'fill':THEME['title']['color']
}

THEME['itemize'] = {
    'x':'center',
    'y':'auto',
    'item_style':'bullet',
    'item_spacing':'+1cm',
    'item_indent':'0cm',
    'item_color':THEME['title']['color'],
    'text_color':THEME['text']['color'],
    'width':None
}

def theme_maketitle(lesson, author, date):
    """
        Function to create the presentation title slide
    """

    args = THEME['maketitle']

    with group(y="center"):

        text(lesson, width=750, y=0, color=args['title_color'], size=args['title_size'], align='center')
        figure('aulas/img/logo_maratona.jpg', width=300, y="+3.5cm")
        text(author, width=750, y="+3.5cm", color=args['subtitle_color'], size=args['author_size'], align='center')
        text(date, width=750, y="+1cm", color=args['date_color'], size=args['date_size'])

THEME['maketitle']['template'] = theme_maketitle


def background_layout():

    total = len(document._slides)
    current = int(document._curentslide.split('_')[1]) + 1
    slide_width = float(document._width)

    y_progress_bar = {'align':'bottom', 'anchor':'bottom', 'shift':0}
    progress_bar = rectangle(x=0, y=y_progress_bar, height=7, width=(current/total * slide_width), 
        color=colors['red'], edgecolor=None)

    x_page_number = {"shift": 0.01, "align":"right", "anchor":"right"}
    text(f'{current}/{total}',  x=x_page_number, y=progress_bar.top-bottom(5), size=13, color=colors['red'])

THEME['slide']['layout'] = background_layout

def cite(author, x='center', y='auto', width=300):
    return box(x=x, y=y, width=width, title=author, 
        title_align='center', color=colors['yellow'], shadow=True)