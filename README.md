# LSTM-API

## Descrição
Este projeto foi desenvolvido para implementar um modelo de previsão de vendas utilizando uma LSTM (Long Short-Term Memory). O projeto utiliza **FastAPI** para expor o modelo através de uma API, e ferramentas como **Docker**, **Prometheus** e **Grafana** para monitoramento e integração com outros sistemas. Além disso, conta com notebooks de desenvolvimento do modelo e pipelines para produção.

### Subtítulo:
**Análise Comparativa de Modelos de Séries Temporais e Redes Neurais**

## Estrutura do Projeto

```bash
LSTM-API/
│
├── app/
│   ├── main.py              # FastAPI app que expõe o endpoint para previsão
│   ├── model.py             # Código do modelo LSTM carregado
│   ├── prometheus_metrics.py # Middleware para monitoramento Prometheus
│   ├── requirements.txt     # Bibliotecas necessárias
│   └── monitor/
│       ├── prometheus.yml   # Configuração do Prometheus
│       └── grafana/         # Configurações para o Grafana
│
├── data/
│   └── Walmart.csv          # Dataset ou fonte de dados
└── docker-compose.yml       # Arquivo Docker Compose para orquestração de múltiplos serviços
```

### Funcionalidades

- **FastAPI**: Prove um endpoint para gerar previsões de vendas em tempo real.
- **Modelo LSTM**: Carregamento do modelo treinado a partir de um arquivo `.h5` para prever dados de vendas.
- **Prometheus**: Monitora métricas de desempenho da API.
- **Grafana**: Visualiza e analisa métricas de monitoramento.
- **Docker**: Empacotamento da aplicação em containers para fácil deploy.

## Setup e Execução

### Pré-requisitos

- **Docker** e **Docker Compose** instalados na máquina.
- Conta no **GitHub** para versionamento e backup do projeto.
- O modelo LSTM treinado deve ser salvo em `models/lstm_model.h5`.

### Passos para rodar a API:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/LSTM-API.git
   cd LSTM-API
   ```

2. **Construa e execute os containers com Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Acesse a API**: Acesse o FastAPI através do [http://localhost:8000/docs](http://localhost:8000/docs).

4. **Acesse o Prometheus**: Acesse as métricas de monitoramento no [http://localhost:9090](http://localhost:9090).

5. **Acesse o Grafana**: Visualize os gráficos e relatórios no [http://localhost:3000](http://localhost:3000).

### Endpoints Disponíveis

- **/predict** (POST): Recebe uma lista de features e retorna uma previsão de vendas com base no modelo LSTM.
  - Exemplo de Payload:
    ```json
    {
      "features": [1.0, 2.0, 3.0, 4.0]
    }
    ```

- **/metrics** (GET): Retorna métricas de desempenho para monitoramento com Prometheus.

## Monitoramento

O sistema de monitoramento é configurado usando **Prometheus** e **Grafana**.

- **Prometheus**: Coleta métricas do uso da API e do modelo.
- **Grafana**: Permite a visualização das métricas coletadas em dashboards personalizáveis.

## Notebooks

Os notebooks estão na pasta `notebook/` e contêm os seguintes arquivos:
- **Walmart_sales_forecasting_notebook_rev001.ipynb**: Primeira versão do modelo.
- **Walmart_sales_forecasting_notebook_rev005.ipynb**: Versão intermediária com ajuste de hiperparâmetros.
- **Walmart_sales_forecasting_notebook_rev006.ipynb**: Versão final com integração do modelo otimizado.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** e enviar **pull requests**.

## Licença

Este projeto está sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Este é o README formatado em Markdown. Ele fornece uma descrição detalhada do seu projeto, incluindo estrutura de diretórios, funcionalidades, instruções de setup e execução, monitoramento, além de uma seção de notebooks e contribuições.