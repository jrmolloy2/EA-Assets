import requests
from asset_checker.errors import InvalidAPICallError


ROOT = "http://environment.data.gov.uk/asset-management"
SINGLE_ASSET = ROOT + "/id/asset/{}.json"


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
