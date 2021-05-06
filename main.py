from openpyxl import load_workbook
from pandas import ExcelWriter
import numpy as np
import pandas as pd

class matriz:

  def arreglos(self):

    df = pd.read_excel("Libro1.xlsx", sheet_name='Hoja1',  header=None)

    matriz=df.values
    print(matriz)

    a=matriz.transpose()
    b=a.tolist()
    print(b)

    matriz1=pd.DataFrame({'Columna1':b[0],'Columna2':b[1],'Columna3':b[2]})
    print(matriz1)

    nuevo=ExcelWriter('Copia1.xlsx')

    matriz1.to_excel(nuevo,'Hoja 1 copia',index=False)

    nuevo.save()


    

a=matriz()
a.arreglos()


  
  