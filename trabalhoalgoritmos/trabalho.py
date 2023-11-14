import pandas as pd

#mostra apenas as cidades
def mostrar_cidades(arquivo):
    df = pd.read_csv(arquivo, delimeter=';', )

    cidades = df['Município']
    
    for cidades in cidades:
        print(cidades)

#mostra cidade e a região
def cidade_regiao(arquivo):
    df = pd.read_csv(arquivo, delimiter=';', encoding='ISO_8859_1')

    cidades = df['Município']
    regiao = df['Região']

    for cidades, regiao in zip(cidades,regiao):
        print(f'{cidades} - {regiao}')


#Mostrar cidade e porte
def cidade_porte(arquivo):
    df = pd.read_csv(arquivo, delimiter=';', encoding='ISO-8859-1')
    
    cidades = df['Município']
    portes = df['Porte']
    
    for cidades, portes in zip(cidades, portes):
        print(f'{cidades} - Porte: {portes}')

#Função gerar o relatorio
def gerar_relatorio(arquivo):
    df = pd.read_csv(arquivo, delimiter=';', encoding='ISO-8859-1')
    
    if 'Unnamed: 9' in df.columns:
        df.drop('Unnamed: 9', axis=1, inplace=True)

    numero_linhas = len(df)
    nomes_colunas = df.columns.to_list()
    
    
    print(f'Número de linhas do documento original: {numero_linhas}')
    print(f'Nomes das colunas que descrevem os dados: {nomes_colunas}')

#mostra o painel para o usuario
def painel(escolha_inicial):
    
    if escolha_inicial == 1:
        escolha2 = int(input(' Escolha 1 para ver o relatório\n 2 para ver as cidades e o porte\n 3 para ver apenas cidades\n 4 para ver as cidades e a região delas:'))
        if escolha2 == 1:
            arquivo = 'municipios.csv'
            gerar_relatorio(arquivo)
        elif escolha2 == 2:
            arquivo = 'municipios.csv'
            cidade_porte(arquivo)
        elif escolha2 == 3:
            arquivo = 'municipios.csv'  
            mostrar_cidades(arquivo) 
        elif escolha2 == 4:
            arquivo = 'municipios.csv'
            cidade_regiao(arquivo)    
    else:
        print('Você saiu')

print("Bem-vindo ao sistema de municípios!")
escolha_inicial= int(input('Escolha 1 para começar ou 0 para sair:'))
painel(escolha_inicial)






