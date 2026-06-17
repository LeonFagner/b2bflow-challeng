import logging
import os

from supabase import create_client, Client

logger = logging.getLogger(__name__)


def get_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise EnvironmentError("SUPABASE_URL e SUPABASE_KEY devem estar definidos no .env")

    return create_client(url, key)


def fetch_contacts(table: str = "contacts", limit: int = 3) -> list[dict]:
    logger.info("Buscando até %d contatos na tabela '%s'...", limit, table)

    try:
        client = get_client()
        response = client.table(table).select("*").limit(limit).execute()
        contacts = response.data

        logger.info("%d contato(s) encontrado(s).", len(contacts))
        return contacts

    except EnvironmentError:
        raise
    except Exception as e:
        logger.error("Erro ao buscar contatos no Supabase: %s", e)
        raise
