import logging
import os

import requests

logger = logging.getLogger(__name__)

ZAPI_BASE_URL = "https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"


def _build_url() -> str:
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")

    if not instance_id or not token:
        raise EnvironmentError("ZAPI_INSTANCE_ID e ZAPI_TOKEN devem estar definidos no .env")

    return ZAPI_BASE_URL.format(instance_id=instance_id, token=token)


def _build_headers() -> dict[str, str]:
    client_token = os.getenv("ZAPI_CLIENT_TOKEN")

    if not client_token:
        raise EnvironmentError("ZAPI_CLIENT_TOKEN deve estar definido no .env")

    return {
        "Content-Type": "application/json",
        "Client-Token": client_token,
    }


def send_message(phone: str, name: str) -> bool:
    message = f"Olá, {name} tudo bem com você?"
    logger.info("Enviando mensagem para %s (%s)...", name, phone)

    response = None
    try:
        url = _build_url()
        headers = _build_headers()
        payload = {"phone": phone, "message": message}

        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()

        logger.info("Mensagem enviada com sucesso para %s.", name)
        return True

    except requests.exceptions.HTTPError as e:
        body = response.text if response is not None else ""
        logger.error("Erro HTTP ao enviar para %s: %s - %s", name, e, body)
        return False
    except requests.exceptions.RequestException as e:
        logger.error("Erro de rede ao enviar para %s: %s", name, e)
        return False
    except EnvironmentError:
        raise
