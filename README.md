# Tutorial de Testes de Mutação em Python

**Repositório:** Shopping-Mall-Cart-Python-Tests

---

## 1. Introdução

A qualidade do software depende não apenas da implementação correta das funcionalidades, mas também da efetividade dos testes que verificam seu comportamento.  
Os **testes de mutação** são uma técnica avançada para avaliação da qualidade das suítes de testes existentes.  

Diferentemente da cobertura tradicional, que apenas verifica quais linhas de código foram executadas, os testes de mutação introduzem defeitos deliberados (*mutantes*) para observar se os testes conseguem detectá-los.  

Neste tutorial, aplicamos a técnica de mutação ao repositório **Shopping-Mall-Cart-Python-Tests**, que simula um sistema de carrinho de compras em Python com casos de testes unitários já implementados.

---

## 2. Ferramentas e Tecnologias Utilizadas

- **Python 3.7+** – Linguagem de programação principal ([Python.org](https://www.python.org/))  
- **python3-venv** – Criação de ambientes virtuais ([Documentação](https://docs.python.org/3/library/venv.html))  
- **pytest** – Framework de testes unitários ([Documentação](https://docs.pytest.org/))  
- **pytest-cov** – Plugin para análise de cobertura ([PyPI](https://pypi.org/project/pytest-cov/))  
- **mutmut** – Ferramenta para testes de mutação em Python ([GitHub](https://github.com/boxed/mutmut))  
- **Kali Linux (VM)** – Ambiente utilizado para executar o `mutmut` no Windows.

---

## 3. Descrição do Projeto Utilizado

O projeto **Shopping-Mall-Cart-Python-Tests** implementa funcionalidades típicas de um carrinho de compras em Python:

- **checkOutRegister.py** – Gerenciamento de itens, cálculo de totais e registro de compras.  
- **product.py** – Representação de produtos com atributos de nome, preço e quantidade.  
- **Testes unitários** – Implementados com `unittest` ou `pytest`, cobrindo funções essenciais do sistema.

---

## 4. Link do Documento de Referência

O tutorial detalhado com todos os passos está disponível no seguinte link:  
[Documento do Google](https://docs.google.com/document/d/1oiFMQMmJRQm1-LBk7cSgNghLKkjr3LQawv2ySDpVcSU/edit?usp=sharing)

---
