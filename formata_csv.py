# -*- coding: utf-8 -*-
import pandas as pd # type: ignore
import re

# Caminho para o arquivo CSV
file_path = r""
output_file = r""

# Ler o arquivo linha a linha e tratar as vírgulas dos decimais
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

processed_lines = []
for line in lines:
    # Identificar o padrão da penúltima coluna com vírgulas decimais
    line = re.sub(r'(\d+),(\d+)', r'\1.\2', line)  # Substitui vírgulas decimais por pontos
    processed_lines.append(line)

# Escrever as linhas processadas em um novo arquivo temporário
temp_file_path = r""
with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
    temp_file.writelines(processed_lines)

# Ler o arquivo temporário como DataFrame
df = pd.read_csv(temp_file_path, delimiter=',', encoding='utf-8', on_bad_lines='skip')

# Exibir as primeiras linhas para verificar
print("Conteudo do DataFrame:")
print(df.head())

# Salvar o DataFrame em Excel
df.to_excel(output_file, index=False)
print(f"Arquivo salvo como {output_file}")
