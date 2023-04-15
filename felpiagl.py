import tkinter as tk
from googlesearch import search
import webbrowser

ultimas_buscas = []
botoes_buscas = []
links_buscas = []

def search_google(query):
    """Pesquisa no Google a resposta para a pergunta"""
    global link_resposta
    try:
        link_resposta = next(search(query, num_results=1))
    except StopIteration:
        link_resposta = "Não foi possível encontrar um resultado."
    return link_resposta


def obter_resposta():
    """Obtém a resposta da pesquisa do Google e exibe o link com a fonte da pesquisa"""
    pergunta = campo_pergunta.get()
    resposta = search_google(pergunta)
    rotulo_link.config(text=link_resposta) #atualiza o rótulo com o link
    if len(ultimas_buscas) == 3:
        ultimas_buscas.pop(0) #remove a busca mais antiga
        ultimas_buscas.append(resposta) #adiciona uma nova busca
        links_buscas.pop(0)
        links_buscas.append(link_resposta)
        exibir_ultimas_buscas()
    else:
        ultimas_buscas.append(resposta)
        links_buscas.append(link_resposta)
        botao_busca = tk.Button(janela, text=resposta, command=lambda: webbrowser.open(link_resposta))
        botao_busca.pack(side=tk.TOP)
        botoes_buscas.append(botao_busca)

def reset():
    """Limpa o conteúdo do campo de pergunta e do campo de resposta"""
    campo_pergunta.delete(0, tk.END)
    rotulo_link.config(text="")
    exibir_ultimas_buscas()

def exibir_ultimas_buscas():
    """Exibie as ultimas três buscas efetuadas"""
for botao in botoes_buscas:
    botao.pack_forget()
    botoes_buscas.clear()
for i in range(len(ultimas_buscas)):
    botao_busca = tk.Button(text=ultimas_buscas[i], command=lambda i=i: webbrowser.open(links_buscas[i]))
    botao_busca.pack(side=tk.TOP)
    botoes_buscas.append(botao_busca)

# Cria a janela principal
janela = tk.Tk()
janela.title("SearchHelpie :)")

# Cria os widgets da interface gráfica

rotulo_link = tk.Label(janela, text="")
rotulo_link.pack(side=tk.TOP)
rotulo_pergunta = tk.Label(janela, text="Em que posso te ajudar?")
rotulo_pergunta.pack(side=tk.TOP)
campo_pergunta = tk.Entry(janela, width=50)
campo_pergunta.pack(side=tk.TOP)
botao_reset = tk.Button(janela, text="Reset", command=reset, bd=4)
botao_reset.pack(side=tk.RIGHT)
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=obter_resposta, bd=4)
botao_pesquisar.pack(side=tk.TOP)
rotulo_ultimas_buscas = tk.Label(janela, text="Últimas buscas:")
rotulo_ultimas_buscas.pack(side=tk.TOP)

# Inicia o loop principal da janela
janela.mainloop()