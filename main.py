# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:44:55 2023

@author: ljzap
"""
from manejadorvf import ManejadorVF

if __name__ == '__main__':
    mv=ManejadorVF()
    mv.testViajero()
    print('Datos de viajeros al inicio: ')
    print(mv)

    num_bus=int(input('Ingrese nro de viajero: '))
    
    nro=mv.buscarViajero(num_bus)
    if nro == None:
        print('El nro de viajero {} no corresponde a un viajero frecuente registrado.'.format(num_bus))
    else:
        print('Seleccione la opcion: ')
        print('1- Consultar Cantidad de Millas.')
        print("2- Acumular Millas")
        print("3- Canjear Millas.")
        opcion=int(input('Ingrese la opcion: '))
        mv.Opciones(nro, opcion)
        
        
    
        
    
    
    
        