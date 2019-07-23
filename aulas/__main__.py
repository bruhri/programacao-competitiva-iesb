import os
import webbrowser
from aula01.graficos import campeoes_brasileiros, campeoes_mudiais

os.system('rm -r .beampy_cache_slide')

#your beampy package
theme_path = '~/.local/lib/python3.6/site-packages/beampy/themes'
theme_path = '/home/c1296467/anaconda3/envs/make_slide/lib/python3.6/site-packages/beampy/themes'

# campeoes_brasileiros()
# campeoes_mudiais()
os.system(f'cp aulas/maratonaiesb_theme.py {theme_path}')

# os.system('python3 aulas/aula01/slide.py')
os.system('python3 aulas/aula02/slide.py')