# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:24:03 2018

@author: Luis César

Calcula - Quebra de Umidade
"""

"""
Descrição das variáveis

Real
Umi, Umf, aux, Mi, Mf, Ui, Uf

Inteiro

"""


def QU(Ui, Uf):  # function  quebra de umidade e ou impureza
  auxf=(Ui-Uf)*100/(100.0-Uf)
  return auxf  

#_____________________________
# Entrada de dados

"""
Umi = input('Teor de umidade inicial (%): ')
Umf = input('Teor de umidade final (%): ')
Mi = input('Massa inicial de produto (t): ')
"""
#_____________________________
# Processamento
print ('    Ui(%)    -  Uf(%)    - QU(%)' )
for i in range (30, 13, -2):
      Umi = i
      Umf = 13.0
      aux = QU(Umi, Umf)
      print (' %8.2f  -  %8.2f  - %8.2f' %(Umi, Umf, aux))

#_