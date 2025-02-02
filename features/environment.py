from playwright.sync_api import Playwright, sync_playwright, Page, Browser
from behave.runner import Context
import json

# Define a custom context class to add type hints
class CustomContext(Context):
    playwright: Playwright # Represents the Playwright instance
    browser: Browser # Represents the Browser instance
    page: Page # Represents the Page instance

def before_all(context: CustomContext):
    # This function is called before all tests start
    print("Starting Playwright...")

    # Load environment variables from env.json
    with open("config/env.json", "r") as f:
        env_vars = json.load(f)

    # Accessing variables from env.json
    browser_type = env_vars["browser_name", "chromium"]
    headless_mode = env_vars["headless", False]

    context.playwright = sync_playwright().start()
    context.browser = context.playwright[browser_type].launch(headless=headless_mode, args=['--start-maximized'])
    context.page = context.browser.new_page()

def before_scenario(context: CustomContext, scenario):
    # This function is called before each scenario
    print(f"Starting scenario: {scenario.name}")
    context.page = context.browser.new_page(no_viewport=True) # Create a new page for the scenario


