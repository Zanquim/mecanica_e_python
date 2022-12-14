# -*- coding: utf-8 -*-
"""calculo_de_vazao.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OOtuJxkpgL9Ue3PwN9uTzsjfAhpg6ud_
"""

import math


def desvio_padrao():

    lista_de_medidas = []
    
    while True:
        
        medidas = input((f'\nDigite o valor de suas medidas:\t'))

        parar = input(f'\nDigite SAIR se quiser parar a inserção de medidas:\t').lower()

        
        lista_de_medidas.append(medidas)
        
        if parar == "sair":

            break
    
    
    print()
    print(f'Esta é a sua lista de medidas {lista_de_medidas}')

    f_medidas = []
    
    for medida in lista_de_medidas:
        f_medidas.append(float(medida))
        print(type(f_medidas[0]))

    colecao = f_medidas

    list_elevado = []

    quadrado = []
        
    media = sum(colecao)/len(colecao)

    print(f'\nA média é: {media:.2f}')

    for numero in colecao:

        numero_menos_media = numero - media

        quadrado.append(numero_menos_media)

        print(f'\nA diferença é: {numero_menos_media:.2f}')

    for elevado in quadrado:

        elevar = elevado*elevado

        list_elevado.append(elevar)

        print(f'\nO quadrado é: {elevar:.4f}')

    variancia = sum(list_elevado)/(len(colecao)-1)

    print(f'\nA variância é: {variancia:.4f}')

    desvio_padrao = math.sqrt(variancia)

    print(f'\nO desvio padrão é: {desvio_padrao:.3f}')

    incerteza = desvio_padrao/math.sqrt(len(colecao))

    print(f'\nA incerteza é {incerteza:.3f}')


desvio_padrao()


def cm_para_m():

    valor_cm = input(f'\nInsira a medida em cm:\t')
    cm_convertido_f = float(valor_cm)
    cm_convertido = f'\n{cm_convertido_f/100}'
    print(f'{cm_convertido} metros')

def m_para_cm():

    valor_m = input(f'\nInsira a medida em m:\t')
    m_convertido_f = float(valor_m)
    m_convertido = f'\n{m_convertido_f/100}'
    print(f'{m_convertido} centímetros')


def m_para_ml():

    valor_m = input(f'\nInsira a medida em m:\t')
    m_convertido_f = float(valor_m)
    m_convertido = f'\n{m_convertido_f*1000}'
    print(f'{m_convertido} milímetros')

def ml_para_m():

    valor_m = input(f'\nInsira a medida em ml:\t')
    ml_convertido_f = float(valor_m)
    ml_convertido = f'\n{ml_convertido_f/1000}'
    print(f'{ml_convertido} metros')


def ml_para_cm():

    valor_m = input(f'\nInsira a medida em ml:\t')
    m_convertido_f = float(valor_m)
    m_convertido = f'\n{m_convertido_f/10}'
    print(f'{m_convertido} centímetros')

  
def cm_para_ml():

  valor_m = input(f'\nInsira a medida em ml:\t')
  m_convertido_f = float(valor_m)
  m_convertido = f'\n{m_convertido_f*10}'
  print(f'{m_convertido} metros')


def volume():

  prismas = ['cubo', 'paralelepípedo', 'cone', 'esfera']

  qual_figura = input(f'\nCalcular o volume de qual figura:\t').lower()

  if qual_figura == 'cubo':

    lado_a_cubo = input(f'\nInsira a medida do lado A em m:\t')
    
    lado_b_cubo = input(f'\nInsira a medida do lado B em m:\t')
    
    altura_cubo = input(f'\nInsira a medida da altura em m:\t')

    
    lado_a_cubo_f = float(lado_a_cubo)
    
    lado_b_cubo_f = float(lado_b_cubo)
    
    altura_cubo_f = float(altura_cubo)

    volume_cubo = lado_a_cubo_f * lado_b_cubo_f * altura_cubo_f

    
    print(f'O cubo tem volume de {volume_cubo:.1f} m³')
      
  
  elif qual_figura == 'paralelepípedo':

        lado_a_parale = input(f'\nInsira a medida do lado A em m:\t')
        
        lado_b_parale = input(f'\nInsira a medida do lado B em m:\t')
        
        altura_parale = input(f'\nInsira a medida da altura em m:\t')

        
        lado_a_parale_f = float(lado_a_parale)
        
        lado_b_parale_f = float(lado_b_parale)
        
        altura_f = float(altura_parale)

        
        volume_paralelepipedo = lado_a_parale_f * lado_a_parale_f * altura_f

        print(f'O paralelepípedo tem volume de {volume_paralelepipedo:.1f} m³')

  elif qual_figura == 'cone':

        raio_do_cone = input(f'\nInsira a medida do raio em m:\t')**2
        
        altura_cone = input(f'\nInsira a medida da altura em m:\t')
        
        pi_co = 3.14
        
        raio_do_cone_f = float(raio_do_cone)
        
        altura_cone_f = float(altura_cone)
        
        pi_f = float(pi_co)
        
        volume_cone = raio_do_cone_f * pi_f * altura_cone_f/3
        
        print(f'\nO cone tem volume de {volume} m³')

  elif qual_figura == 'esfera':

        raio_do_cone = input(f'\nInsira a medida do raio em m:\t')
        
        altura_cone = input(f'\nInsira a medida da altura em m:\t')
        
        pi_cu = 3.14
        
        raio_do_cone_f = float(raio_do_cone)**2
        altura_cone_f = float(altura_cone)
        pi_cu_f = float(pi_cu)
        
        volume_esfera = (4*raio_do_cone_f * altura_cone_f * pi_cu_f)/3
        
        print(f'\nA esfera tem volume de {volume_esfera:.1f} m³')


volume()