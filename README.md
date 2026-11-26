# README.md

# Análise do desempenho de estudantes

Análise exploratória da base **Students Performance in Exams** (1000 estudantes), feita em Python com Pandas, NumPy e Matplotlib.

## Pergunta investigada

Fazer o curso de preparação para as provas está associado a notas mais altas em matemática?

```python
Os alunos que concluíram o curso de preparação tiveram média maior em matemática: 69,7
contra 64,1 dos que não fizeram, uma diferença de cerca de 5,6 pontos.Uma diferença significativa.
```

## Sobre a base de dados

- **Fonte:** https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
- **Observações:** 1000 linhas, cada uma representando um estudante
- **Variáveis:** 8 colunas, sem valores ausentes
- **Variável principal analisada:** nota de matemática (`math score`)

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `gender` | Categórica | Gênero do estudante |
| `race/ethnicity` | Categórica | Grupo de raça/etnia (A a E) |
| `parental level of education` | Categórica ordinal | Escolaridade dos pais |
| `lunch` | Categórica | Tipo de almoço (standard ou free/reduced) |
| `test preparation course` | Categórica | Se concluiu o curso de preparação (none ou completed) |
| `math score` | Quantitativa | Nota de matemática (0 a 100) |
| `reading score` | Quantitativa | Nota de leitura (0 a 100) |
| `writing score` | Quantitativa | Nota de escrita (0 a 100) |

## O que foi feito

- Exploração inicial: dimensões, tipos de dados e valores ausentes
- Medidas de tendência central: média, mediana e moda
- Medidas separatrizes: quartis e percentis (P10 e P90)
- Medidas de dispersão: variância, desvio padrão, amplitude, coeficiente de variação, amplitude interquartil e desvio absoluto médio
- Forma da distribuição: assimetria e curtose
- Tabela de frequência (absoluta, relativa e acumulada) com intervalos de 10 pontos
- Detecção de valores atípicos pelo critério de Tukey (1,5 × IQR)
- Visualizações: histograma, box plot, gráfico de barras e gráfico de dispersão

## Principais resultados

**Nota de matemática**

| Medida | Valor |
| --- | --- |
| Média | 66,1 |
| Mediana | 66 |
| Desvio padrão | 15,2 |
| Q1 / Q3 | 57 / 77 |
| Amplitude interquartil | 20 |
| Assimetria | -0,28 |

A distribuição é aproximadamente simétrica, com leve assimetria à esquerda. Foram encontrados 8 valores atípicos, todos na ponta inferior (notas de 0 a 26). Eles foram mantidos, pois são notas possíveis e coerentes com o desempenho dos mesmos alunos nas outras provas.

**Descobertas**

1. **As notas das três provas andam juntas.** A correlação entre leitura e matemática é de 0,82, e entre leitura e escrita é de 0,95.
2. **O curso de preparação está associado a notas maiores.** Quem concluiu teve média de 69,7 em matemática, contra 64,1 de quem não fez.
3. **O tipo de almoço mostrou a maior diferença entre grupos.** Almoço padrão: média de 70,0. Almoço gratuito ou reduzido: média de 58,9.
4. **A escolaridade dos pais acompanha o desempenho.** A média de matemática sobe de cerca de 62 a 63 pontos (pais com ensino médio ou menos) para cerca de 69 a 70 (graduação ou mestrado).

> **Atenção:** os resultados indicam **associações, não relações de causa e efeito**.
> 

## Gráficos

!Histograma das notas de matemática

!Box plot das notas de matemática

!Média de matemática por escolaridade dos pais

!Leitura x Matemática

## Como executar

1. Instale as bibliotecas:

```
pip install numpy pandas matplotlib
```

1. Deixe o arquivo `StudentsPerformance.csv` na mesma pasta do script.
2. Execute:

```
Trabalho_analise_dados.py
```

## Ferramentas

Python · Pandas · NumPy · Matplotlib

## Autor

Gabriel Gomes da silva e souza · www.linkedin.com/in/gabrielgssouza
