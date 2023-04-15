import tkinter as tk
from googlesearch import search
import webbrowser

def search_google(query):
    """Pesquisa no Google a resposta para a pergunta"""
    try:
        resposta = next(search(query, num_results=1))
    except StopIteration:
        resposta = "Não foi possível encontrar uma resposta para a pergunta."
    return resposta


def obter_resposta():
    """Obtém a resposta da pesquisa do Google e exibe-a no painel de resposta"""
    pergunta = campo_pergunta.get()
    resposta = search_google(pergunta)
    webbrowser.open(resposta) # abre o link no navegador padrão do sistema
    campo_resposta.config(state='normal')
    campo_resposta.delete('1.0', tk.END)
    campo_resposta.insert(tk.END, resposta)
    campo_resposta.config(state='disabled')

# Cria a janela principal
janela = tk.Tk()
janela.title("Automação de perguntas e respostas do Google")

# Cria os widgets da interface gráfica
rotulo_pergunta = tk.Label(janela, text="Pergunta:")
rotulo_pergunta.pack(side=tk.TOP)
campo_pergunta = tk.Entry(janela, width=50)
campo_pergunta.pack(side=tk.TOP)
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=obter_resposta)
botao_pesquisar.pack(side=tk.TOP)
rotulo_resposta = tk.Label(janela, text="Resposta:")
rotulo_resposta.pack(side=tk.TOP)
campo_resposta = tk.Text(janela, width=50, height=10, state='disabled')
campo_resposta.pack(side=tk.TOP)

# Inicia o loop principal da janela
janela.mainloop()