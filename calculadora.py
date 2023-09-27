#def calculadora():
    #b = float(input("N1 > "))
    #a = float(input("N2 > "))
    #somaN = a+b
    #subN = a-b
    #multiN = a*b
   # divideN =  a/b
    #print("A soma desses números é -> ",somaN ) 
   # print("A subtração desses números é -> ", subN ) 
  #  print("A multiplicação desses números é -> ", multiN ) 
 #   print("A Divisão desses números é -> ", divideN ) 


#calculadora()

##########################################


# 
#bm = input('me fale uma operação? ')

#n =int(input('diga um numero? '))
#n2 =int(input('Outro: '))



#def calculadora():
   # print("Soma", n + n2) 
  #  print("Subtração", n - n2) 
 #   print("Multiplicação", n * n2) 
#    print("Divisão", n / n2) 

#calculadora()


operacao = input("Digite a operacao desejada se é--> (soma, sub, mult, div): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if operacao == "soma":
	resultado = int(numero1) + int(numero2)
if operacao == "sub":
	resultado = int(numero1) - int(numero2)
if operacao == "mult":
	resultado = int(numero1) * int(numero2)
if operacao == "div":
	resultado = int(numero1) / int(numero2)

