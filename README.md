# Supabase + Z-API Challenge

Aplicação Python que busca contatos no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.

## Pré-requisitos

- Python 3.11+
- Conta no [Supabase](https://supabase.com)
- Instância ativa na [Z-API](https://z-api.io)

## Setup

**1. Clone o repositório:**
```bash
git clone https://github.com/LeonFagner/b2bflow-challenge.git
cd b2bflow-challenge
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente:**
```bash
cp .env.example .env
```
Abra o `.env` e preencha com suas credenciais (veja a seção abaixo).

**4. Crie a tabela no Supabase:**

Acesse seu projeto no Supabase → **SQL Editor** e execute:

```sql
CREATE TABLE contacts (
    id   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
```

**5. Insira os contatos de teste:**

Ainda no SQL Editor, execute:

```sql
INSERT INTO contacts (name, phone) VALUES
    ('João Silva',  '5511999990001'),
    ('Maria Souza', '5511999990002'),
    ('Carlos Lima', '5511999990003');
```

> O campo `phone` deve estar no formato E.164 sem o `+`: `5511999999999`  
> (55 = Brasil, 11 = DDD, 9 dígitos do número)

**6. Rode o projeto:**
```bash
python main.py
```

## Variáveis de ambiente

Copie `.env.example` para `.env` e preencha:

| Variável | Onde encontrar |
|---|---|
| `SUPABASE_URL` | Supabase → Project Settings → API → Project URL |
| `SUPABASE_KEY` | Supabase → Project Settings → API → anon key (legacy/JWT) |
| `ZAPI_INSTANCE_ID` | Painel Z-API → sua instância → ID da instância |
| `ZAPI_TOKEN` | Painel Z-API → sua instância → Token |
| `ZAPI_CLIENT_TOKEN` | Painel Z-API → sua instância → Client Token |

> **Atenção:** Use a chave `anon` **legada** do Supabase (começa com `eyJ...`), não a nova chave `sb_publishable_`.

## O que o projeto faz

1. Carrega as credenciais do `.env`
2. Conecta no Supabase e busca até 3 contatos da tabela `contacts`
3. Para cada contato, monta a mensagem: `Olá, <nome> tudo bem com você?`
4. Envia a mensagem via Z-API (WhatsApp)
5. Loga o resultado de cada envio no terminal

## Estrutura do projeto

```
b2bflow-challenge/
├── main.py                  # Orquestrador principal
├── services/
│   ├── __init__.py
│   ├── supabase_service.py  # Busca de contatos no Supabase
│   └── zapi_service.py      # Envio de mensagens via Z-API
├── .env.example             # Modelo de variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```
