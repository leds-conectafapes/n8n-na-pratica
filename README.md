# Curso de n8n: Automação de Fluxos de Trabalho  
**Carga horária:** 12 horas  

## 🎯 Objetivo Geral

Capacitar os participantes a utilizar o n8n para criação, automação e gestão de fluxos de trabalho, aplicando os conceitos em projetos práticos como:

- Automação de tarefas repetitivas  
- Criação de chatbots inteligentes e contextualizados  
- Integrações com APIs e ferramentas externas  
- Geração e busca de embeddings com IA generativa  
- Sistemas de RAG (retrieval augmented generation)  

---

## 📋 Ementa do Curso

### Dia 1 – Introdução e Projetos Básicos com n8n
**Tópicos:**
- O que é o n8n e suas principais aplicações  
- Configuração do ambiente local com Docker  
- Criação de fluxos simples: Webhook, HTTP Request, Set, IF, Switch  
- **Projeto prático:** Chatbot automatizado com API Gemini  

### Dia 2 – Embeddings, RAG e OpenAI na prática
**Tópicos:**
- Comparativo entre OpenAI e Gemini para geração de embeddings  
- Introdução ao OpenAI Playground e criação de Assistentes  
- Construção de fluxos com busca vetorial (RAG) e resposta contextual  
- Subida e uso do OpenWebUI como interface alternativa para testes  
- **Projeto prático:** Chatbot com OpenAI, base vetorial e respostas inteligentes  

### Dias 3 e 4 – Prática Guiada e Livre
**Tópicos:**
- Exploração de projetos sugeridos ou autorais com n8n  
- Apoio para criação de fluxos com IA, automações e integrações reais  
- Testes com embeddings, OpenAI Assistants e chatbots com contexto  

---

## 🛠️ Pré-requisitos

- Conhecimentos básicos de lógica de programação  
- Familiaridade com conceitos de APIs REST  
- Computador com acesso à internet  
- Conta na OpenAI (Playground) e GitHub  

---

## 🔧 Ferramentas Utilizadas

- **n8n** (plataforma de automação visual)  
- **Docker Compose** (ambiente local com múltiplos serviços)  
- **PostgreSQL + pgvector** (armazenamento vetorial)  
- **OpenAI API** (assistentes, geração de embeddings, respostas)  
- **Gemini API** (respostas baseadas em LLM)  
- **OpenWebUI** (interface gráfica alternativa para playground local)  

---

## 📚 Estrutura do Repositório

```

n8n-na-pratica/
├── dia-1/
│   ├── slide
│   ├── exemplo
│   └── projeto-chatbot
├── dia-2/
│   ├── slide
│   └── projeto-validar-propostas
├── recursos/
│   ├── dados/               # pasta para leitura e escrita no n8n
│   ├── docker-compose       # arquivos de setup local
└── README.md

````

---

## 🚀 Como Começar

### Instalação Local (via Docker Compose)

```bash
# Clone o repositório
git clone https://github.com/leds-conectafapes/n8n-na-pratica
cd n8n-na-pratica/docker

# Suba o ambiente com n8n, PostgreSQL e OpenWebUI
docker compose up -d
````

A stack sobe automaticamente:

* `n8n` em `http://localhost:5678`
* `OpenWebUI` em `http://localhost:3000`
* `PostgreSQL` em `http://localhost:5432`, com extensão `pgvector` para armazenar embeddings

---

## 📖 Conceitos Fundamentais

### O que é o n8n?

O n8n é uma plataforma de automação de fluxos de trabalho baseada em nós (nodes), permitindo:

* Conectar serviços e APIs externas com facilidade
* Automatizar tarefas do dia a dia
* Criar lógicas complexas de forma visual
* Utilizar funções personalizadas com JavaScript
* Integrar com modelos de linguagem para criar fluxos inteligentes

---

## 🧠 Inteligência Artificial no Fluxo

### OpenAI Playground + Assistentes

* Criação de assistentes personalizados com contexto e arquivos
* Geração de embeddings com `text-embedding-3-*`
* Recuperação de informações via vetores (RAG)
* Integração direta via API com n8n

### OpenWebUI

* Interface gráfica para testes com LLMs (incluindo seus assistentes OpenAI)
* Visualização de histórico de conversas
* Rápida prototipagem e uso local sem precisar do Playground

---

## 🎯 Projetos Práticos

### Projeto 1 – Chatbot Automatizado com Gemini

* Recebe mensagens via Webhook
* Usa Gemini API para responder com base em prompt
* Primeira experiência com API de LLM

### Projeto 2 – RAG com Gemini

* Gera embeddings de documentos
* Armazena vetores no PostgreSQL (pgvector)
* Faz busca vetorial e usa OpenAI para gerar resposta contextual
* Exibe alternativa visual via OpenWebUI

---

## 🎥 Aulas Gravadas

Todas as aulas do curso estão disponíveis no links:
📺 [Clique Aqui!](https://youtube.com/playlist?list=PLo7sFyCeiGUes7oNdHc9BI-QZDepodAVs&si=z98Cj2mqpcpvA4E6)

---

## 📎 Referências Úteis

* n8n Docs: [https://docs.n8n.io](https://docs.n8n.io)
* OpenAI Playground: [https://platform.openai.com/playground](https://platform.openai.com/playground)
* OpenWebUI: [https://docs.openwebui.com/getting-started/](https://docs.openwebui.com/getting-started/)
* Variáveis de Ambiente OpenWebUI: [https://docs.openwebui.com/getting-started/env-configuration/](https://docs.openwebui.com/getting-started/env-configuration/)

---

## 📁 GitHub

Repositório do curso:
[https://github.com/leds-conectafapes/n8n-na-pratica](https://github.com/leds-conectafapes/n8n-na-pratica)
