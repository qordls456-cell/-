import os
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Get the absolute path of the index.html file
    file_path = os.path.abspath('index.html')

    page.goto(f'file://{file_path}')

    # Click the start button
    page.locator("#startStopBtn").click()

    # Wait for 3 seconds for the timer to update
    page.wait_for_timeout(3000)

    # Assert that the display is not "00:00:00"
    display = page.locator("#display")
    expect(display).not_to_have_text("00:00:00")

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)