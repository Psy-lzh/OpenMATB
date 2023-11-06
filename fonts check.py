from pyglet import *
from matplotlib import font_manager
import pandas as pd
a=[]
b=[]
df=pd.DataFrame()
for x in font_manager.fontManager.ttflist:
    if font.have_font(x.name):
        a.append(x.name)
        b.append(x.fname)
df['name']=a
df['local']=b
df['name']=df['name'].drop_duplicates()
df=df.dropna()
df.to_excel('Fonts in computer.xlsx',index=False)