import tkinter as tk
import re
from calculadora import calcular

janela = tk.Tk()

janela.title("calculadora")
janela.geometry("400x500")


visor= tk.Entry(janela, width = 30, font = ("Arial", 12))
visor.grid(row=0, column=0, columnspan=3)

def adicionar_numero(numero):
    visor.insert(tk.END, numero) #tk.end insere o número no final da string que está no visor, ou seja, se o visor tiver 1 e eu clicar em 2, ele vai ficar 12 e não 21

def adicionar_operador(operador):
    visor.insert(tk.END, operador)

def calcular_resultado():
    expressao = visor.get()
    padrao = r'^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$' #utilizado para validar a expressão, ou seja, para verificar se a expressão está no formato correto. O padrão é uma expressão regular que verifica se a expressão tem o formato "número operador número", onde o número pode ser inteiro ou decimal, e o operador pode ser +, -, * ou /. O ^ indica que a expressão deve começar com o padrão, e o $ indica que a expressão deve terminar com o padrão. O -? indica que o número pode ser negativo, e o (?:\.\d+)? indica que o número pode ter uma parte decimal opcional.
    resultado_regex = re.match(padrao, expressao)               #serve para verificar se a expressão está no formato correto, ou seja, se ela tem o formato "número operador número". Se a expressão estiver no formato correto, o resultado_regex vai conter os grupos correspondentes ao número 1, operador e número 2. Se a expressão não estiver no formato correto, o resultado_regex vai ser None.


    if not resultado_regex:
        return

    num1 , operador , num2 = resultado_regex.groups() # serve para extrair os grupos correspondentes ao número 1, operador e número 2 da expressão. O método groups() retorna uma tupla com os grupos correspondentes à expressão regular. No caso, a tupla vai conter o número 1, operador e número 2, que são atribuídos às variáveis num1, operador e num2, respectivamente.

def apagar_numero():
    
    if visor.get() == "":
         return 
    else:
        visor.delete(len(visor.get())-1, tk.END)  # apaga o último caractere do visor

def trocar_sinal():
    expressao=visor.get()
    converter = float(expressao) *-1
    visor.delete(0,tk.END)
    visor.insert(tk.END,converter)
    

botao = tk.Button(janela, text ="7", command=lambda: adicionar_numero("7"))  # o lambda é usado para criar uma função anônima, ou seja, uma função que não tem nome. Ele é usado aqui para passar o parâmetro "7" para a função adicionar_numero quando o botão for clicado.
botao.grid(row = 1, column=0, ipadx= 10)                                        #lambda também faz com que a função seja executada apenas quando o botão for clicado, e não quando o programa for iniciado.

botao = tk.Button(janela, text ="8", command=lambda: adicionar_numero("8"))
botao.grid(row = 1, column=1, ipadx= 10)

botao = tk.Button (janela, text ="9", command=lambda: adicionar_numero("9"))
botao.grid(row = 1, column=2, ipadx= 10)

botao = tk.Button (janela, text ="4", command =lambda: adicionar_numero("4"))
botao.grid(row = 2, column=0, ipadx= 10)

botao = tk.Button (janela, text ="5", command =lambda: adicionar_numero("5"))
botao.grid(row = 2, column=1, ipadx= 10)

botao = tk.Button (janela, text ="6", command =lambda: adicionar_numero("6"))
botao.grid(row = 2, column=2, ipadx= 10)

botao = tk.Button (janela, text ="1", command=lambda: adicionar_numero("1"))
botao.grid(row = 3, column=0, ipadx= 10)

botao = tk.Button (janela, text ="2", command=lambda: adicionar_numero("2"))
botao.grid(row = 3, column=1, ipadx= 10)

botao = tk.Button (janela, text ="3", command=lambda: adicionar_numero("3"))
botao.grid(row = 3, column=2, ipadx= 10)

botao = tk.Button(janela, text = "0", command=lambda: adicionar_numero("0"))
botao.grid(row = 4 , column = 1 , ipadx= 10)

botao = tk.Button(janela, text = ".", command=lambda: adicionar_numero("."))
botao.grid(row = 4 , column = 0, ipadx= 11)

botao = tk.Button(janela, text = "=", command=calcular_resultado)
botao.grid(row = 4 , column = 2, ipadx= 10)

botao = tk.Button(janela, text = "+", command=lambda: adicionar_operador("+"))
botao.grid(row = 1 , column = 3, ipadx= 10)

botao = tk.Button(janela, text = "x", command = lambda: adicionar_operador("*") )
botao.grid(row = 2 , column = 3, ipadx= 10)

botao = tk.Button(janela, text = "/", command=lambda: adicionar_operador("/"))
botao.grid(row = 3 , column = 3, ipadx= 10)

botao = tk.Button(janela, text = "-", command=lambda: adicionar_operador("-"))
botao.grid(row = 4 , column = 3, ipadx= 10)

botao = tk.Button(janela, text = "C", command=lambda: visor.delete(0, tk.END))  # o comando delete apaga o conteúdo do visor, e o parâmetro 0 indica que ele deve apagar desde o início da string até o final (tk.END)
botao.grid(row = 5 , column = 1, ipadx= 10)

botao = tk.Button(janela, text = "⌫", command=lambda: apagar_numero())
botao.grid(row = 5 , column = 2, ipadx= 10)

botao = tk.Button(janela, text = "±", command=lambda: trocar_sinal())
botao.grid(row = 5 , column = 3, ipadx= 10)


janela.mainloop()
