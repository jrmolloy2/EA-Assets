# Environment Agency Asset Checker

## Description
---

This project allows users to check whether an ID exists in the Environment Agency's Asset Management database (AIMS). This project uses Python 3.11 and the [Environment Agency's Asset Management API](https://environment.data.gov.uk/asset-management/doc/reference).

While working on flood risk mapping data for the Environment Agency, I needed to check whether a list of ID numbers existed in the AIMS database. As I was working externally to the Environment Agency, I did not have access to the database directly. There is a [mapping portal available](https://environment.data.gov.uk/asset-management/index.html), allowing users to search by asset ID. However, not all assets are returned through this portal (such as bridges). Additionally, AIMS data is available to download as vector datasets through the [Defra Data Services platform](https://environment.data.gov.uk/), but downloading sizeable data and searching through it using a GIS platform such as QGIS is time-consuming and requires frequent updates (the Defra Data Services platform is updated daily).

This project aims to solve this problem by using get requests to the Asset Management API and retrieving live data to verify asset IDs exist in AIMS.

<br>

## Installation
---

Clone this repository using the command:

`git clone git@github.com:jrmolloy2/EA-Assets.git`

<br>

## How to use
---

<br>

## Credits
---

[Environment Agency's Asset Management API](https://environment.data.gov.uk/asset-management/doc/reference)

---