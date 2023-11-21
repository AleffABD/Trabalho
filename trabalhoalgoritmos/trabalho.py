import pandas as pd

#Trabalho algoritimos
#Aluno:Aleff Abdala

#função que cria um dataframe
def carregar_dados(arquivo):
    return pd.read_csv(arquivo, delimiter=';', encoding='ISO-8859-1')

#função que mostra as cidades
def mostrar_cidades(df):
    for cidade in df['Município']:
        print(cidade)

#função que mostra a cidade e a região
def cidade_regiao(df):
    for cidade, regiao in zip(df['Município'], df['Região']):
        print(f'{cidade} - {regiao}')

#funçao que mostra a cidade e o porte 
def cidade_porte(df):
    for cidade, porte in zip(df['Município'], df['Porte']):
        print(f'{cidade} - Porte: {porte}')

#função que busca uma cidade 
def buscar_cidade(df, nome_cidade):
    if 'Unnamed: 9' in df.columns:
        df = df.drop('Unnamed: 9', axis=1)

    cidade = df[df['Município'].str.contains(nome_cidade, case=False)]
    
    if not cidade.empty:
        print(cidade)
    else:
        print(f'A cidade {nome_cidade} não foi encontrada.')

#Função que cria um arquivo filtrado   
def arquivo_filtrado(df):
    coluna_filtro = input(f'Informe a coluna para filtragem: ').strip()
    tipo_filtro = input(f'Informe o tipo de filtragem desejada para a coluna {coluna_filtro}: ').strip()

    if coluna_filtro not in df.columns:
        print(f'Coluna {coluna_filtro} não encontrada.')
        return

    df_filtrado = df[df[coluna_filtro].str.contains(tipo_filtro, case=False)]

    if df_filtrado.empty:
        print(f'Nenhum dado encontrado com os critérios de filtragem fornecidos.')
        return

    nome_arquivo = input(f'Informe o nome do arquivo para salvar os dados filtrados (inclua a extensão .csv): ').strip()
    df_filtrado.to_csv(nome_arquivo, index=False)

    print(f'Arquivo {nome_arquivo} foi criado com sucesso com os dados filtrados.')    
    print(f'\nGerando relatório do arquivo filtrado...')
    gerar_relatorio(nome_arquivo)

#Função que mostra apenas as cidades capitais
def cidades_capitais(df):
    cidades_capital = df[df['Capital'] == "Capital"]

    print(f'As cidades capitais são:')
    for nome_cidade in cidades_capital['Município']:
        print(f'{nome_cidade}')

#Funçao que cria um arquivo de resumo
def arquivo_resumo(df):
    coluna = input('Informe uma coluna para o resumo: ').strip()
    nome_arquivo = input('Informe o nome do arquivo de resumo: ').strip()

    if coluna not in df.columns or 'População 2010' not in df.columns:
        print(f'A coluna "{coluna}" ou "População 2010" não está presente no DataFrame.')
        return

    resumo = df.groupby(coluna)['População 2010'].agg(['size', 'mean'])
    resumo.rename(columns={'size': 'Contagem de Cidades', 'mean': 'Média da População'}, inplace=True)
    resumo['Média da População'] = resumo['Média da População'].round(2)
    resumo = resumo.reset_index()
    resumo.to_csv(nome_arquivo, index=False)

    print(f'Arquivo de resumo {nome_arquivo} criado com sucesso. Ele contém a contagem de cidades e a média da população por {coluna}.')

#Função que Gerar um relatorio
def gerar_relatorio(arquivo):
    df = pd.read_csv(arquivo, delimiter=';', encoding='ISO-8859-1')
    numero_linhas = len(df)
    nomes_colunas = df.columns.tolist()  

    print(f'Número de linhas do documento: {numero_linhas}')
    print(f'Nomes das colunas: {nomes_colunas}')

#Mostrar os dados estatisticos da população
def dados_estatisticos(df):
    
    coluna = 'População 2010' 

    if coluna not in df.columns:
        print(f"Coluna '{coluna}' não encontrada.")
        return

    dados_coluna = df[coluna]

    if not pd.api.types.is_numeric_dtype(dados_coluna):
        print(f"A coluna '{coluna}' não contém dados numéricos.")
        return
       
    media = dados_coluna.mean()
    mediana = dados_coluna.median()
    moda = dados_coluna.mode()[0]  
    desvio_padrao = dados_coluna.std()

    print(f"\nAnálise Estatística da Coluna '{coluna}':")
    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Desvio Padrão: {desvio_padrao}")

    

#Painel de escolha do usuário
def painel():
    while True:
        escolha1 = int(input(f'Escolha 1 para começar ou 0 para sair:'))
        if escolha1 == 0:
            print(f'Você saiu.')
            break
        elif escolha1 == 1:
            arquivo = 'trabalhoalgoritmos/municipios.csv'
            dados = carregar_dados(arquivo)
            while True:
                escolha2 = int(input(f'0 para sair\n1 para ver o relatório\n2 para ver as cidades e o porte\n3 para ver apenas cidades\n4 para ver as cidades e a região delas\n5 para ver quais cidades são capital\n6 para pesquisar uma cidade\n7 para criar um arquivo de resumo com informações estatisticas\n8 para criar um arquivo com informações filtradas\n9 para ver os dados estatisticos da população: '))
                if escolha2 == 0:
                    print(f'Você saiu do painel de opções.')
                    break
                elif escolha2 == 1:
                    gerar_relatorio(arquivo)
                elif escolha2 == 2:
                    cidade_porte(dados)
                elif escolha2 == 3:
                    mostrar_cidades(dados)
                elif escolha2 == 4:
                    cidade_regiao(dados)
                elif escolha2 == 5:
                    cidades_capitais(dados)
                elif escolha2 == 6:
                    nome_cidade = input(f'Digite o nome da cidade que deseja procurar: ')
                    buscar_cidade(dados, nome_cidade)  
                elif escolha2 == 7:
                    arquivo_resumo(dados)     
                elif escolha2 == 8:
                    arquivo_filtrado(dados)  
                elif escolha2 == 9:
                    dados_estatisticos(dados)      
                else:
                    print(f'Escolha inválida. Tente novamente.')
        else:
            print(f'Digite um numero válido')

print(f'Bem-vindo ao sistema de municípios!')
painel()