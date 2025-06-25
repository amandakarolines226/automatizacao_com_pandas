"""Automatiza login e preenchimento de formulário com Selenium e Pandas."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Início do webdriver
drive = webdriver.Chrome()

def selecionar_clicar_escrever(elemento, texto):
    """Clica e escreve em um elemento da página pelo ID."""
    text = drive.find_element(By.ID, elemento)
    text.click()
    text.send_keys(texto)

# Acessa a página de login
drive.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Preenche login e senha
selecionar_clicar_escrever("email", "coisa@gmail.com")
selecionar_clicar_escrever("password", "123")

# Clica no botão de login
botao = drive.find_element(By.ID, "pgtpy-botao")
botao.click()

# Lê a planilha de produtos
ARQUIVO = "c:/Users/Amanda/Downloads/PRODUTOS.csv"
tabela = pd.read_csv(ARQUIVO)

def click_and_write(element_id, valor):
    """Limpa e escreve em um campo pelo ID."""
    elemento = drive.find_element(By.ID, element_id)
    elemento.clear()
    elemento.send_keys(valor)

# Vai para a página da tabela
drive.get("https://dlp.hashtagtreinamentos.com/python/intensivao/tabela")

# Preenche o formulário com os dados
for _, row in tabela.iterrows():
    click_and_write("codigo", row.codigo)
    click_and_write("marca", row.marca)
    click_and_write("tipo", row.tipo)
    click_and_write("categoria", row.categoria)
    click_and_write("preco_unitario", row.preco_unitario)
    click_and_write("custo", row.custo)
    click_and_write("obs", row.obs)

    # Envia o formulário (se necessário para cada linha)
    botao_submit = drive.find_element(By.ID, "pgtpy-botao")
    botao_submit.click()

input("Pressione Enter para fechar o navegador...")
drive.quit()
