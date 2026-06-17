import logging
import sys

from dotenv import load_dotenv

load_dotenv()

from services.supabase_service import fetch_contacts
from services.zapi_service import send_message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Iniciando envio de mensagens...")

    try:
        contacts = fetch_contacts(table="contacts", limit=3)
    except Exception as e:
        logger.critical("Não foi possível buscar contatos: %s", e)
        sys.exit(1)

    if not contacts:
        logger.warning("Nenhum contato encontrado. Encerrando.")
        return

    success_count = 0
    for contact in contacts:
        name = contact.get("name")
        phone = contact.get("phone")

        if not name or not phone:
            logger.warning("Contato ignorado por dados incompletos: %s", contact)
            continue

        sent = send_message(phone=phone, name=name)
        if sent:
            success_count += 1

    logger.info("Concluído. %d/%d mensagem(ns) enviada(s).", success_count, len(contacts))


if __name__ == "__main__":
    main()
