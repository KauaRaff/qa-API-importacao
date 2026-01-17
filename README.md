#  Test Calc Importação

Projeto de Quality em Python focado em **testes automatizados**, simulando o cálculo de custos de importação com base em:
- valor do produto
- frete
- taxa de câmbio
- imposto de importação
- ICMS

O objetivo é demonstrar boas práticas de **QA**, **pytest**, **mock de API**, **logs** e **CI/CD com GitHub Actions**.

---

##  Tecnologias Utilizadas

- **Python 3.13**
- **Pytest**
- **Requests**
- **unittest.mock**
- **Logging**
- **GitHub Actions (CI)**

---

##  Estrutura do Projeto
```
test-calc-importacao/
│
├── api_importacao/
│ ├── init.py
│ ├── cambio.py
│ └── calculo.py
│
├── tests/
│ ├── test_api.py
│ ├── test_calculo.py
│ ├── test_cambio.py
│ └── test_moeda_invalida.py
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── requirements.txt
└── README.md
```

---

##  Funcionalidades Testadas

###  Cálculo de Importação
- Conversão de moeda
- Aplicação de imposto de importação (60% quando aplicável)
- Cálculo correto de ICMS (18%)
- Retorno detalhado do cálculo (base, impostos e total)

###  API de Câmbio
- Moeda válida
- Moeda inválida
- API indisponível (mock)

---

##  Execução dos Testes

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute os testes:
   ```
   pytest -v
    ```
3. Para visualizar com os Logs:
   ```
   pytest -v --log-cli-level=INFO
   ```
   
---

## CI/CD com o Actions
- Roda automaticamente a cada push ou pull request

- Instala dependências

- Executa todos os testes automatizados

---

## Autor
- Kauã Raffaello - QA Jr.

