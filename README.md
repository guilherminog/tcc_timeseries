# **Integração de Técnicas de Aprendizado Profundo para Previsão de Vendas no Varejo**
## **Um Estudo de Caso da Walmart**

### **Análise Comparativa de Modelos de Séries Temporais e Redes Neurais**

---

## 📋 **Descrição do Projeto**
Este projeto é uma análise aprofundada da previsão de vendas semanais no varejo, usando dados reais da Walmart. Nosso foco é comparar o desempenho entre métodos tradicionais de séries temporais (ARIMA, SARIMAX) e modelos de aprendizado profundo (LSTM), utilizando uma abordagem data-driven e moderna.

**Diferencial**: Este estudo integra a modelagem de séries temporais com aprendizado profundo, destacando como técnicas avançadas de redes neurais podem superar métodos estatísticos tradicionais em cenários complexos. Além disso, o projeto abrange o desenvolvimento de uma API escalável para previsão em tempo real, facilitando a aplicação prática dos modelos desenvolvidos.

**Links para Visualização do Código e Relatório**:
- 📄 [Visualizar no GitHub NBViewer](https://nbviewer.org/github/guilherminog/tcc_timeseries/blob/main/TCC_PUC_Walmart_sales_forecasting_notebook_Sarimax_LSTM.ipynb)
- 🚀 [Executar no Google Colab](https://colab.research.google.com/drive/1qeJXkiapyZ3O_jVM6WkAUgZUVARAdQqt?usp=sharing)
- 📈 [Relatório Técnico](https://drive.google.com/file/d/1a__3mByg0ND4--p3gK4LR1Z_RA2844q7/view?usp=sharing)
- 📂 [Drive](https://drive.google.com/drive/folders/1ArTjIj6kSaMjbKrxA7yFVbVpTcZsM2Pf?usp=sharing)
---

## 📂 **Estrutura do Projeto**
```
├── AJUSTES_MODELOS
│   ├── SARIMAX.ipynb                # Notebook com análise detalhada do SARIMAX
│   ├── Walmart_forecast_LSTM.ipynb  # Implementação do modelo LSTM
│   └── ajuste_sarimax_por_loja.ipynb # Ajuste do SARIMAX por loja
├── MEMORIA
│   └── LSTM-API - DESENVOLVIMENTO FUTURO
│       ├── app/                     # API FastAPI para deploy
│       ├── models/                  # Modelos salvos
│       ├── monitor/                 # Scripts de monitoramento com Prometheus
│       ├── Dockerfile               # Configuração para containerização
│       └── docker-compose.yml       # Arquivo de orquestração
├── dataset/
├── README.md
└── TCC_PUC_Walmart_sales_forecasting_notebook_Sarimax_LSTM.ipynb
```

---

## ⚙️ **Instalação e Execução**
Para executar o projeto localmente, siga as instruções abaixo:

### 1. Clone o Repositório
```bash
git clone https://github.com/guilherminog/tcc_timeseries.git
cd tcc_timeseries
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Execute os Notebooks
Acesse os notebooks interativos para explorar as análises e resultados detalhados.

---

## 🧠 **Metodologia e Abordagem**
A metodologia segue o padrão **CRISP-DM**, abordando etapas fundamentais de ciência de dados para garantir robustez na análise e reprodutibilidade dos resultados.

1. **Análise Exploratória de Dados (EDA)**:
   - Visualização das distribuições das variáveis (vendas, temperatura, CPI).
   - Análise de correlações entre variáveis exógenas e vendas semanais.
   - Detecção de outliers e tratamento de dados faltantes.

2. **Feature Engineering**:
   - Extração de features sazonais: mês, semana e ano.
   - Inclusão de variáveis externas como preço do combustível e taxa de desemprego para capturar influências econômicas nas vendas.

3. **Modelagem**:
   - **Modelos Tradicionais**: ARIMA, SARIMAX, Prophet, ETS, TBATS. Avaliamos a performance de modelos robustos e amplamente utilizados para séries temporais.
   - **Aprendizado Profundo**: Implementação de LSTM com técnicas de regularização (Dropout) e ajuste de hiperparâmetros usando RMSprop, Early Stopping e análise de validação cruzada.

4. **Avaliação de Desempenho**:
   - Utilização das métricas **RMSE**, **MAPE** e **R²** para comparação.
   - Análise dos resíduos para identificar possíveis padrões não capturados pelos modelos.

---

## 📊 **Resultados e Discussão**
A análise comparativa demonstrou os seguintes pontos:

- **Desempenho do LSTM**: O modelo LSTM apresentou o melhor desempenho geral, com menor RMSE e maior precisão em capturar padrões complexos e não lineares. Sua capacidade de modelar dependências de longo prazo o torna ideal para cenários de alta complexidade.
- **Desempenho do SARIMAX**: O SARIMAX foi eficaz em capturar a sazonalidade e padrões autocorrelacionados, especialmente em lojas com menor variabilidade nas vendas. No entanto, mostrou limitações em lojas com padrões não lineares, onde o LSTM se destacou.
- **Impacto das Variáveis Exógenas**: A inclusão de variáveis como CPI e preço do combustível melhorou significativamente o desempenho dos modelos, indicando forte correlação com as vendas semanais.

---

## 📈 **Visualizações**
- **Gráficos de Previsões**: Comparação das previsões dos modelos SARIMAX e LSTM para todas as 45 lojas.
- **Análise Exploratória**: Distribuições das variáveis e análise de outliers.
- **Top 5 Lojas**: Desempenho das lojas com melhores resultados, destacando o impacto de variáveis externas.

---

## 🔍 **Conclusão**
Este estudo evidencia a eficácia do uso de aprendizado profundo para previsões de vendas complexas. Enquanto o SARIMAX é eficiente para padrões sazonais e variáveis controladas, o LSTM demonstrou superioridade em cenários com alta variabilidade e dependências complexas. A integração de técnicas de aprendizado profundo mostrou-se uma abordagem promissora, especialmente para dados de alta dimensionalidade e complexidade.

---

## 🚀 **Trabalhos Futuros e Aplicabilidade**
- **Otimização de Hiperparâmetros**: Aplicar técnicas avançadas de otimização como Optuna para melhorar o desempenho.
- **Exploração de Modelos Híbridos**: Combinar CNNs e LSTM para capturar padrões espaciais e temporais simultaneamente.
- **Deploy e Monitoramento**: Desenvolvimento de uma API escalável com Docker e FastAPI, incluindo monitoramento contínuo com Prometheus para assegurar desempenho e disponibilidade.

---

## 💡 **Diferenciais e Impacto do Projeto**
- **Integração de Aprendizado Profundo e Modelagem Tradicional**: Combinação inovadora que maximiza a capacidade preditiva e oferece insights valiosos para a tomada de decisão.
- **Escalabilidade e Aplicabilidade Prática**: O projeto inclui um pipeline completo, desde a análise até o deploy, pronto para ser implementado em ambientes de produção no varejo.
- **Abordagem Data-Driven**: Análise baseada em dados e validação com métricas robustas garantem a precisão e a relevância das previsões para o contexto de negócios.

---

## 📚 **Referências**
- Hochreiter, S., & Schmidhuber, J. (1997). "Long Short-Term Memory". Neural Computation.
- Géron, A. (2019). "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow". O'Reilly Media.
- Nielsen, F. (2021). "Practical Time Series Analysis with Machine Learning". O'Reilly Media.

---


[IN](https://www.linkedin.com/in/guilherminog/)
