# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:29:50 2023

@author: ljzap
"""
import csv
from viajerofrecuente import ViajeroFrecuente

class ManejadorVF:
    __listavf=[]
    
    def __init__(self):
        self.__listavf=[]
    def agregarViajero(self, viajero):
        self.__listavf.append(viajero)
    
    
    def testViajero(self):
        archivo=open('archivoVF.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                viajero=ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2], fila[3], int(fila[4]))
                self.agregarViajero(viajero)
        archivo.close()
        
    def buscarViajero(self, nro):
        i=0
        retorno= None
        bandera= False
        while not bandera and i< len(self.__listavf):
            if self.__listavf[i].getNro()==nro:
                bandera= True
                retorno= i
            else:
                i+=1
        return retorno
    
    def Opciones(self,i, opcion):
        if opcion==1:
            self.__listavf[i].cantidadTotaldeMillas()
        elif opcion==2:
            acum=int(input('Ingresar millas a acumular: '))
            self.__listavf[i].acumularMillas(acum)
        elif opcion==3:
            canje=int(input('Ingresar millas a canjear: '))
            self.__listavf[i].canjearMillas(canje)
        else:
            print('La opcion elegida no es correcta.')

    
    
    