# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:43:02 2023

@author: nicassia

LETRECO
"""
import random as rd

dicio = ["grama", "verde", "caldo" ,"crase","cinco","trava","galho"]
palavra = list(dicio[rd.randint(0,len(dicio)-1)])

tentativa = 1

palpite = "palpi"

while tentativa<=2 and palavra != palpite:
    palpite = list(input("\ntentativa {}: ".format(tentativa)))
    exibe = ["_","_","_","_","_"]
    dicas = []
    
    for n in range(len(palpite)):
        if palpite[n] in palavra:
            if palpite[n] == palavra[n]:
                exibe[n] = palpite[n]
            else:
                dicas.append(str("letra '{}' pertence a palavra".format(palpite[n])))
        n = n + 1
            
    print(*exibe, sep = ' ')
    if dicas != []:    
        print("dica(s): ",*dicas, sep = "\n - ")
    if palavra == palpite:
        print("\nPARABÉNS, VOCÊ GANHOU!")
    n = 0
    tentativa = tentativa + 1

print("\nA palavra é: ",*palavra, sep = "")    
print("\nFIM DE JOGO")
