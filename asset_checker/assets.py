"""Module to handle get requests and data parsing from the Environment Agency's Asset Management API."""


import requests
from errors import InvalidAPICallError


ROOT = "http://environment.data.gov.uk/asset-management"
SINGLE_ASSET = ROOT + "/mapping-api/Asset?assets=http://environment.data.gov.uk/asset-management/id/asset/{}"


class CallAsset:
    """Handles get requests to retrieve data for an asset.
    
    Parameters
    ----------
    asset_id : int
        ID of an asset to check.

    Attributes
    ----------
    asset_id : int
        ID of an asset to check.

    Examples
    --------
    >>> asset_call = CallAsset(263188)    
    """

    def __init__(self, asset_id):
        self.asset_id = asset_id

    def get_asset_information(self):
        """Make a get request to retrieve data for a single asset.
        
        Returns
        -------
        list
            A JSON-like object containing the asset information.
        
        Raises
        ------
        InvalidAPICallError
            If the status code of the response is not OK (200).        
        
        Examples
        --------
        
        Example response is abbreviated for legibility.
        
        >>> asset_data = CallAsset(263188)
        >>> asset_data.get_asset_information()
        [{"id": "url", "geometry": {"type": Point"}, "asset-type": {"label": "Structure"}}]
        """

        url = SINGLE_ASSET.format(self.asset_id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise InvalidAPICallError(response.status_code)


class AssetData:
    """Parses asset information retrieved from the API.
    
    Parameters
    ----------
    data : list
        A JSON-like object containing the data retrieved from the API.

    Attributes
    ----------
    data : list
        A JSON-like object containing the data retrieved from the API.
    
    Examples
    --------

    Example data argument abbreviated for legibility.

    >>> asset = AssetData([{"id": "url", "geometry": {"type": "Point"}}])
    """

    def __init__(self, data):
        self.data = data
        self._asset_type = None
        self._asset_subtype = None
        self._geom_type = None

    def set_asset_type(self):
        """Extracts the asset type and sets the asset_type attribute.
        
        Raises
        ------
        KeyError
            If the self.data attribute does not contain the expected keys.
        IndexError
            If the self.data attribute is an empty list.
        """

        if self.data:
            try:
                self._asset_type = self.data[0]["asset-type"]["label"]
                self._asset_subtype = self.data[0]["asset-sub-type"]["label"]
            except KeyError:
                raise KeyError("Unexpected format of JSON response from the API.")
        else:
            raise IndexError("No asset data returned from the API.")

    def get_asset_type(self):
        """Returns a string representation of the asset type and subtype."""

        return self._asset_type + ": " + self._asset_subtype

    def set_geometry_type(self):
        """Extracts the geometry and sets the geom_type attribute.
        
        Raises
        ------
        KeyError
            If the self.data attribute does not contain the expected keys.
        IndexError
            If the self.data attribute is an empty list.
        """

        if self.data:
            try:
                self._geom_type = self.data[0]["geometry"]["type"]
            except KeyError:
                raise KeyError("Unexpected format of JSON response from the API.")
        else:
            raise IndexError("No asset data returned from the API.")

    def get_geometry_type(self):
        """Returns a string representation of the geometry type."""

        return self._geom_type
