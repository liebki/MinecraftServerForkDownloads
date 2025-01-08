"""
This script simply uses the API of mojang to get all versions available,
check if they have server files or not and then creates two files which are
in the repository which contain all direct download links for all versions.
"""

import requests
import json

MOJANG_MANIFEST_URL = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"


def fetch_json(url: str):
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: Parsed JSON data from the response.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to fetch data from {url}")
        exit()
    return response.json()


def save_to_json(data, filename: str):
    """
    Saves given data to a JSON file.

    Args:
        data (_type_): The data to write to the file.
        filename (str): The name of the output file.
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Download links saved to {filename}")


def filter_versions(versions):
    """
    Filters release and snapshot versions from the version manifest data.

    Args:
        versions (list): List of version metadata from the manifest.

    Returns:
        tuple: Two dictionaries:
               - A dictionary of release versions and their asset URLs.
               - A dictionary of snapshot versions and their asset URLs.
    """
    print("Filtering versions into releases and snapshots:")
    release_versions = {
        version.get("id", "Unknown version"): version.get("url", "error")
        for version in versions
        if "release" in version.get("type", "error")
    }

    snapshot_versions = {
        version.get("id", "Unknown version"): version.get("url", "error")
        for version in versions
        if "snapshot" in version.get("type", "error")
    }

    return release_versions, snapshot_versions


def get_server_urls(vanilla_asset_urls):
    """
    Fetches server URLs from the asset URLs.

    Args:
        vanilla_asset_urls (dict): A dictionary of version IDs and their asset URLs.

    Returns:
        tuple: Two dictionaries:
               - Versions with server URLs.
               - Versions without server URLs.
    """
    print("Querying all asset URLs to get possible server direct download URLs:")
    versions_with_server = {}
    versions_without_server = {}

    for version, url in vanilla_asset_urls.items():
        data_asset = fetch_json(url)
        try:
            server_url = data_asset["downloads"]["server"]["url"]
            print(f"There is a server.jar available for version {version}")
            versions_with_server[version] = server_url
        except KeyError:
            print(f"There is no server.jar available for version {version}")
            versions_without_server[version] = url

    return versions_with_server, versions_without_server


def main():
    """
    Main function to gather version data, filter releases, and save server URLs.
    """
    print("Trying to gather all versions available in manifestv2 file:")
    manifest_data = fetch_json(MOJANG_MANIFEST_URL)

    all_versions = manifest_data.get("versions", [])
    releases_asset_urls, snapshots_asset_urls = filter_versions(all_versions)

    release_versions_with_server, release_versions_without_server = get_server_urls(
        releases_asset_urls
    )
    snapshot_versions_with_server, snapshot_versions_without_server = get_server_urls(
        snapshots_asset_urls
    )

    final_data_release = {
        "server_available": release_versions_with_server,
        "server_unavailable": release_versions_without_server,
    }

    final_data_snapshot = {
        "server_available": snapshot_versions_with_server,
        "server_unavailable": snapshot_versions_without_server,
    }

    save_to_json(final_data_release, "release_vanilla_downloads.json")
    save_to_json(final_data_snapshot, "snapshot_vanilla_downloads.json")

    print("Done, saved release and snapshot urls to their respective files.")


if __name__ == "__main__":
    main()
