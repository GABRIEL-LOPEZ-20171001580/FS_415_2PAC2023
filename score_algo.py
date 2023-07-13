import pandas as pd
from lib_notas import *

df = pd.read_csv('./Listado_FS_415.csv')

string = 'I1.INT'
df = add_column(df,string)

groups  = [
            [[20201002877,20141003775,20151002176],86]
        ]

for i in range(0,len(groups)):
    df = insert_note(df,string,groups[i][0],groups[i][1])


string = 'I2.CM' 
df = add_column(df,string)

groups  = [
            [[20201002877,20141003775,20151002176],42]
        ]

for i in range(0,len(groups)):
    df = insert_note(df,string,groups[i][0],groups[i][1])

df.to_csv('NOTAS_FS_415_12_07_2023.csv')
