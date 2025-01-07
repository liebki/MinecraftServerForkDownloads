"""
This script simply uses the API of papermc to get all versions of paper-server,
get the highest build number, use this to construct the direct download link and
to create a simple json which contains all versions with their download link.
"""

import requests
import json

# Could possibly also be changed to travertine, waterfall, velocity or folia to download those
BASE_PROJECT_TYPE = "paper"
BASE_URL = f"https://api.papermc.io/v2/projects/{BASE_PROJECT_TYPE}/"


def fetch_versions() -> dict:
    """Method to get all available versions

    Raises:
        Exception: Error if versions can't be fetched

    Returns:
        str: The json string
    """
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch versions: {response.status_code}")


def fetch_builds(version) -> str:
    """Method to get build informations of specific version

    Raises:
        Exception: Error if informations can't be fetched

    Returns:
        str: The json string
    """
    response = requests.get(f"{BASE_URL}versions/{version}/builds/")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Failed to fetch builds for version {version}: {response.status_code}"
        )


# Generate download links for the latest (highest) build of each version
def generate_download_links() -> dict:
    """This method simply creates the json to write to the output file

    Returns:
        dict: All versions with one direct download link
    """
    versions_data = fetch_versions()
    versions = versions_data["versions"]
    download_links = {}

    for version in versions:
        print(f"Version: {version}")
        builds_data = fetch_builds(version)

        builds = builds_data.get("builds", [])
        if isinstance(builds, list) and builds:

            latest_build = max(builds, key=lambda b: b["build"])

            build_number = latest_build["build"]
            file_name = latest_build["downloads"]["application"]["name"]

            download_url = f"{BASE_URL}versions/{version}/builds/{build_number}/downloads/{file_name}"
            download_links[version] = download_url
        else:
            print(f"No builds found for version {version} or 'builds' is not a list.")

    return download_links


def save_to_json(data, filename: str):
    """Method to generate a output json file which contains all versions and links

    Args:
        data (_type_): The data to write to the file
        filename (str): What file name to use
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Download links saved to {filename}")


if __name__ == "__main__":
    try:
        download_links = generate_download_links()
        save_to_json(data=download_links, filename="paper_downloads.json")

    except Exception as e:
        print(f"An error occurred: {e}")
