# from datetime import datetime
# import asyncio
# from playwright.async_api import async_playwright


# async def run(playwright):
#     chromium = playwright.chromium
#     browser = await chromium.launch(headless=False)
#     device = playwright.devices["iPad Mini"]
#     # context = await browser.new_context(**device)

#     page = await browser.new_page()
#     await page.goto("https://www.washingtonpost.com")
#     await page.wait_for_load_state("networkidle")
#     # await page.evaluate("document.body.style.zoom=0.4")

#     #! This has the no effect
#     # await page.evaluate("async() => {for (let i = 0; i < document.body.scrollHeight; i+=100) {window.scrollTo({top: 0, left:i, behaviour: 'smooth'})}}")
#     # await page.wait_for_timeout(6000)

#     date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

#     await page.screenshot(path='screenshots/{}-wapo.png'.format(date), full_page=True)
#     await browser.close()


# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)
# asyncio.run(main())


testing_if_works = True
