import requests
from asset_checker.errors import InvalidAPICallError


ROOT = "http://environment.data.gov.uk/asset-management"
SINGLE_ASSET = ROOT + "/mapping-api/Asset?assets=http://environment.data.gov.uk/asset-management/id/asset/{}"


class CallAsset:

    def __init__(self, asset_id):
        self.asset_id = asset_id

    def get_asset_information(self):
        url = SINGLE_ASSET.format(self.asset_id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise InvalidAPICallError(response.status_code)


class AssetData:

    def __init__(self, data):
        self.data = data
        self._asset_type = None
        self._asset_subtype = None
        self._geom_type = None

    def set_asset_type(self):
        if self.data:
            try:
                self._asset_type = self.data[0]["asset-type"]["label"]
                self._asset_subtype = self.data[0]["asset-sub-type"]["label"]
            except KeyError:
                raise KeyError("Unexpected format of JSON response from the API.")
        else:
            raise IndexError("No asset data returned from the API.")

    def get_asset_type(self):
        return self._asset_type + ": " + self._asset_subtype

    def set_geometry_type(self):
        if self.data:
            try:
                self._geom_type = self.data[0]["geometry"]["type"]
            except KeyError:
                raise KeyError("Unexpected format of JSON response from the API.")
        else:
            raise IndexError("No asset data returned from the API.")

    def get_geometry_type(self):
        return self._geom_type
