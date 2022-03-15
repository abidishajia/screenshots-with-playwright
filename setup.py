from datetime import datetime
import asyncio
from playwright.async_api import async_playwright


async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    device = playwright.devices["iPad Mini"]
    # context = await browser.new_context(**device)

    page = await browser.new_page()
    await page.goto("https://www.washingtonpost.com")
    await page.wait_for_load_state("domcontentloaded")
    await page.set_viewport_size({"width": 1600, "height": 1000})
    page_height = await page.evaluate("() => document.body.scrollHeight")
    await page.set_viewport_size({"width": 1600, "height": page_height})
    # await page.evaluate("document.body.style.zoom=0.4")

    # await page.evaluate("""async() => {
    #     const timeout = (ms) => {
    #         return new Promise((resolve) => {
    #             setTimeout(resolve, ms);
    #         });
    #     };
    #     for (let i = 0; i < document.body.scrollHeight; i+=100) {
    #         window.scrollTo(0, i);
    #         await timeout(500);
    #     }
    # }""")
    await page.wait_for_timeout(6000)

    date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

    await page.screenshot(path='screenshots/{}-washingtonpost.png'.format(date), full_page=True)
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
