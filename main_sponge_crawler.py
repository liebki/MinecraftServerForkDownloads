"""Simple script to get all forge server jar direct download links using selenium."""

# pylint: disable=C0301

import json
import requests

BASE_SPONGE_URL = "https://dl-api.spongepowered.org/v2/groups/org.spongepowered/artifacts/spongevanilla"
VERSIONS_SPONGE_URL_TEMP = "https://dl-api.spongepowered.org/v2/groups/org.spongepowered/artifacts/spongevanilla/versions?limit=1&tags=minecraft:{mc_version}"


def save_to_json(data, filename: str):
    """
    Saves given data to a JSON file.

    Args:
        data (_type_): The data to write to the file.
        filename (str): The name of the output file.
    """
    with open(file=filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Download links saved to {filename}")


def get_json(url: str):
    """Function to get the JSON content from a URL

    Args:
        url (str): URL to query

    Returns:
        _type_: _description_
    """
    response = requests.get(url=url, timeout=120)
    if response.status_code == 200:
        return response.json()

    print(f"Error fetching URL: {url}")
    return None


def filter_versions(minecraft_versions: list[str]) -> list[str]:
    """Method to filter out all base versions

    Args:
        minecraft_versions (list[str]): A list of minecraft versions

    Returns:
        list[str]: A list of minecraft versions but filtered of base versions
    """
    return [version for version in minecraft_versions if version.count(".") > 1]


def construct_download_url(artifact: str, mc_version: str) -> str:
    """Method to build the correct direct download url

    Args:
        artifact (str): The artifact string
        mc_version (str): The respective minecraft version

    Returns:
        str: Download url to directly download sponge file
    """
    if mc_version in ["1.8", "1.8.9", "1.9", "1.9.4", "1.10.2", "1.11", "1.11.2"]:
        return f"https://repo.spongepowered.org/repository/legacy-transfer/org/spongepowered/spongevanilla/{artifact}/spongevanilla-{artifact}.jar"

    return f"https://repo.spongepowered.org/repository/maven-releases/org/spongepowered/spongevanilla/{artifact}/spongevanilla-{artifact}-universal.jar"


def process_minecraft_versions():
    """Method to process the versions and generate the links"""
    sponge_downloads = {}
    initial_data = get_json(BASE_SPONGE_URL)

    if not initial_data or "tags" not in initial_data:
        print("Error: No 'minecraft' list found in the initial data.")
        return {}

    minecraft_versions = initial_data["tags"]["minecraft"]
    minecraft_versions = filter_versions(minecraft_versions)

    for mc_version in minecraft_versions:
        print(f"Processing mc version: {mc_version}:")
        versions_url = VERSIONS_SPONGE_URL_TEMP.format(mc_version=mc_version)
        version_data = get_json(versions_url)

        if version_data and "artifacts" in version_data:
            artifact = next(iter(version_data["artifacts"].keys()), None)
            if artifact:
                print(f"- Found artifact {artifact}\n")
                download_url = construct_download_url(artifact, mc_version)
                sponge_downloads[mc_version] = download_url

        else:
            print(f"Error: No artifact found for Minecraft version {mc_version}")

    save_to_json(sponge_downloads, "sponge_downloads.json")


def main():
    """Main which executes everything."""
    process_minecraft_versions()


if __name__ == "__main__":
    main()
