# README: Análise de Contatos entre Proteínas em Trajetória do GMX 

# AVISO 

<i> Este repositório está em fase de testes e pode apresentar instabilidade ou erros. Use com cautela, se encontrar erros, nos reporte.

<h1></h1>

Este projeto realiza a análise de contatos entre proteínas utilizando scripts para gerar estatísticas de contato e gráficos de calor baseados nesses dados.

## Fluxo de Análise

1. **Ordenar contatos**:
   O arquivo de contatos gerado (`contact_AB.dat`) é ordenado numericamente, adicionando uma linha em branco no início e a palavra `END` no final.

2. **Converter para formato xyz-matrix**:
   O arquivo ordenado é transformado no formato xyz-matrix usando um script AWK.

3. **Gerar gráfico de calor**:
   O gráfico de calor é criado a partir do arquivo xyz-matrix utilizando um script Gnuplot.

## Arquivos e Scripts

- `contact_AB.dat`: Arquivo com os dados de contatos entre proteínas.
- `transform-to-xyzmatrix.awk`: Script AWK para converter os dados no formato xyz-matrix.
- `heatmapplot.gnu`: Script Gnuplot para gerar o gráfico de calor.
- `contact_analysis.py`: Script Python que automatiza todo o fluxo de análise.

## Como Obter o Arquivo `contact_AB.dat`

O arquivo `contact_AB.dat` pode ser gerado utilizando o script `newcontacts.tcl` no VMD (Visual Molecular Dynamics). Siga as etapas abaixo:

1. Abra o VMD e carregue a trajetória da simulação molecular.
2. Carregue o script `newcontacts.tcl` no VMD.
3. Execute o script no VMD para analisar os contatos entre as proteínas A e B ao longo da trajetória.
4. Após a execução, o arquivo `contact_AB.dat` será gerado com as estatísticas dos contatos.
5. Mova o arquivo gerado para o mesmo diretório dos outros scripts para prosseguir com a análise.

## Pré-requisitos

- **Python 3.x**
- **GNU Awk**
- **Gnuplot**
- **VMD (Visual Molecular Dynamics)**

Certifique-se de que todas as ferramentas acima estão instaladas e disponíveis no seu ambiente.

## Como Usar

1. **Prepare os arquivos**:
   - Certifique-se de ter o arquivo `contact_AB.dat` na mesma pasta que o script Python.
   - Coloque o script AWK e o script Gnuplot na mesma pasta.

2. **Configure os parâmetros**:
   Abra o arquivo `contact_analysis.py` e ajuste os seguintes parâmetros, se necessário:
   - `init_res`: Número inicial de resíduos da proteína A.
   - `final_res`: Número final de resíduos da proteína A.

3. **Execute o script**:
   No terminal, execute o comando:
   ```bash
   python contact_analysis.py
   ```

4. **Saída**:
   - O arquivo ordenado será salvo como `transform-to-xyzmatrix.in`.
   - O arquivo no formato xyz-matrix será salvo como `transform-to-xyzmatrix.out`.
   - O gráfico de calor será salvo como `heatmap_output.png`.

## Observações

- O script Python automatiza o uso do AWK e do Gnuplot, garantindo um fluxo integrado.
- Certifique-se de ajustar os caminhos no dicionário `define_paths` do script Python, se necessário.
- Caso deseje usar outra ferramenta para gerar o gráfico, o arquivo `transform-to-xyzmatrix.out` pode ser reutilizado.

## Contato
Em caso de dúvidas ou problemas, entre em contato com o desenvolvedor do script.

