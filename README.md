# Envio de mensagens via WhatsApp com Supabase e Z-API

Aplicação em Python que procura contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp usando a api Z-API.

## Setup da tabela no Supabase

Crie um projeto no Supabase e adicione uma tabela chamada `contatos`. Ela precisa ter as colunas `id` (int8), `created_at` (timestamptz), `nome` (text) e `telefone` (text).

Depois é só cadastrar de 1 a 3 contatos com nome e telefone. O telefone precisa estar no formato `5511999999999`, ou seja, sem espaços ou traços.

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:
```
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

## Como rodar

1. Instale as dependências:

```bash
pip install supabase python-dotenv requests
```

2. Preencha o arquivo `.env` com suas credenciais

3. Execute:

```bash
python main.py
```
