# Minecraft Server Fork Direct Download

This repository contains various Python scripts for easy Minecraft server download and compilation. It automatically scrapes and lists the latest versions of popular Minecraft server types, including Vanilla, PaperMC and Sponge every three days, with additional server types to follow.

---

### I own said Tools/Pages/APIs etc. and want the scraping to stop!
- The json files are automatically built every three days by workflows, which scrape the data, if you are the owner of one of those APIs/Pages/Tools and want me to remove/stop the usage/scraping of said API/Page/Tool, please contact me I will take it down without hesitation!
- Mail: ciranuxdev
- Host: gmail
- Subject: "Takedown/Scraping Stop"

---

## Features

- Fetch and compile all available minecraft versions of Spigot and CraftBukkit using spigotmc's BuildTools.
- Download Vanilla, PaperMC, sponge and soon other server JARs easily using their direct files (look at [How to Build/Get server X Now?](#how-to-buildget-server-x-now))
- The json files in the repository should contain all (available) download links to directly download the files.

---

## Scripts Overview

### 1. **Spigot Build Tools Script**
Compiles Spigot and CraftBukkit JARs for specified Minecraft versions using [BuildTools](https://www.spigotmc.org/wiki/buildtools/).

#### Requirements:
- **Java 8, 11, 16, 17, 21** installed and configured in the script.
- BuildTools downloaded from SpigotMC.

#### Usage:
1. Install required Java versions.
2. Update the script with Java paths.
3. Run the script to build JARs.

---

### 2. **Vanilla Server Download Script**
Fetches Minecraft release version information and identifies available server download links.

#### Output:
- Generates 'release_vanilla_downloads.json' file with all server.jar files directly downloadable from mojang for each version (only full releases).
- For the snapshots look into the 'snapshot_vanilla_downloads.json' file to download those directly from mojang.

---

### 3. **PaperMC Crawler**
Uses the [PaperMC API](https://api.papermc.io) to get the latest PaperMC builds.

#### Output:
- Generates `paper_downloads.json` with build links for each Minecraft version.

---

### 4. **Sponge Crawler**
Uses the [Sponge API](https://dl-api.spongepowered.org/v2) to get the latest builds.

#### Output:
- Generates `sponge_downloads.json` with build links for each (available) Minecraft version.

---

## Dependencies

- **Install required Python packages**:
  - ```pip install selenium webdriver-manager requests```
  - selenium & webdriver-manager are needed for [getbukkit_crawler](old/main_getbukkit_crawler.py)
  - requests is used in every API-crawler script

- **Java Versions**:
  - Only for the buildtools script needed
  - Ensure all required Java versions are installed for BuildTools, check the [script](main_buildtools_runner.py)'s "java_paths" dict for that.

---

## How to Build/Get server X Now?

- To show where or how to get the latest or some specific version you can take a look at the following pages/tools:

### Vanilla (Done)
- Head to [minecraft.net](https://www.minecraft.net/en-us/download/server) to download the latest version or check:
  - Releases: '[release_vanilla_downloads.json](release_vanilla_downloads.json)'
  - Snapshots: '[snapshot_vanilla_downloads.json](snapshot_vanilla_downloads.json)'.

### Paper (Done)
- Head to [PaperMC](https://papermc.io/downloads/paper) to download the latest version or check:
  - '[paper_downloads.json](paper_downloads.json)'.

### Sponge (Done)
- Download from [Sponge's official page](https://spongepowered.org/downloads/spongevanilla) to download different versions or check:
  - '[sponge_downloads.json](sponge_downloads.json)' (I didnt test the files, if something is wrong open an issue please).

### Forge (Done)
- Head to [Forge's official site](https://files.minecraftforge.net/net/minecraftforge/forge/) to download different versions or check:
  - '[forge_downloads.json](forge_downloads.json)' (I didnt test the files, if something is wrong open an issue please).

### Spigot ([DMCA](#dmca-bukkit))
- Use the [BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar) directly or via the provided Python script to build all versions available.

### Fabric (WIP)
- Go to [Fabric's server page](https://fabricmc.net/use/server/) to download the desired version - WIP: (check `fabric_downloads.json` for available versions.)

### NeoForge (WIP)
- Visit [NeoForge's download page](https://projects.neoforged.net/neoforged/neoforge) - WIP: (check `neoforge_downloads.json` for available versions.)

---

## Future Plans
- Implement the missing server/loader types with scripts and workflows (GitHub Actions) like forge, neoforge and fabric.
- Maybe make the buildtools-script use multiple threads to enhance the build time.
- Automatically create a unified list containing direct download links for all Minecraft versions across all server types for the easiest access!
- Add auto download of newest buildtools to buildtools_script.
- Add automatic retrieval of all minecraft versions for all scripts that are hard-coded right now.

---

## Important Disclaimer ⚠
This repository does not host any Minecraft server files and is not affiliated with Mojang/Microsoft, SpigotMC, or PaperMC. The scripts only automate fetching or compiling files from publicly available tools or APIs.

---

## DMCA-Bukkit:
Due to licensing issues, Spigot and CraftBukkit cannot be distributed directly. You must compile them yourself using BuildTools.
See the stupid thing for yourself: https://github.com/github/dmca/blob/master/2014/2014-09-05-CraftBukkit.md

---

## License

This project is licensed under the GPL-3.0 license. See the [GPL-3.0 License](LICENSE) file for details.