# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:44:55 2023

@author: ljzap
"""

class ViajeroFrecuente:
    __num_viajero=0
    __dni=0
    __nombre=''
    __apellido=''
    __millas_acum=0
    
    def __init__(self, num_viajero,dni, nombre, apellido, millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=millas_acum
    def cantidadTotaldeMillas(self):
        print('Millas en total: {}'.format(self.__millas_acum))
        return self.__millas_acum
    def acumularMillas(self, millas_rec):
        print('Millas antes de la recarga: {}'.format(self.__millas_acum))
        self.__millas_acum+=millas_rec
        print('Millas despues de la recarga: {}'.format(self.__millas_acum))
        return self.__millas_acum
    def canjearMillas(self, millas_canj):
        print('Millas antes del canje: {}'.format(self.__millas_acum))
        if self.__millas_acum>=millas_canj:
            self.__millas_acum-=millas_canj
            print('Millas despues del canje: {}'.format(self.__millas_acum))
        else:
            print('No es posible la operación (millas insuficientes).')
        return self.__millas_acum    
    def getNro(self):
        return self.__num_viajero