# Supabase + Z-API Challenge

Aplicação Python que busca contatos no Supabase e envia mensagens via Z-API.

## Pré-requisitos

- Python 3.11+
- Conta no [Supabase](https://supabase.com)
- Instância ativa na [Z-API](https://z-api.io)

## Configuração

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <repo-url>
   cd supabase-zapi-challenge
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Copie o arquivo de exemplo e preencha com suas credenciais:
   ```bash
   cp .env.example .env
   ```

## Variáveis de ambiente

| Variável           | Descrição                              |
|--------------------|----------------------------------------|
| `SUPABASE_URL`     | URL do projeto no Supabase             |
| `SUPABASE_KEY`     | Chave anon/public do Supabase          |
| `ZAPI_INSTANCE_ID` | ID da instância na Z-API               |
| `ZAPI_TOKEN`       | Token da instância na Z-API            |
| `ZAPI_CLIENT_TOKEN`| Client-Token de segurança da Z-API     |

## Estrutura da tabela `contacts`

Crie a tabela no Supabase com ao menos as colunas:

| Coluna  | Tipo   | Descrição                         |
|---------|--------|-----------------------------------|
| `name`  | text   | Nome do contato                   |
| `phone` | text   | Telefone no formato E.164 (`5511999999999`) |

## Execução

```bash
python main.py
```

## Estrutura do projeto

```
supabase-zapi-challenge/
├── main.py                  # Orquestrador principal
├── services/
│   ├── supabase_service.py  # Busca de contatos
│   └── zapi_service.py      # Envio de mensagens
├── .env.example             # Modelo de variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```
