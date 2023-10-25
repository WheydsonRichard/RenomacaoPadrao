import os
import re

# Diretório onde estão os arquivos PDF
diretorio = 'C:\\Users\\jur.wheydson\\Downloads\okk'

# Expressão regular para extrair partes do nome do arquivo
padrao = re.compile(r'(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4})')

# Lista todos os arquivos na pasta
for nome_arquivo in os.listdir(diretorio):
    # Verifica se o arquivo é um arquivo PDF
    if nome_arquivo.endswith('.pdf'):
        # Aplica a expressão regular para extrair partes do nome do arquivo
        partes = re.match(padrao, nome_arquivo)
        if partes:
            # Renomeia o arquivo com o padrão desejado
            novo_nome = f'{partes.group(1)}-{partes.group(2)}.{partes.group(3)}.{partes.group(4)}.{partes.group(5)}.{partes.group(6)}.pdf'
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            caminho_novo = os.path.join(diretorio, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f'Arquivo renomeado: {nome_arquivo} para {novo_nome}')
        else:
            print(f'Nome do arquivo não corresponde ao padrão: {nome_arquivo}')
    else:
        print(f'Arquivo {nome_arquivo} não é um arquivo PDF')
