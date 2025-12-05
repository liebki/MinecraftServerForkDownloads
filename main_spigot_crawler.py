"""Simple script to get all Spigot server jar direct download links using selenium."""

# pylint: disable=W0718

import json
import sys
import time
from urllib.parse import urljoin
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


BASE_URL = "https://files.mcjars.app/spigot/"
OUTPUT_FILENAME = "spigot_downloads.json"
DIRECTORY_WAIT_SECONDS = 30
REQUEST_DELAY_SECONDS = 5


def throttle_requests():
    """Pause between requests to avoid rate limiting."""
    if REQUEST_DELAY_SECONDS > 0:
        time.sleep(REQUEST_DELAY_SECONDS)


def save_to_json(data, filename: str):
    """
    Saves given data to a JSON file.

    Args:
        data (dict): The data to write to the file.
        filename (str): The name of the output file.
    """
    with open(file=filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Download links saved to {filename}")


def initialize_driver():
    """
    Initialize the WebDriver with options.

    Returns:
        webdriver.Firefox: The initialized WebDriver.
    """
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")

        options.add_argument("--no-sandbox")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=options
        )
        return driver
    except Exception as e:
        print(f"Error initializing the WebDriver: {e}")
        sys.exit(1)


def wait_for_directory_listing(driver, timeout: int = DIRECTORY_WAIT_SECONDS) -> bool:
    """Wait for the directory listing table to be present."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tr td a"))
        )
        return True
    except TimeoutException:
        return False


def fetch_versions(driver):
    """
    Fetch all available Spigot versions listed on the main page.

    Args:
        driver (webdriver.Firefox): The WebDriver instance.

    Returns:
        list[tuple[str, str]]: (version, version_url) pairs in listing order.
    """
    driver.get(BASE_URL)
    if not wait_for_directory_listing(driver):
        print("Timed out waiting for the Spigot versions directory listing.")
        return []
    throttle_requests()

    versions = []
    for anchor in driver.find_elements(By.CSS_SELECTOR, "table tr td a"):
        text = anchor.text.strip()
        if not text or text == "[Parent Directory]":
            continue
        if not text.endswith("/"):
            continue
        version = text.rstrip("/")
        href = anchor.get_attribute("href")
        versions.append((version, href))

    return versions


def fetch_latest_build_number(driver, version_url):
    """Return the highest numeric build directory available for the version."""
    driver.get(version_url)
    if not wait_for_directory_listing(driver):
        print(f"Timed out waiting for build listings at {version_url}")
        throttle_requests()
        return None

    throttle_requests()

    build_numbers = []
    for anchor in driver.find_elements(By.CSS_SELECTOR, "table tr td a"):
        text = anchor.text.strip()
        if not text or text == "[Parent Directory]":
            continue
        if not text.endswith("/"):
            continue
        candidate = text.rstrip("/")
        if candidate.isdigit():
            build_numbers.append(int(candidate))

    if not build_numbers:
        return None

    return str(max(build_numbers))


def main():
    """Main which executes everything."""
    result_dict = {}

    driver = initialize_driver()
    try:
        versions = fetch_versions(driver)
        print(f"Found {len(versions)} Spigot version directories.")

        for version, version_url in versions:
            latest_build = fetch_latest_build_number(driver, version_url)
            if not latest_build:
                print(f"No build directories found for version {version}.")
                continue

            server_jar_url = urljoin(version_url, f"{latest_build}/server.jar")
            result_dict[version] = server_jar_url
            print(f"Latest build for {version}: {latest_build}")
    finally:
        driver.quit()

    save_to_json(result_dict, OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
