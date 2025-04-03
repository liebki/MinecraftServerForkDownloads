"""Simple script to get all forge server jar direct download links using selenium."""

# pylint: disable=W0718

import json
import sys
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def fetch_hrefs(driver):
    """
    Fetches all href links from the main page and strips from adfocus link.

    Args:
        driver (webdriver.Firefox): The WebDriver instance.

    Returns:
        list: A list of cleaned href URLs.
    """
    driver.get("https://files.minecraftforge.net/net/minecraftforge/forge/")
    driver.implicitly_wait(10)

    li_version_list_elements = driver.find_elements(By.CLASS_NAME, "li-version-list")
    print(f"Found {len(li_version_list_elements)} 'li-version-list' elements.")

    hrefs = []
    for element in li_version_list_elements:
        ul_element = element.find_element(By.CSS_SELECTOR, "ul.nav-collapsible")
        li_elements = ul_element.find_elements(By.CSS_SELECTOR, "li:not([class])")

        for li in li_elements:
            a_tag = li.find_element(By.TAG_NAME, "a")
            href = a_tag.get_attribute("href")
            href = href.replace("https://adfoc.us/serve/sitelinks/?id=271228&url=", "")
            hrefs.append(href)

    return hrefs


def process_link(driver, link):
    """
    Processes each link, retrieves the title, and finds the appropriate download link.

    Args:
        driver (webdriver.Firefox): The WebDriver instance.
        link (str): The URL to process.

    Returns:
        str: The stripped title.
        str: The found href URL.
    """
    try:
        driver.get(link)

        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/h1")
            )
        )

        title_text = title_element.text
        stripped_title = title_text.replace(
            "Downloads for Minecraft Forge - MC ", ""
        ).strip()

        href_found = None
        for title in ["Installer", "Universal", "Server"]:
            try:
                a_tag = driver.find_element(By.XPATH, f"//a[@title='{title}']")
                href_found = a_tag.get_attribute("href")
                href_found = href_found.replace(
                    "https://adfoc.us/serve/sitelinks/?id=271228&url=", ""
                )
                break
            except Exception:
                continue

        return stripped_title, href_found

    except Exception as e:
        print(f"Error processing link {link}: {e}")
        return None, None


def main():
    """Main which executes everything."""
    result_dict = {}

    driver = initialize_driver()
    hrefs = fetch_hrefs(driver)

    for link in hrefs:
        stripped_title, href_found = process_link(driver, link)

        if stripped_title and href_found:
            result_dict[stripped_title] = href_found

    save_to_json(result_dict, "forge_downloads.json")
    driver.quit()


if __name__ == "__main__":
    main()
