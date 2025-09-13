from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
import os

def run_accessibility_check(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Only explicitly set binary location if needed locally (Brave)
    if os.getenv("IS_STREAMLIT_CLOUD") != "true":
        chrome_options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    # Let Selenium find the driver automatically (works in Cloud)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        axe = Axe(driver)
        axe.inject()
        results = axe.run()
        violations = results["violations"]

        issues = []
        for v in violations:
            for node in v["nodes"]:
                issues.append({
                    "impact": v["impact"],
                    "description": v["description"],
                    "help": v["help"],
                    "help_url": v["helpUrl"],
                    "selector": ", ".join(node["target"]),
                    "html": node["html"],
                })

        return issues

    except Exception as e:
        print(f"Error: {e}")
        return []

    finally:
        driver.quit()
