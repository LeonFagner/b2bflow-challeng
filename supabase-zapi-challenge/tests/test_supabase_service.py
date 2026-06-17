import unittest
from unittest.mock import MagicMock, patch


class TestGetClient(unittest.TestCase):

    @patch.dict("os.environ", {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test-key"})
    @patch("services.supabase_service.create_client")
    def test_returns_client_with_valid_env(self, mock_create):
        from services.supabase_service import get_client
        mock_create.return_value = MagicMock()
        get_client()
        mock_create.assert_called_once_with("https://test.supabase.co", "test-key")

    @patch.dict("os.environ", {}, clear=True)
    def test_raises_when_env_missing(self):
        from services.supabase_service import get_client
        with self.assertRaises(EnvironmentError):
            get_client()


class TestFetchContacts(unittest.TestCase):

    def _make_client(self, data):
        mock_response = MagicMock()
        mock_response.data = data
        mock_client = MagicMock()
        mock_client.table.return_value.select.return_value.limit.return_value.execute.return_value = mock_response
        return mock_client

    @patch.dict("os.environ", {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test-key"})
    @patch("services.supabase_service.get_client")
    def test_returns_contacts(self, mock_get_client):
        from services.supabase_service import fetch_contacts
        fake = [{"name": "Joao", "phone": "5511999990001"}, {"name": "Maria", "phone": "5511999990002"}]
        mock_get_client.return_value = self._make_client(fake)
        result = fetch_contacts()
        self.assertEqual(result, fake)

    @patch.dict("os.environ", {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test-key"})
    @patch("services.supabase_service.get_client")
    def test_returns_empty_list(self, mock_get_client):
        from services.supabase_service import fetch_contacts
        mock_get_client.return_value = self._make_client([])
        self.assertEqual(fetch_contacts(), [])

    @patch.dict("os.environ", {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test-key"})
    @patch("services.supabase_service.get_client")
    def test_respects_limit(self, mock_get_client):
        from services.supabase_service import fetch_contacts
        mock_client = self._make_client([])
        mock_get_client.return_value = mock_client
        fetch_contacts(limit=2)
        mock_client.table.return_value.select.return_value.limit.assert_called_once_with(2)

    @patch.dict("os.environ", {"SUPABASE_URL": "https://test.supabase.co", "SUPABASE_KEY": "test-key"})
    @patch("services.supabase_service.get_client")
    def test_raises_on_supabase_error(self, mock_get_client):
        from services.supabase_service import fetch_contacts
        mock_client = MagicMock()
        mock_client.table.return_value.select.return_value.limit.return_value.execute.side_effect = Exception("DB error")
        mock_get_client.return_value = mock_client
        with self.assertRaises(Exception):
            fetch_contacts()


if __name__ == "__main__":
    unittest.main()
