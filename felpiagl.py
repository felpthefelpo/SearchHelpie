import tkinter as tk
from googlesearch import search
import webbrowser

ultimas_buscas = []
ultimas_buscas_dict = {}
botoes_buscas = []
links_buscas = []

def search_google(query):
    """Pesquisa no Google a resposta para a pergunta"""
    global link_resposta
    if query in ultimas_buscas_dict:
        link_resposta = ultimas_buscas_dict[query]
    else:
        try:
            link_resposta = next(search(query, num_results=1))
            ultimas_buscas_dict[query] = link_resposta
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
    pergunta = ultimas_buscas[i]
    link = ultimas_buscas_dict.get(pergunta, "")
    botao_busca = tk.Button(text=ultimas_buscas[i], command=lambda i=i: webbrowser.open(link))
    botao_busca.pack(side=tk.TOP)
    botoes_buscas.append(botao_busca)

def sair():
    """Cria o botão para sair do app"""
    janela.destroy()
    
def exibir_informacoes():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Informações")
    nova_janela.geometry("300x200")
    rotulo_versao = tk.Label(nova_janela, text="Versão: Alpha 1.0")
    rotulo_versao.pack()
    rotulo_desenvolvedor = tk.Label(nova_janela, text="Desenvolvido por: Felipe Andrade")
    rotulo_desenvolvedor.pack()
    rotulo_endereco = tk.Label(nova_janela, text="Endereço: Planeta terra :)")
    rotulo_endereco.pack()

# Cria a janela principal
janela = tk.Tk()
janela.title("SearchHelpie :)")

# Cria os widgets da interface gráfica

botao_reset = tk.Button(janela, text="Reset", command=reset, bd=4)
botao_reset.pack(side=tk.RIGHT)
rotulo_link = tk.Label(janela, text="")
rotulo_link.pack(side=tk.TOP)
rotulo_pergunta = tk.Label(janela, text="Em que posso te ajudar?")
rotulo_pergunta.pack(side=tk.TOP)
campo_pergunta = tk.Entry(janela, width=50)
campo_pergunta.pack(side=tk.TOP)
botao_sair = tk.Button(janela, text="Sair", command=sair, bd=4)
botao_sair.pack(side=tk.RIGHT)
botao_informacoes = tk.Button(janela, text="Informações", command=exibir_informacoes, bd=4)
botao_informacoes.pack(side=tk.LEFT)
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=obter_resposta, bd=4)
botao_pesquisar.pack(side=tk.TOP)
rotulo_ultimas_buscas = tk.Label(janela, text="Últimas buscas:")
rotulo_ultimas_buscas.pack(side=tk.TOP)

# Inicia o loop principal da janela
janela.mainloop()