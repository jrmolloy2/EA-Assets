import unittest
from unittest import mock
from asset_checker.assets import CallAsset


class TestCallAsset(unittest.TestCase):

    def test_init_valid(self):
        asset_call = CallAsset(263188)
        self.assertEqual(263188, asset_call.asset_id)

    @mock.patch("asset_checker.assets.requests.get")
    def test_get_asset_information_valid(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = "test"

        asset_call = CallAsset(263188)
        result = asset_call.get_asset_information()
        self.assertEqual("test", result)


if __name__ == "__main__":
    unittest.main()
