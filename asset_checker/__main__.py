"""Program to check whether asset IDs exist in the Environment Agency's Asset Management database."""


from asset_checker.assets import CallAsset, AssetData
from asset_checker.errors import InvalidAPICallError


def main():
    """Command-line program to check asset IDs exist in the Asset Management database."""

    print("Welcome to the Asset Checker.")

    check_asset = True
    while check_asset:

        asset_id = input("Enter the asset ID: ")
        try:
            asset_id = int(asset_id)
        except ValueError:
            print("Please enter a number.")
            continue

        asset_call = CallAsset(asset_id)
        try:
            data = asset_call.get_asset_information()
        except InvalidAPICallError as exc:
            print(exc)
            continue

        asset_data = AssetData(data)
        try:
            asset_data.set_asset_type()
            asset_data.set_geometry_type()
        except KeyError as exc:
            print(exc)
        except IndexError as exc:
            print(exc)
        else:
            print("Asset type: {}".format(asset_data.get_asset_type()))
            print("Asset geometry type: {}".format(asset_data.get_geometry_type()))

        user_decision = input("Do you want to check another asset ID? (Y/N) ")
        if user_decision.lower() == "n":
            check_asset = False

    print("Thank you for using the Asset Checker.")
    

if __name__ == "__main__":
    main()
