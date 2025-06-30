# Curso de n8n: Automação de Fluxos de Trabalho

## 🎯 Objetivo Geral

Capacitar os participantes a utilizar o n8n para criação, automação e gestão de fluxos de trabalho, aplicando os conceitos em projetos práticos como:

- Automação de tarefas 
- Chatbots contextualizados
- Integrações com APIs e ferramentas externas

## 📋 Ementa do Curso

### Dia 1 - Introdução e Projetos Básicos com n8n
**Carga horária:** 3 horas

**Tópicos:**
- Introdução ao n8n e conceitos fundamentais
- Configuração do ambiente de trabalho
- Construção de fluxos básicos
- **Projeto prático:** Chatbot automatizado com Gemini

## 🛠️ Pré-requisitos

- Conhecimentos básicos de lógica de programação
- Familiaridade com conceitos de APIs
- Computador com acesso à internet
- Conta no GitHub (para versionamento de projetos)

## 🔧 Ferramentas Utilizadas

- **n8n** (plataforma principal)
- **Docker** (para ambiente local)
- **Gemini API** (para funcionalidades de IA)

## 📚 Estrutura do Repositório

```
n8n-na-pratica/
├── dia-1/
│   ├── slide
│   ├── exemplo
│   └── projeto-chatbot
├── dia-2/
│   ├── slide
│   ├── ...
├── recursos/
│   ├── templates/
│   ├── credenciais-exemplo/
│   └── troubleshooting.md
└── README.md
```

## 🚀 Como Começar

### Instalação Local (Docker)
```bash
# Clone o repositório
git clone https://github.com/leds-conectafapes/n8n-na-pratica
cd n8n-na-pratica/docker-compose-yml

# Execute o n8n com Docker
docker compose up
```

## 📖 Conceitos Fundamentais

### O que é o n8n?
O n8n é uma plataforma de automação de fluxos de trabalho baseada em nós (nodes) que permite:
- Conectar diferentes serviços e APIs
- Automatizar tarefas repetitivas
- Criar fluxos de trabalho visuais
- Integrar sistemas diversos sem código complexo

### Principais Vantagens
- **Open-source:** Código aberto e gratuito
- **Visual:** Interface drag-and-drop intuitiva
- **Extensível:** Mais de 400+ integrações nativas
- **Flexível:** Suporte a código personalizado
- **Self-hosted:** Controle total sobre seus dados

## 🎯 Projetos Práticos

### Projeto 1: Chatbot Inteligente com IA

* Integração com **modelo de linguagem (Gemini)** para respostas contextuais
* Leitura e interpretação de **embeddings gerados a partir de documentos**
* O chatbot responde com base no conteúdo de **arquivos PDF, ou textos vetorizados previamente**
