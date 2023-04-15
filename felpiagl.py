import tkinter as tk
from googlesearch import search
import webbrowser

def search_google(query):
    """Pesquisa no Google a resposta para a pergunta"""
    global link_resposta
    try:
        link_resposta = next(search(query, num_results=1))
    except StopIteration:
        link_resposta = "Não foi possível encontrar uma resposta para a pergunta."
    return link_resposta


def obter_resposta():
    """Obtém a resposta da pesquisa do Google e exibe-a no painel de resposta"""
    pergunta = campo_pergunta.get()
    resposta = search_google(pergunta)
    rotulo_link.config(text=link_resposta) #atualiza o rótulo com o link
    campo_resposta.config(state='normal')
    campo_resposta.delete('1.0', tk.END)
    campo_resposta.insert(tk.END, resposta)
    campo_resposta.config(state='disabled')

def abrir_link():
    """Abre o link no navegador padrão do sistema"""
    resposta = rotulo_link.cget("text")
    webbrowser.open(resposta)

def reset():
    """Limpa o conteúdo do campo de pergunta e do campo de resposta"""
    campo_pergunta.delete(0, tk.END)
    campo_resposta.config(state='normal')
    campo_resposta.delete('1.0', tk.END)
    campo_resposta.config(state='disabled')

# Cria a janela principal
janela = tk.Tk()
janela.title("SearchHelpie :)")

# Cria os widgets da interface gráfica
rotulo_link = tk.Label(janela, text="")
botao_abrir_link = tk.Button(janela, text="Abrir link", command=abrir_link)
botao_abrir_link.pack(side=tk.TOP)
rotulo_link.pack(side=tk.TOP)
botao_reset = tk.Button(janela, text="Reset", command=reset)
botao_reset.pack(side=tk.TOP)

rotulo_pergunta = tk.Label(janela, text="Em que posso te ajudar?")
rotulo_pergunta.pack(side=tk.TOP)
campo_pergunta = tk.Entry(janela, width=50)
campo_pergunta.pack(side=tk.TOP)
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=obter_resposta)
botao_pesquisar.pack(side=tk.TOP)
rotulo_resposta = tk.Label(janela, text="Resultado da busca:")
rotulo_resposta.pack(side=tk.TOP)
campo_resposta = tk.Text(janela, width=50, height=10, state='disabled')
campo_resposta.pack(side=tk.TOP)

# Inicia o loop principal da janela
janela.mainloop()