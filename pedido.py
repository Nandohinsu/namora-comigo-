import tkinter as tk
import random
import webbrowser

janela = tk.Tk()
janela.title("Namora comigo?")
janela.geometry("600x400")
janela.configure(bg="pink")

texto = tk.Label(
    janela,
    text="💖 Aceita namorar comigo? 💖",
    font=("Arial", 22, "bold"),
    bg="pink"
)
texto.pack(pady=40)


def clicar_sim():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")


def fugir():
    largura = janela.winfo_width()
    altura = janela.winfo_height()

    x = random.randint(0, largura - 100)
    y = random.randint(0, altura - 50)

    botao_nao.place(x=x, y=y)

botao_sim = tk.Button(
    janela,
    text="SIM 💘",
    font=("Arial", 14, "bold"),
    bg="lightgreen",
    command=clicar_sim
)

botao_sim.place(x=180, y=250)


botao_nao = tk.Button(
    janela,
    text="NÃO 😢",
    font=("Arial", 14, "bold"),
    bg="tomato"
)

botao_nao.place(x=320, y=250)


botao_nao.bind("<Enter>", lambda e: fugir())

janela.mainloop()