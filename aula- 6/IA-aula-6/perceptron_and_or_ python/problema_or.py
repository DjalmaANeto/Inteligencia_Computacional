# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:24:20 2019

@author: Aluno
"""
import xlrd

def xlread():
    #abre arquivo
    xls = xlrd.open_workbook("amostra_or.xlsx")
    #pega a primeira linha
    plan = xls.sheets()[0]
    
    #para i de zero ao numero de linhasda planilha
    for i in range(plan.nrows):
        #le os valores nas linhas da planilha
        yield plan.row_values(i)
    
def p(obtido):
    if obtido > 0.1:
        return 1
    
    return 0

def atualiza_pesos(obtido, desejado, W_old, n, x):
    e = desejado - obtido;
    return W_old + n*e*x;

        
def treinamento(n, w1, w2, epocas):
    x1 = []
    x2 = []
    classe = [] 
    
    for linha in xlread():
        x1.append(linha[0])
        x2.append(linha[1])
        classe.append(linha[2])
        
    del x1[0];
    del x2[0];
    del classe[0];
    
    
    for z in range(1, epocas+1):
        finalizado = True;
        print("\n\nEpoca {}:".format(z))
        print("|   X1  |   X2  |  Resultado obtido |  Resultado desejado |  W1 new |  W2 new  |")
        for i in range(0, len(x1)):
            obtido = p((x1[i]*w1) + (x2[i]*w2)) #obtido recebe é a função de verificação;
            
            if obtido != classe[i]:
                w1 = float('{0:.3g}'.format(atualiza_pesos(obtido, classe[i], w1, n, x1[i])))
                w2 = float('{0:.3g}'.format(atualiza_pesos(obtido, classe[i], w2, n, x2[i])))
                finalizado = False;
                
            print("|   {}  |   {}  |        {}         |          {}         |    {}  |    {}   |".format(str(int(x1[i])).center(2), str(int(x2[i])).center(2), str(obtido).center(2), str(int(classe[i])).center(2), str(w1).center(2), str(w2).center(2)))
        
        if finalizado==True:
            break;
            
    
    
    if finalizado == False:
        print("\nNão foi possível compreender a amostra.\nTente com outros valores.")
    
    
    else:
        print("\n\nFinalizou na época {}".format(z))
        print("Treinamento finalizado.\nOs pesos são W1 = {}, W2 = {}.".format(w1, w2));
    
treinamento(0.1, -0.2, 0.5, 50);