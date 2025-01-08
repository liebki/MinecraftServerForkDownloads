import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
import time

# How long to wait before doing anything after a page load
TIME_PAGELOAD = 2

# If getbukkit.org ever adds new pages with the same structure, they could be added here
server_data = [
    {"url": "https://getbukkit.org/download/spigot", "type": "Spigot"},
    {"url": "https://getbukkit.org/download/vanilla", "type": "Vanilla"},
    {"url": "https://getbukkit.org/download/craftbukkit", "type": "CraftBukkit"},
]

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

except Exception as e:
    print(f"Error initializing the WebDriver: {e}")
    exit(1)

initial_links = []

try:
    for server in server_data:
        driver.get(server["url"])
        time.sleep(TIME_PAGELOAD)

        download_panes = driver.find_elements(By.CLASS_NAME, "download-pane")
        print(f"Found {len(download_panes)} download pane-divs on {server['url']}.")

        for pane in download_panes:
            try:
                # First element with 'col-sm-3' class contains the version:
                version_element = pane.find_element(By.CLASS_NAME, "col-sm-3")
                version_name = version_element.text.strip()

                # Element with '#downloadr' contains the 1st stage download href:
                download_button = pane.find_element(By.CSS_SELECTOR, "#downloadr")
                link = download_button.get_attribute("href")

                if link:
                    initial_links.append(
                        {
                            "server_type": server["type"],
                            "version": version_name,
                            "link": link,
                        }
                    )
            except Exception as e:
                print(f"Error processing a pane: {e}")
                continue

    print(f"Collected {len(initial_links)} 1st stage links from all pages.")
    download_links = []

    for idx, item in enumerate(initial_links):
        try:
            driver.get(item["link"])
            time.sleep(TIME_PAGELOAD)

            # Use button with '//*[@id="get-download"]/div/div/div[2]/div/h2/a' xpath, has the direct download link:
            download_element = driver.find_element(
                By.XPATH, '//*[@id="get-download"]/div/div/div[2]/div/h2/a'
            )
            direct_link = download_element.get_attribute("href")

            download_links.append(
                {
                    "name": item["version"],
                    "server_type": item["server_type"],
                    "version": item["version"],
                    "direct_download_link": direct_link,
                }
            )
            print(
                f"[{idx + 1}/{len(initial_links)}] Collected: {item['version']} ({item['server_type']}) - {direct_link}"
            )

        except Exception as e:
            print(f"Error processing link {idx + 1}: {e}")
            continue

finally:
    if driver:
        driver.quit()

output_file = "getbukkit_versions.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(download_links, f, indent=4)

print(f"Download links saved to {output_file}")
