# 🚀 Supabase + Z-API Challenge

Uma automação simples, direta e poderosa: busca contatos no Supabase e dispara mensagens personalizadas no WhatsApp usando a Z-API.

Pensa nisso como um mini sistema de disparo inteligente, sem planilha, sem copy manual, sem dor de cabeça.

---

## ⚡ O que esse projeto faz (na prática)

- Puxa contatos direto de um banco no Supabase  
- Monta mensagens personalizadas tipo: “Olá, João tudo bem com você?”  
- Envia tudo automaticamente via WhatsApp (Z-API)  
- Registra o que deu certo e o que deu ruim no terminal  

---

## 🧠 Ideia por trás

Esse projeto simula um cenário real bem comum:

“Preciso automatizar comunicação com clientes sem virar escravo de planilha.”

Ele junta:

- Supabase (banco de dados na nuvem)
- Z-API (envio de mensagens no WhatsApp)
- Python (orquestração da automação)

---

## 🧱 Arquitetura do sistema

Fluxo da aplicação:

main.py  
↓  
supabase_service.py → busca contatos no banco  
↓  
zapi_service.py → envia mensagens via WhatsApp  
↓  
terminal → logs do resultado  

---

## 🛠️ Tecnologias usadas

- Python 3.11  
- Supabase (PostgreSQL na nuvem)  
- Z-API (WhatsApp API)  
- Requests  
- python-dotenv  

---

## 🚀 Setup do projeto

### 1. Clone o repositório

git clone https://github.com/LeonFagner/b2bflow-challenge.git  
cd b2bflow-challenge  

---

### 2. Instale as dependências

pip install -r requirements.txt  

---

### 3. Configure variáveis de ambiente

cp .env.example .env  

Preencha o arquivo `.env`:

SUPABASE_URL=your_supabase_url  
SUPABASE_KEY=your_supabase_key  
ZAPI_INSTANCE_ID=your_instance_id  
ZAPI_TOKEN=your_token  
ZAPI_CLIENT_TOKEN=your_client_token  

---

## 🗄️ Banco de dados (Supabase)

CREATE TABLE contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

---

## 🧪 Inserir dados de teste

INSERT INTO contacts (name, phone) VALUES
('João Silva',  '5511999990001'),
('Maria Souza', '5511999990002'),
('Carlos Lima', '5511999990003');

---

## ▶️ Executar o projeto

python main.py  

---

## 💬 Resultado esperado

Mensagem enviada para João Silva ✔  
Mensagem enviada para Maria Souza ✔  
Mensagem enviada para Carlos Lima ✔  

---

## 🎯 Objetivo do projeto

Demonstrar integração entre:

- banco de dados em nuvem  
- API externa de mensagens  
- automação com Python  

Tudo isso simulando um fluxo real de backend.


---

## 📌 Estrutura do projeto

b2bflow-challenge/  
├── main.py  
├── services/  
│   ├── __init__.py  
│   ├── supabase_service.py  
│   └── zapi_service.py  
├── .env.example  
├── .gitignore  
├── requirements.txt  
└── README.md  

---

## 🧠 Resumo

Esse projeto é um mini sistema de automação backend que integra:

- dados (Supabase)
- API externa (Z-API)
- lógica de envio
- automação com Python

Simples, mas com cara de produto real.
