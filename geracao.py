"""
GERAÇÃO

Este módulo faz os cálculos randômicos e cria um GUI.

"""
from tkinter import *
from tabelas import *

# passo 1: Escolher raça e profissão -> Usuário (todos as demais escolhas serão randômicas)


class Application:
    def __init__(self, master=None, **kwargs):
        self.widget1 = Frame(master)
        self.widget1["width"] = 102
        self.widget1["bg"] = "black"
        self.widget1.pack()  # gerenciador de layout

        self.tagmar = Label(self.widget1, image=foto) # insere imagem inicial
        self.tagmar.pack(side=TOP, pady=30)

        self.txt = Label(self.widget1)
        self.txt["font"] = ("Calibri", "12")
        self.txt["text"] = "Programa para criação de personagens semi aleatórios.\n"\
                           "Você escolhe a raça e em seguida a profissão. \n\n" \
                           "Todos os dados restantes serão determinados pelo programa."  # insere texto
        self.txt.pack(side=TOP, ipadx=15, ipady=10)

        self.esq = Label(self.widget1, width=50)
        self.esq["font"] = ("Calibri", "12")
        self.esq["text"] = "Escolha a raça do personagem: "
        self.esq.pack(side=LEFT, pady=30, padx=30, ipadx=15, ipady=10)

        self.dir = Label(self.widget1, width=50)
        self.dir.pack(pady=30, ipadx=15, ipady=10)

        raca.set("L")
        for texto in racas:
            b = Radiobutton(self.dir, text=texto, variable=raca, value=texto)
            b.pack(anchor=W)

        """ Outra maneira:
        self.raca = Radiobutton(self.dir, text="Humano", variable=raca, value="Humano").pack(anchor=W)
        self.raca = Radiobutton(self.dir, text="Meio-elfo", variable=raca, value="Meio-elfo").pack(anchor=W)
        self.raca= Radiobutton(self.dir, text="Elfo florestal", variable=raca, value="Elfo florestal").pack(anchor=W)
        self.raca = Radiobutton(self.dir, text="Elfo dourado", variable=raca, value="Elfo dourado").pack(anchor=W)
        self.raca = Radiobutton(self.dir, text="Anão", variable=raca, value="Anão").pack(anchor=W)
        self.raca = Radiobutton(self.dir, text="Pequenino", variable=raca, value="Pequenino").pack(anchor=W)
        """


def callback():
    print("called the callback!")


root = Tk()

raca = StringVar()

menu = Menu(root)
menu.add_cascade(label="Arquivo", menu=root)
menu.add_command(label="Novo", command=callback)
menu.add_command(label="Abrir...", command=callback)
menu.add_separator()
menu.add_command(label="Sair", command=callback)
helpmenu = Menu(menu)
menu.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Sobre...", command=callback)


foto = PhotoImage(file="tagmar.gif")     # variável foto
Application(root)  # nome do pacote
root.title("Personagens Automáticos - TAGMAR")  # título janela principal
root.config(bg="black", menu=menu)              # cor janela principal e menus
root.geometry("1000x650+10+10")                 # tamanho da janela principal
mainloop()
