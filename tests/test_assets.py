import unittest
from unittest import mock
from asset_checker.assets import CallAsset, AssetData
from asset_checker.errors import InvalidAPICallError


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

    @mock.patch("asset_checker.assets.requests.get")
    def test_get_asset_information_invalid_status_code(self, mock_get):
        mock_get.return_value.status_code = 404

        asset_call = CallAsset(263188)
        with self.assertRaises(InvalidAPICallError):
            asset_call.get_asset_information()


class TestAssetData(unittest.TestCase):

    def test_init_valid(self):
        asset_data = AssetData("test")
        self.assertEqual("test", asset_data.data)

    def test_set_asset_type_valid(self):
        mock_json = [
            {
                "id": "mock_url",
                "type": "mock_url",
                "label": "mock_asset:id",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-0.1952, 53.08209]
                },
                "asset-type": {
                    "id": "mock_url",
                    "label": "Structure"
                },
                "asset-sub-type": {
                    "id": "mock_url",
                    "label": "Outfall"
                }
            }
        ]
        asset_data = AssetData(mock_json)
        asset_data.set_asset_type()
        self.assertEqual("Structure: Outfall", asset_data.get_asset_type())

    def test_get_asset_type_invalid_no_data(self):
        mock_json = []
        asset_data = AssetData(mock_json)
        with self.assertRaises(IndexError):
            asset_data.set_asset_type()

    def test_get_asset_type_invalid_unexpected_structure(self):
        mock_json = [
            {
                "id": "mock_url"
            }
        ]
        asset_data = AssetData(mock_json)
        with self.assertRaises(KeyError):
            asset_data.set_asset_type()

    def test_set_geometry_type_valid(self):
        mock_json = [
            {
                "id": "mock_url",
                "type": "mock_url",
                "label": "mock_asset:id",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-0.1952, 53.08209]
                },
                "asset-type": {
                    "id": "mock_url",
                    "label": "Structure"
                },
                "asset-sub-type": {
                    "id": "mock_url",
                    "label": "Outfall"
                }
            }
        ]
        asset_data = AssetData(mock_json)
        asset_data.set_geometry_type()
        
        self.assertEqual("Point", asset_data.get_geometry_type())

    def test_set_geometry_type_invalid_no_data(self):
        mock_json = []
        asset_data = AssetData(mock_json)

        with self.assertRaises(IndexError):
            asset_data.set_geometry_type()

    def test_set_geometry_type_invalid_unexpected_structure(self):
        mock_json = [
            {"id": "mock_url"}
        ]
        asset_data = AssetData(mock_json)

        with self.assertRaises(KeyError):
            asset_data.set_geometry_type()


if __name__ == "__main__":
    unittest.main()
