# Minecraft Server Fork Downloads

This repository contains Python scripts to simplify downloading and compiling Minecraft server JAR files. It supports different server types like Spigot, CraftBukkit, Vanilla, and PaperMC.

---

## Features

- Fetch and compile all minecraft versions of Spigot and CraftBukkit using spigotmc's BuildTools.
- Download Vanilla, PaperMC, and other server JARs.
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

### 2. **GetBukkit.org Crawler**
Scrapes Vanilla, Spigot, and CraftBukkit download links from [getbukkit.org](https://getbukkit.org/).

#### Output:
- Generates `getbukkit-versions.json` with version details and download links.

---

### 3. **PaperMC API Crawler**
Uses the [PaperMC API](https://api.papermc.io) to get the latest PaperMC builds.

#### Output:
- Generates `paper_downloads.json` with build links for each Minecraft version.

---

## Dependencies

- **Install required Python packages**:
  ```bash
  pip install selenium webdriver-manager
  ````

- **Java Versions**: 
  - Ensure all required Java versions are installed for BuildTools, check the [script](main_buildtools_runner.py)'s "java_paths" dict for that.

---

## How to Build/Get server X Now?

To show where or how to get the latest or some specific version you can take a look at the following pages/tools:

### Vanilla
- Head to [minecraft.net](https://www.minecraft.net/en-us/download/server) to download the latest version or check 'getbukkit_downloads.json' or 'only_vanilla_downloads.json'.

### Spigot
- Use the [BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar) directly or via the provided Python script.

### Paper
- Head to [PaperMC](https://papermc.io/downloads/paper) to download the latest version or check 'paper_downloads.json'.

### Fabric
- Go to [Fabric's server page](https://fabricmc.net/use/server/) to download the desired version - WIP: (check `fabric_downloads.json` for available versions.)

### NeoForge
- Visit [NeoForge's download page](https://projects.neoforged.net/neoforged/neoforge) - WIP: (check `neoforge_downloads.json` for available versions.)

### Sponge
- Download from [Sponge's official page](https://spongepowered.org/downloads/spongevanilla) - WIP: (check `sponge_downloads.json` for available versions.)

### Forge
- Head to [Forge's official site](https://files.minecraftforge.net/net/minecraftforge/forge/) - WIP: (check `forge_downloads.json` for available versions.)

---

## Future Plans
- Remove vanilla scraper from getbukkit_crawler and create own vanilla_scrape script to get everything directly from mojang
- Implement the missing server/loader types with scripts and workflows (GitHub Actions) like forge, neoforge, sponge and fabric.
- Maybe make the buildtools-script use multiple threads to enhance the build time
- Automatically create a unified list containing direct download links for all Minecraft versions across all server types for the easiest access!

---

## Important Disclaimer ⚠:  
This repository does not host any Minecraft server files and is not affiliated with Mojang/Microsoft, SpigotMC, or PaperMC. The scripts only automate fetching or compiling files from publicly available tools or APIs.

---

## Reminder ⚠:
Due to licensing issues, Spigot and CraftBukkit cannot be distributed directly. You must compile them yourself using BuildTools.


---

## License

This project is licensed under the GPL-3.0 license. See the [GPL-3.0 License](LICENSE) file for details.