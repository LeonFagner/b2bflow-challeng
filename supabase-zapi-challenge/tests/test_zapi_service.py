import unittest
from unittest.mock import MagicMock, patch

import requests

ENV = {
    "ZAPI_INSTANCE_ID": "instance123",
    "ZAPI_TOKEN": "token123",
    "ZAPI_CLIENT_TOKEN": "clienttoken123",
}


class TestBuildUrl(unittest.TestCase):

    @patch.dict("os.environ", ENV)
    def test_builds_correct_url(self):
        from services.zapi_service import _build_url
        url = _build_url()
        self.assertIn("instance123", url)
        self.assertIn("token123", url)

    @patch.dict("os.environ", {}, clear=True)
    def test_raises_when_env_missing(self):
        from services.zapi_service import _build_url
        with self.assertRaises(EnvironmentError):
            _build_url()


class TestBuildHeaders(unittest.TestCase):

    @patch.dict("os.environ", ENV)
    def test_returns_correct_headers(self):
        from services.zapi_service import _build_headers
        headers = _build_headers()
        self.assertEqual(headers["Client-Token"], "clienttoken123")
        self.assertEqual(headers["Content-Type"], "application/json")

    @patch.dict("os.environ", {}, clear=True)
    def test_raises_when_client_token_missing(self):
        from services.zapi_service import _build_headers
        with self.assertRaises(EnvironmentError):
            _build_headers()


class TestSendMessage(unittest.TestCase):

    @patch.dict("os.environ", ENV)
    @patch("services.zapi_service.requests.post")
    def test_returns_true_on_success(self, mock_post):
        from services.zapi_service import send_message
        mock_post.return_value = MagicMock(status_code=200)
        mock_post.return_value.raise_for_status = MagicMock()
        self.assertTrue(send_message(phone="5511999990001", name="Joao"))

    @patch.dict("os.environ", ENV)
    @patch("services.zapi_service.requests.post")
    def test_message_format(self, mock_post):
        from services.zapi_service import send_message
        mock_post.return_value = MagicMock(status_code=200)
        mock_post.return_value.raise_for_status = MagicMock()
        send_message(phone="5511999990001", name="Joao")
        _, kwargs = mock_post.call_args
        self.assertEqual(kwargs["json"]["message"], "Olá, Joao tudo bem com você?")
        self.assertEqual(kwargs["json"]["phone"], "5511999990001")

    @patch.dict("os.environ", ENV)
    @patch("services.zapi_service.requests.post")
    def test_returns_false_on_http_error(self, mock_post):
        from services.zapi_service import send_message
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("400 Client Error")
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response
        self.assertFalse(send_message(phone="5511999990001", name="Joao"))

    @patch.dict("os.environ", ENV)
    @patch("services.zapi_service.requests.post")
    def test_returns_false_on_network_error(self, mock_post):
        from services.zapi_service import send_message
        mock_post.side_effect = requests.exceptions.ConnectionError("timeout")
        self.assertFalse(send_message(phone="5511999990001", name="Joao"))

    @patch.dict("os.environ", {}, clear=True)
    def test_raises_on_missing_env(self):
        from services.zapi_service import send_message
        with self.assertRaises(EnvironmentError):
            send_message(phone="5511999990001", name="Joao")


if __name__ == "__main__":
    unittest.main()
