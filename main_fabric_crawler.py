"""Simple script to get all fabric server jar direct download links."""

import json
import requests


def fetch_data(url: str) -> list:
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        list: The JSON data as a list.
    """
    response = requests.get(url=url, timeout=120)
    response.raise_for_status()

    return response.json()


def filter_versions(game_versions: list, stable: bool) -> list:
    """
    Filters game versions based on their stability.

    Args:
        game_versions (list): List of game version data.
        stable (bool): True for stable versions, False for non-stable versions.

    Returns:
        list: List of filtered game version strings.
    """
    return [
        version["version"] for version in game_versions if version["stable"] == stable
    ]


def construct_download_urls(
    versions: list, loader_version: str, installer_version: str
) -> dict:
    """
    Constructs a dictionary of download URLs for given game versions.

    Args:
        versions (list): List of game version strings.
        loader_version (str): The loader version.
        installer_version (str): The installer version.

    Returns:
        dict: A dictionary with game versions as keys and download URLs as values.
    """
    download_url_template = (
        "https://meta.fabricmc.net/v2/versions/loader/{}/{}//{}/server/jar"
    )
    download_urls = {}

    for version in versions:
        download_url = download_url_template.format(
            version, loader_version, installer_version
        )
        download_urls[version] = download_url

    return download_urls


def save_to_json(data: dict, filename: str):
    """
    Saves given data to a JSON file.

    Args:
        data (dict): The data to write to the file.
        filename (str): The name of the output file.
    """
    with open(file=filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Download links saved to {filename}")


def main():
    """Main which executes everything."""
    game_versions = fetch_data("https://meta.fabricmc.net/v2/versions/game")
    loader_versions = fetch_data("https://meta.fabricmc.net/v2/versions/loader")
    installer_versions = fetch_data("https://meta.fabricmc.net/v2/versions/installer")

    latest_loader_version = loader_versions[0]["version"]
    latest_installer_version = installer_versions[0]["version"]

    stable_versions = filter_versions(game_versions, stable=True)
    non_stable_versions = filter_versions(game_versions, stable=False)

    stable_downloads = construct_download_urls(
        stable_versions, latest_loader_version, latest_installer_version
    )

    non_stable_downloads = construct_download_urls(
        non_stable_versions, latest_loader_version, latest_installer_version
    )

    save_to_json(stable_downloads, "release_fabric_downloads.json")
    save_to_json(non_stable_downloads, "snapshot_fabric_downloads.json")

    print("done")


if __name__ == "__main__":
    main()
