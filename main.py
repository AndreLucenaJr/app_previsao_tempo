#todos os importes
import requests
from pprint import pprint
import tkinter as tk
from tkinter import messagebox


#Configuração da API key
API_key = '1a05332c99683ae41d8eb54519e6d058'



#Funcão criada pra checar os dados do tempo baseado na cidade escolhida
def checar_tempo():
    cidade = cidade_entry.get()
    base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+ API_key + '&q='+ cidade

    #checar por possiveis erros usando try e except
    try:
        #tranformando o resposta do base_url em json
        dados_tempo = requests.get(base_url).json()
        listar_dados(dados_tempo)
    
    except Exception as e:
        messagebox.showerror('"Erro", f"Erro ao buscar dados: {str(e)}"')


#Função criada para fazer a listagem dos dados do tempo de mandeira organizada
def listar_dados(dados):
    resultado.config(state="normal")
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, "Dados do Tempo:\n")
    resultado.insert(tk.END, f"Cidade: {dados['name']}\n")
    resultado.insert(tk.END, f"País: {dados['sys']['country']}\n")
    resultado.insert(tk.END, f"Temperatura: {dados['main']['temp']} °C\n")
    resultado.insert(tk.END, f"Condição: {dados['weather'][0]['description']}\n")
    resultado.insert(tk.END, f"Umidade: {dados['main']['humidity']}%\n")
    resultado.insert(tk.END, f"Pressão: {dados['main']['pressure']} hPa\n")
    resultado.config(state="disabled")


#Configurando a janela do Tkinter
root = tk.Tk()
root.title('Previsão do tempo atual')

#Criação dos widgets interativos do app
janela = tk.Frame(root)
janela.pack(padx=20, pady=20)

#widget da escolha da cidade
label = tk.Label(janela, text = 'Digite o nome da cidade:')
label.pack

cidade_entry = tk.Entry(janela)
cidade_entry.pack()

#Criação do botao para buscar os dados
buscar_button = tk.Button(janela, text = 'Buscar Dados do Tempo', command = checar_tempo)
buscar_button.pack()

resultado = tk.Text(janela, wrap=tk.WORD, width=60, height=20, state="disabled")
resultado.pack()

#Roda o app
root.mainloop()