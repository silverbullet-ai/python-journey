# test_weather.py

import unittest
from unittest.mock import patch, Mock
from weather import get_temperature


class TestWeather(unittest.TestCase):

    @patch("weather.requests.get")
    def test_get_temperature_returns_value(self, mock_get):
        # Arrange: fake API response
        mock_response = Mock()
        mock_response.json.return_value = {"temperature": 23.0}
        mock_get.return_value = mock_response

        # Act
        temp = get_temperature("Gaya")

        # Assert
        self.assertEqual(temp, 23.0)
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
