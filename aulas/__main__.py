import os
import webbrowser

theme_path = '~/.local/lib/python3.6/site-packages/beampy/themes'

os.system(f'cp aulas/maratonaiesb_theme.py {theme_path}')
os.system('python3 aulas/aula01/slide.py')
webbrowser.open('aulas/aula01/slide.html')