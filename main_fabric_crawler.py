import requests
import json

def save_to_json(data, filename: str):
    """
    Saves given data to a JSON file.

    Args:
        data (dict or list): The data to write to the file.
        filename (str): The name of the output file.
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Download links saved to {filename}")

url_game_versions = "https://meta.fabricmc.net/v2/versions/game"
game_versions_response = requests.get(url_game_versions)
game_versions_data = game_versions_response.json()

stable_game_versions = [version['version'] for version in game_versions_data if version['stable']] # release
non_stable_game_versions = [version['version'] for version in game_versions_data if not version['stable']] # snapshot

url_loader = "https://meta.fabricmc.net/v2/versions/loader"
loader_response = requests.get(url_loader)
loader_data = loader_response.json()
latest_loader_version = loader_data[0]['version']

url_installer = "https://meta.fabricmc.net/v2/versions/installer"
installer_response = requests.get(url_installer)
installer_data = installer_response.json()
latest_installer_version = installer_data[0]['version']

stable_download_urls = []
non_stable_download_urls = []
download_url_template = "https://meta.fabricmc.net/v2/versions/loader/{}/{}//{}/server/jar"

for minecraft_version in stable_game_versions:
    download_url = download_url_template.format(minecraft_version, latest_loader_version, latest_installer_version)
    stable_download_urls.append({
        "minecraft_version": minecraft_version,
        "download_url": download_url
    })

for minecraft_version in non_stable_game_versions:
    download_url = download_url_template.format(minecraft_version, latest_loader_version, latest_installer_version)
    non_stable_download_urls.append({
        "minecraft_version": minecraft_version,
        "download_url": download_url
    })

save_to_json(stable_download_urls, "release_fabric_downloads.json")
save_to_json(non_stable_download_urls, "snapshot_fabric_downloads.json")

print("done")