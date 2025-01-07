import os
import subprocess

BUILDTOOLS_LOCATION = "/Users/kim/Downloads/BuildTools.jar"
COMMAND_TEMPLATE = "{java_path} -Xms512M -jar {build_tools} --nogui --compile {compile_type} --rev {version}"

# List of minecraft versions
versions = [
    "1.8",
    "1.8.3",
    "1.8.4",
    "1.8.5",
    "1.8.6",
    "1.8.7",
    "1.8.8",
    "1.9",
    "1.9.2",
    "1.9.4",
    "1.10",
    "1.10.2",
    "1.11",
    "1.11.1",
    "1.11.2",
    "1.12",
    "1.12.1",
    "1.12.2",
    "1.13",
    "1.13.1",
    "1.13.2",
    "1.14",
    "1.14.1",
    "1.14.2",
    "1.14.3",
    "1.14.4",
    "1.15",
    "1.15.1",
    "1.15.2",
    "1.16.1",
    "1.16.2",
    "1.16.3",
    "1.16.4",
    "1.16.5",
    "1.17",
    "1.17.1",
    "1.18.1",
    "1.18.2",
    "1.19",
    "1.19.1",
    "1.19.2",
    "1.19.3",
    "1.19.4",
    "1.20.1",
    "1.20.2",
    "1.20.3",
    "1.20.4",
    "1.20.5",
    "1.20.6",
    "1.21",
    "1.21.1",
    "1.21.2",
    "1.21.3",
    "1.21.4",
]

# Minecraft versions with their respective java runtime version
java_requirements = {
    "1.8": "8",
    "1.8.3": "8",
    "1.8.4": "8",
    "1.8.5": "8",
    "1.8.6": "8",
    "1.8.7": "8",
    "1.8.8": "8",
    "1.9": "8",
    "1.9.2": "8",
    "1.9.4": "8",
    "1.10": "8",
    "1.10.2": "8",
    "1.11": "8",
    "1.11.1": "8",
    "1.11.2": "8",
    "1.12": "11",
    "1.12.1": "11",
    "1.12.2": "11",
    "1.13": "11",
    "1.13.1": "11",
    "1.13.2": "11",
    "1.14": "11",
    "1.14.1": "11",
    "1.14.2": "11",
    "1.14.3": "11",
    "1.14.4": "11",
    "1.15": "11",
    "1.15.1": "11",
    "1.15.2": "11",
    "1.16.1": "11",
    "1.16.2": "11",
    "1.16.3": "11",
    "1.16.4": "11",
    "1.16.5": "16",
    "1.17": "17",
    "1.17.1": "17",
    "1.18.1": "17",
    "1.18.2": "17",
    "1.19": "17",
    "1.19.1": "17",
    "1.19.2": "17",
    "1.19.3": "17",
    "1.19.4": "17",
    "1.20.1": "21",
    "1.20.2": "21",
    "1.20.3": "21",
    "1.20.4": "21",
    "1.20.5": "21",
    "1.20.6": "21",
    "1.21": "21",
    "1.21.1": "21",
    "1.21.2": "21",
    "1.21.3": "21",
    "1.21.4": "21",
}

# Java paths for 8, 11, 16, 17 and 21 which need to be set
java_paths = {
    "8": "/Library/Java/JavaVirtualMachines/temurin-8.jdk/Contents/Home/bin/java",  # Set the actual path to Java 8
    "11": "/Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/bin/java",  # Set the actual path to Java 11
    "16": "/Library/Java/JavaVirtualMachines/temurin-16.jdk/Contents/Home/bin/java",  # Set the actual path to Java 16
    "17": "/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin/java",  # Set the actual path to Java 17
    "21": "/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home/bin/java",  # Set the actual path to Java 21
}


def run_command(command: str):
    """Method to call subprocess

    Args:
        command (str): The command to execute
    """
    try:
        print(f"Running command: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while building: {e}")


for version in versions:
    required_java_version = java_requirements.get(version)

    if required_java_version and java_paths.get(required_java_version):
        java_path = java_paths[required_java_version]
        print(
            f"Trying to build minecraft version {version} with Java version {required_java_version}:"
        )

        # Compiling each version for craftbukkit & spigot:
        for compile_type in ["craftbukkit", "spigot"]:
            command = COMMAND_TEMPLATE.format(
                java_path=java_path,
                build_tools=BUILDTOOLS_LOCATION,
                compile_type=compile_type,
                version=version,
            )
            run_command(command)
    else:
        print(
            f"Skipping minecraft version {version} as the required Java version ({required_java_version}) is not available."
        )

print("Whole build process completed.")
