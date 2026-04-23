# Trabalho Prático 5 - DSatur
## Resolução de Problemas com Grafos  
Disciplina: Grafos  
Professor: Ricardo Carubbi  
---
## 📌 Descrição
Este trabalho consiste na implementação do algoritmo **DSatur** para resolver o problema de **coloração de vértices**, aplicado ao mapa político do Brasil.
Cada estado brasileiro foi modelado como um vértice, e cada fronteira terrestre entre estados foi representada como uma aresta não direcionada.
---
## 🎯 Objetivo
- Modelar o mapa do Brasil como um grafo não direcionado  
- Implementar o algoritmo DSatur  
- Produzir uma coloração válida  
- Utilizar o menor número possível de cores  
- Validar automaticamente a solução  
---
## 🧠 Sobre o algoritmo DSatur
O **DSatur (Degree of Saturation)** é uma heurística gulosa para coloração de grafos.
A ideia central é escolher, a cada passo, o vértice mais restrito, ou seja, aquele com maior **grau de saturação**.
### 🔹 Grau de saturação
O grau de saturação de um vértice é a quantidade de **cores diferentes** presentes em seus vizinhos já coloridos.
### 🔹 Critérios de escolha
1. Maior grau de saturação  
2. Em caso de empate → maior grau (mais conexões)  
3. Persistindo empate → escolha arbitrária  
### 🔹 Atribuição de cor
O vértice escolhido recebe a **menor cor disponível** que não cause conflito com seus vizinhos.
---
## 🗺️ Modelagem do problema
- Cada estado brasileiro → vértice  
- Cada fronteira terrestre → aresta  
- Grafo não direcionado  
- Representação: lista de adjacência (algs4)  
Os vértices foram indexados conforme exigido pelo enunciado (ordem alfabética das siglas).
---
## 🗂 Estrutura do projeto

T5/
├── README.md
├── dados/
│   └── brasil.txt
└── src/
├── main.py
├── graph.py
└── dsatur.py

---
## ▶️ Como executar
No terminal, dentro da pasta do projeto:
```bash
python3 src/main.py dados/brasil.txt

⸻

📈 Resultado obtido

* Coloração válida encontrada
* Total de cores utilizadas: 4
* Resultado consistente com o Teorema das Quatro Cores

⸻

🧪 Execução realizada

Exemplo de saída do programa:

Total de cores: 4  
Coloração válida? True

Isso confirma que a solução gerada atende às restrições do problema.

⸻

✅ Validação da solução

A coloração é considerada válida quando:

* Nenhum vértice adjacente possui a mesma cor

O programa realiza automaticamente essa verificação ao final da execução.

⸻

🎥 Vídeo explicativo

Link do vídeo:

👉 COLE AQUI O LINK DO SEU VÍDEO

⸻

⚠️ Observações

* O algoritmo DSatur é uma heurística, portanto não garante sempre o número cromático mínimo
* Nenhuma biblioteca externa de grafos foi utilizada
* Foi utilizada a base algs4, conforme exigido pelo enunciado
