import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dados = pd.read_csv("StudentsPerformance.csv")



notas = dados["math score"].to_numpy()      

print(f"media dasnotas de matematica:{np.mean(notas)}")                      
print(f"mediana das notas de matematica:{np.median(notas)}")                     
print(f"desvio-padrão amostral de matematica:{np.std(notas, ddof=1)}")               
print(np.percentile(notas, [10, 25, 50, 75, 90]))   
print(np.corrcoef(dados["reading score"], dados["math score"]))  
#tamanho da base de dados 1007 linhas e 8 colunas
print(dados.shape)

#nome das variaveis
print(dados.columns)

#Tipos de dados
print(dados.dtypes)

#primeiras observaçoes
print(dados.head)
#dados ausentes
print(dados.isnull().sum())

#PROBLEMA 1
#a) Students performace
#b)Kaggle
#c)Cada linha da base de dados represent um estudante
#d) existem 1000 observações
print(dados.shape[0])
#e)existem 8 variaveis
print(dados.shape[1])
#f)As variaveis math score, reading score e writing score sao quantitativas.
#g)Gender, race, parental level of education, lunch.

#h)Não.
#i)Investigarem se Fatores socioeconômicos e educacionais estão associados ao desempenho acadêmico dos estudantes.

#PARTE 2
#A) A variavel escolhida foi math score
#b) representa a nota obtida por cada aluno
''' Existe diferença de desempenho entre os grupos de estudantes?RESPOSTA:SIM'''
'''O tipo de alimentação está associado ao desempenho??SIM'''
''' A escolaridade dos pais está associada às notas dos filhos?'''
print(dados.info())
print(dados.isnull().sum())
print(dados[["math score", "reading score", "writing score"]].agg(["mean", "median"]))
print(dados.groupby("race/ethnicity")["math score"].agg(['mean','median']))
#Nota-se que existem uma grande diferença na media e na mediana de notas de matematica entre os grupos, o grupo E com media 73.8 e o grupo A com media 61.6d
print(dados.groupby('lunch')["math score"].agg(["mean","median"]))

''' existe tambem uma grande diferença nas medias das notas em matematica nos grupos.
o grupo que teve o almoço reduzido teve a media de 58.9 
e o grupo em que o almoço foi normal a media foi de 70'''

print(dados.groupby("parental level of education")["math score"].agg(["mean","median"]))

''' Observamos que a escolaridade dos pais 
afeta proporcionalmente as notas dos alunos.'''
#parte 3
'''a) é a nota media dos 1000 estudantes em matematica. media = 66,09'''

'''b) é a nota que divide os valores na metade. mediana = 66 '''

'''c)A media e a mediana são muito semelhantes a variaça é menor que 1'''

'''d)a media e mediana serem proximas indica que a distribuição é simétrica,
        sem valores extremos(outliers)distorcendo'''
print(dados["math score"].mode())
'''e) existem mode e ela é 65 em matematica mas não possue significância'''
'''f) a mediana pois ela é resistente a outliers mas poderia ser a media tambem pois estao bem parecidas '''
print(dados["math score"].value_counts())

#PARTE IV
notas = ["math score", "writing score", "reading score"]
print(dados[notas].describe())
print(dados[notas].quantile([0.10,0.90]))
#observando o dados 25% dos alunos tiraram ate 57 pontos na prova de matematica
#50% tirou ate 66 pontos que é a media da turma
#75 tirou ate 77 pontos 
#observando o percentil 10 vemos que os 10% piores da turma tiraram 47 pontos
#o percentil 90 vemos que 10% tirou acuma de 86 pontos
'''conseguimos observar aproximadamente pelas essa novas analises que 10% dos alunos com menor nota ate o minimo tem uma diferença
maior do que o 10% melhor ate o maximo.Isso representa uma boa nota dos alunos e uma cauda baixa. '''

#PARTE V
variancia = dados[notas].var() # variancia amostral
desvio = dados[notas].std() # desvio padrao
amplitude = dados[notas].max() - dados[notas].min()
cv = dados[notas].std() / dados[notas].mean()
iqr = dados[notas].quantile(0.75) - dados[notas].quantile(0.25)# amplitude interquartil
dam = (dados[notas] - dados[notas].mean()).abs().mean() # desvio absoluto medio

resumo = pd.DataFrame({
    "Variância": variancia,
    "Desvio padrão": desvio,
    "Amplitude": amplitude,
    "CV (%)": cv,
    "IQR": iqr,
    "Desvio abs. médio": dam
})
print(resumo.round(2))
print(amplitude) #a)a amplitude de matematica é de 100 de writing score é 90 e reading score 83.
#b) Moderado. Com o desvio padrao de aproximadamente 15 numa escala de 0 a 100 os alunos costumamficar 15 pontos abaixo ou acima da media.
#c)Variabilidade moderada tem alunos com desempenhos altos e alunos com desempenhos um pouco abaixo da media.
print(cv)
'''d)Sim. com cv em torno de 21% a 23% podemos observar que a dispersão é moderada em releção a media
e a variabilidade é parecida entre as disciplinas'''
'''e) Sim. a amplitude total é influenciada pelos valores extremos como o aluno que tirou 0 em matematica.
ja o IQR considera so os 50%, os dados centrais, entre o Q1 e o Q3, mostrando que a maioria que dos alunos 
se concentra numa zona mais estreita '''
'''f)Sim.Nas 3 avaliações existem outliers inferiores. em matematica 8, na escrita 5 e em leitura 5 tambem puxando a media para baixo.'''
print(dados[notas].boxplot())
print(plt.show())
#PARTE VI
print(dados[notas].skew())# assimetria
print(dados[notas].kurt())# curtose
#a) a destrubição de certa forma é simetrica, as assimetrias ficam muito proximas a zero.
#b) existe mas bem leve
#c) assimetrias inferiores, isso nos da que temos mais notas baixas.
#d)sim,poucos, existem alguns outliers que puxam um pouco a media para baixo.
#e) sim, nesse caso a media fica abaixo da mediana

#PARTE VII
for c in notas:
    dados[c].hist(bins=20)
    plt.axvline(dados[c].mean(),color = "red", label = "media")
    plt.axvline(dados[c].median(), color = "blue", label = " mediana")
    plt.title(c)
    plt.legend()
    plt.show()

bins = [0,10,20,30,40,50,60,70,80,90,101]
labels =["0-9","10-19","20-29","30-39","40-49"
         ,"50-59","60-69","70,79","80-89","90-100"]

faixas = pd.cut(dados["math score"], bins= bins, labels = labels, right = False)

fa = faixas.value_counts().sort_index()

tabela = pd.DataFrame({"Freq. absoluta":fa,
                        "Freq. Relativa(%)": (fa/ fa.sum() * 100).round(1),
                        "freq. acumulada":fa.cumsum(),
                        "freq. rel. acumulada(%)":(fa.cumsum()/fa.sum()*100).round(1)})


fa.plot(kind="bar")
plt.xlabel("Faixa de nota")
plt.ylabel("Número de alunos")
plt.show()
print(tabela)
#a) o intevalo de 60-69 com 268 alunos
#b) os intervalos de 0-9 e 10-19, empatados com 2 alunos cada
#c) conseguimos ver onde os dados estão mais concentrados e o intervalo com maior numero de ocorrencias
#d)permite ver quantos alunos estão ate derterminada nota
'''E) a maior parte dos alunos ter um desempenho intermediario(67.2%)dos alunos acertaram entre 50 a 79 questões,
poucos alunos tiveram notas muito baixas apenas 4% abaixo de 39 questões e cerca de 16% dos alunos teve nota maior que 80'''

#PARTE VIII
#parte IX histograma
plt.figure(figsize=(9,5))
plt.hist(dados["math score"],bins=20, edgecolor = "black")
plt.axvline(dados["math score"].mean(), color = "red",linestyle ="--" ,label = "media")
plt.axvline(dados["math score"].median(),color = "purple",linestyle ="-" , label = "mediana")
plt.title("distribuição das notas de matematica")
plt.xlabel("nota")
plt.ylabel("numero de alunos")
plt.legend()
plt.savefig("histograma_matematica.png", dpi=150, bbox_inches="tight")
plt.show()
#a) A maior concentração de dados esta entre 60 e 70 pontos
#b) Distribuição é simetríca  com formato de sino
#c) Sim, de 0 a 30 pontos temos poucas observações e no intervalo de 10 a 15 pontos não vemos nenhuma
#d) Sim, a média e a mediana praticamente se sobrepõem, confirmando a simetría
#e)Os números resumem o centro e a dispersão, mas só o gráfico mostra que há um único pico e nos dos lados vai decaindo.


#parte X
#box plot matematica
plt.figure(figsize=(6,6))
plt.boxplot(dados["math score"], tick_labels=["matematicas"])
plt.title("box plot notas de matematica")
plt.ylabel("notas")
plt.savefig("boxplot_matematica.png", dpi=150, bbox_inches="tight")

plt.show()
q1 = dados["math score"].quantile(0.25)
q2 = dados["math score"].median
q3 = dados['math score'].quantile(0.75)
iqr = q3 - q1
lim_inf = q1 - 1.5 * iqr
lim_sup = q3 + 1.5 * iqr

outliers = dados[(dados["math score"] < lim_inf) | (dados["math score"] > lim_sup)]
print(f"o q1 é:{q1},\n o q2 é:{q2}\n o q3 é:{q3}\n limite superior:{lim_sup}\n limite inferior:{lim_inf}")
print(outliers)
#a) a mediana aparece em 66 pontos
#b) o q1 é 57 pontos e o q3 é 77 pontos
#c) Sim aparecerem 8 ocorrencias abaixo do bigode inferior e não ha nenhum superior
#d)parecem observações reais.Esses valores são possivel de se ocorrer visto que a nota maxima é 100 e minima é 0.
'''D) Não.Esses valores representam notas reais de alunos, remover , interferiria em todos as medidas '''


#parte XI
#grafico de barras
ordem = ["some high school","high school","some college","associate's degree","bachelor's degree","master's degree"]
medias = dados.groupby("parental level of education")["math score"].mean().loc[ordem]

plt.figure(figsize =(10,5))
medias.plot(kind="bar",edgecolor = "black",color = "blue")

plt.title("media de matematica por escolaridade dos pais")
plt.xlabel("escolaridade dos pais")
plt.ylabel("nota media de matematica")
plt.xticks(rotation = 30)
plt.ylim(0,100)
plt.tight_layout()
plt.savefig("barras_matematica_pais.png", dpi=150, bbox_inches="tight")
plt.show()
#a) Se a escolaridade dos pais influência nas notas de matemática dos filhos.
#b) Porque a variavel do eixo x é categórica, o grafico de barras é o ideal para se comparar valores categoricos com numericos.
#c)Nível de escolaridade dos pais dos alunos
#d)A media das notas dos alunos
#e) Em geral quanto maior a escolaridade dos pais, maior a média dos filhos em matemática, mas essa relação não é perfeitamente linear.

# grafico de dispersão 

plt.figure(figsize=(7,6))
plt.scatter(dados["reading score"],dados["math score"], alpha= 0.5)
plt.title("relação entre nota de leitura e nota de matematica")
plt.xlabel("nota de leitura")
plt.ylabel("nota de matematica")
plt.savefig("dispersão_matematica.png", dpi=150, bbox_inches="tight")
plt.show()
print(dados["reading score"].corr(dados["math score"]))

#a) Se os alunos que tiram boas notas em leitura tambem tiram boas notas em matemática
#b) Porque as duas varíaveis são quantitativas e o objetivo é verificar se existe relação entre as duas.
#c) A nota da leitura do aluno.
#d) A nota de matemática do aluno
'''e)Existe uma relação positiva e forte: os pontos formam uma nuvem inclinada para cima,
e a correlação é de 0,82. Em geral, quem tem nota alta em leitura também tem nota alta em matemática
 Mas a relação não é perfeita'''

# grafico de setores
plt.figure()
dados["lunch"].value_counts().plot(kind = "pie",autopct = "%1.f%%")
plt.title("tipo de almoço")
plt.ylabel("")
plt.show()

#parte XII
'''Em grande parte dos grafícos, uma pessoa que nunca viu a base de dados consiguiria compreender bem
Porem a algumas limitações como o nível de escolaridade ser em ingles.'''
#parte XIII
'''1) Analisei uma base com 1000 estudantes e 8 varíaveis: 5 quantitativas(gênero,raça,escolaridade dos pais, tipo de almoço,preparação para o teste)
e 3 categóricas(notas de matemática, notas de leitura, notas de escrita de 0 a 100) cada linha representa um aluno.'''

'''2) A varíavel principal analisada foi notas de matemática'''
''' 3,4,5)A nota de matemática apresentou média 66,1 e mediana 66 isso indica que o aluno medio acerta 2/3 das questões.
O desvio padrão foi de 15,2 pontos e a amplitude interquartil foi de 20 pontos.
Isso indica variabilidade moderada: metade dos alunos está concentrada numa faixa de 20 pontos,
mas há diferenças consideráveis de desempenho entre eles, já que a distância entre o P10 (47) e o P90 (86) passa de 38 pontos.'''

''' 6) A distruibuição é aproximadamente simétrica, em formato de sino e com um unico pico.
Como a média e mediana são proxímas, ambas representas o aluno tipíco.
Existe uma leve assimétria a inferior devido a notas bem baixas.'''

'''7) no boxplot identifiquei 8 outliers inferiores(valores atipicos) de 0 a 26 pontos e nenhum superior.
Não pareceram erros as notas são possíveis e coerentes com as demais notas dos mesmos alunos,
que também foram mal em leitura e escrita'''
''' 8)O histograma mostrou a concentração dos alunos entre 60 e 70 pontos
(a faixa mais comum, com cerca de 27% dos alunos na faixa de 60 a 69), e que cerca de 67% estão entre 50 e 79.
O box plot confirmou os quartis e destacou os outliers abaixo do bigode inferior. 
O gráfico de barras mostrou que a média de matemática tende a subir com a escolaridade dos pais,
e a dispersão evidenciou uma relação positiva e forte entre as notas de leitura e matemática.'''
'''9) O desempenho em matemática,leitura e escrita anda junto.
A correlação entre leitura e matemática é de 0,82, e entre leitura e escrita chega a 0,95.
Isso sugere que alunos que vão bem em uma área tendem a ir bem nas outras.'''

'''Os alunos que concluíram o curso de preparação tiveram média maior em matemática: 69,7
contra 64,1 dos que não fizeram, uma diferença de cerca de 5,6 pontos.'''

'''O tipo de almoço mostrou a maior diferença entre os grupos: alunos com almoço padrão tiveram média de 70 pontos,
enquanto os com almoço gratuito ou reduzido tiveram 58,9 pontos, uma diferença de cerca de 11 pontos.
Como esse tipo de almoço costuma estar ligado à condição socioeconômica, isso sugere que fatores sociais podem estar associados ao desempenho.'''