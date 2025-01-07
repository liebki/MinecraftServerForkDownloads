# Minecraft Server Fork Downloads

This repository contains various Python scripts which aim to make it easier to download and/or compile Minecraft server JAR files. The scripts automate the process for different Minecraft server types, including Spigot, CraftBukkit, Vanilla, and PaperMC.

Please note that these scripts do **not** host any Minecraft server files themselves and are not affiliated with Mojang/Microsoft, SpigotMC, or PaperMC in any way. They simply scrape links or use tools provided by these projects to fetch the latest versions. Always ensure that you comply with the respective Terms of Service (ToS) of the server types and software used.

I will definitly add other server types in the future, like quilt etc. my goal is to make them available in a simple list or page here.

## Scripts Overview

### 1. **Build Tools Script (SpigotMC)**

This script uses the [BuildTools](https://www.spigotmc.org/wiki/buildtools/) from SpigotMC to compile all available versions of CraftBukkit and Spigot. It downloads and builds the Minecraft server JAR file(s) for each version specified in the code.

#### Requirements:
- **Java 8, Java 11, Java 16, Java 17, Java 21**: The script requires these specific versions to compile all Minecraft versions. You must manually set the paths to each Java version in the script.

#### Output:
- A runnable **Minecraft server JAR file** (CraftBukkit or Spigot) will be created in the directory from which the script is executed for **each** version, this takes a while to compile and build.

#### Usage:
1. Ensure you have all the required Java versions installed on your system.
2. Modify the script to point to the correct Java version paths.
3. Execute the script to compile the desired Minecraft versions.

### 2. **GetBukkit.org Crawler**

This script crawls [getbukkit.org](https://getbukkit.org/) for download links of various Minecraft server types (Spigot, CraftBukkit, and Vanilla). It extracts the direct download URLs for the **Vanilla** version of the Minecraft server, as this is the only one that is useful for downloading from Mojang/Microsoft. But you can also get the spigot and craftbukkit links by just uncommenting those in "server_data".

#### Output:
- A **`getbukkit-versions.json`** file containing:
  - **Version**: The Minecraft version.
  - **Name**: The name of the server type (e.g., Vanilla).
  - **Type**: The server type (e.g., Vanilla).
  - **Download Link**: A direct URL to download link (from getbukkit.org/Mojang/Microsoft).

#### Usage:
1. Run the script to gather all the direct download links

### 3. **PaperMC API Crawler**

This script interacts with the [PaperMC API](https://api.papermc.io) to retrieve the latest builds for PaperMC, a popular fork of Spigot. It scrapes the API for the latest build download links for each Minecraft version.

#### Output:
- A **`paper_downloads.json`** file containing:
  - **Version**: The Minecraft version.
  - **Download Link**: The direct download URL for the newest PaperMC build.

#### Usage:
1. Execute the script to get the latest PaperMC build download links.

## Dependencies

The following Python packages are required to run these scripts:

- **python** (version 3.10.0)
- **selenium**: For web scraping and automation.
- **webdriver-manager**: To handle browser drivers for Selenium.

To install the necessary dependencies, use pip:

```bash
pip install selenium webdriver-manager
```

## Important Notes

- **Java Versions**: The Build Tools script requires Java 8, 11, 16, 17, and 21 to compile all Minecraft versions. Please ensure that you have these versions installed and/or configured in the script.
- **Legal Disclaimer**:
  - These scripts do not host any files, and the author is not affiliated with Mojang/Microsoft, SpigotMC, or PaperMC. They are just helper tools to download and compile the respective Minecraft server files.
  - Always ensure you comply with the Terms of Service of each server software (Spigot, PaperMC, Mojang, etc.).
  - The files produced by these scripts are solely for personal use, and the author is not responsible for any misuse or distribution of the files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial tool designed to facilitate the process of downloading and compiling Minecraft server JAR files. This tool is provided "as is" without any guarantees or support. The use of this script is at your own risk.

---

**Note**: If you're unsure about the legal implications of using these scripts or downloading Minecraft server files, please refer to the official licensing and Terms of Service of each platform (Mojang, SpigotMC, PaperMC, etc.).