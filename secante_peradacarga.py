import math # importa o modulo de funções matemáticas
#function
def PotKW(vazao, pressao, rend): 
   #Calcula a potência ventilador kW
   #Função de: Vazao (m³/min), Pressã (Pa), Rend (%)
    aux = 0.0
    vazao = vazao / 60 # m³/seg
    rend = rend / 100  # decimal
    aux = vazao * pressao / (rend * 1000)  #Potência kW
    return aux


def PerdaCarga(vazao1, area1, altura1, fatorPe1):
 #Cálculo da perda de carga - grãos em Pascal
 #Função: Vazão (m³/min); Area (m²); Altura (m), produto, fator de majoração 1,5 a 2)
    a= 7.5000 # constantes para trigo
    b =  0.1460
    qa = vazao1 / area1 # Fluxo de ar por area - m³ de ar/min.m²
    aux = (a * (qa ** 2) * altura1 * fatorPe1) / (math.log(1 + b * qa))  #Calculo da  perda de carga Pascal
    
    return aux


def SecantePC(qvazao,  altura_Chapa, altura, rventilador, nVent1):
    #Dim Q0, Q1, Q2, Qaux, Potct, Pes0, Pes1, Pes2, Fx0, Fx1, kW2, Cte, ErroQ As Double
    #Dim Altura1, Ton1 As Double
    #Dim I, J, K As Integer

 k = 1 #int
 i = 0 # int
 ErroQ =100.0 # float
 

 while  (k <= nChapas):
    altura1 = k * altura_Chapa
    Cte = 60 / rventilador / 1000
    # Início Método da secante
    q0 = qazao   # Chutes de Valores inicias
    q1 = qvazao * 1.15
    i= 0
    while ((ErroQ > 0.1) and (i < 100)):
        Pes0 = PerdaCarga(q0, area, altura1, FatorPe)  #Pascal
        Pes1 = PerdaCarga(q1, area, altura1, FatorPe)  #Pascal
        Fx0 = PotKW(Q0, Pes0, rventilador) - KW * nVent1 # F(xo)
        Fx1 = PotKW(Q1, Pes1, rventilador) - KW * nVent1 # F(x1)
        q2 = (q0 * Fx1 - q1 * Fx0) / (Fx1 - Fx0)
        ErroQ = Abs(q1 - q2)
        q0 = q1
        q1 = q2
        i = i + 1
 
#Fim Método da secante
   
    if (i > 100):
      print('Método secante não converge !!!')
      break

   
   #Publicar dados para o gráfico
    Pes2 = PerdaCarga(q2, qrea, qltura1, FatorPe)
    kW2 = PotKW(q2, Pes2, rventilador)
    k= k + 1

return

    diam = float(input('Diâmetro do silo (m) ='))
    altc = float(input('Altura de cilidro (m) ='))



