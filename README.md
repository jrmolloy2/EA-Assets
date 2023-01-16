# Environment Agency Asset Checker

## Description
---

This project allows users to check whether an ID exists in the Environment Agency's Asset Management database (AIMS). This project uses Python 3.11 and the [Environment Agency's Asset Management API](https://environment.data.gov.uk/asset-management/doc/reference).

While working on flood risk mapping data for the Environment Agency, I needed to check whether a list of ID numbers existed in the AIMS database. As I was working externally to the Environment Agency, I did not have access to the database directly. There is a [mapping portal available](https://environment.data.gov.uk/asset-management/index.html), allowing users to search by asset ID. However, not all assets are returned through this portal (such as bridges). Additionally, AIMS data is available to download as vector datasets through the [Defra Data Services platform](https://environment.data.gov.uk/), but downloading sizeable data and searching through it using a GIS platform such as QGIS is time-consuming and requires frequent updates (the Defra Data Services platform is updated daily).

This project aims to solve this problem by using get requests to the Asset Management API and retrieving live data to verify asset IDs exist in AIMS.

<br>

## Installation

Clone this repository using the command:

```console
git clone git@github.com:jrmolloy2/EA-Assets.git
```

Install the requirements using the command below from the EA-Assets folder.

```console
pip install -r requirements.txt
```

Run the package using the command below from the EA-Assets folder:

```console
python -m asset_checker
```

<br>

## How to use

This program is a command-line interface. On running, the program will prompt you to enter an asset ID.

```console
Welcome to the Asset Checker.
Enter the asset ID:
```

The asset ID entered should be a number, otherwise you will see an error and be prompted to enter the asset ID again.

```console
Please enter a number.
Enter the asset ID: 
```

Once you have entered a number, the program will call the Environment Agency's Asset Management API and return the asset type and geometry type.

```console
Asset type: Structure: Outfall
Asset geometry type: Point
```

If the number entered by the user is not in the Asset Management database, an error will be printed.

```console
Enter the asset ID: 999999999999
No asset data returned from the API.
```

The program continues on a loop, asking the user whether they want to check another asset.

```console
Do you want to check another asset ID? (Y/N)
```

If the user enters N (either upper- or lower-case), the program will end.

```console
Do you want to check another asset ID? (Y/N) n
Thank you for using the Asset Checker.
```

<br>

## Tests

Unittests are available in the tests folder. These can be run using the command below from the EA-Assets folder.

```console
python -m unittest discover -v
```

<br>

## Credits

[Environment Agency's Asset Management API](https://environment.data.gov.uk/asset-management/doc/reference)

---