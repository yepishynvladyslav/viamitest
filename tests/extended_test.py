"""VIAMI TEST additional browser checks.
Requires a running local server on port 8765 and Playwright.
"""
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 390, "height": 844})
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.goto("http://127.0.0.1:8765/", wait_until="domcontentloaded")
        page.get_by_role("button", name="Посмотреть рабочее демо").click()
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        page.get_by_role("button", name="Каталог").click()
        page.get_by_role("button", name="Создать поездку").click()
        form = page.locator("#new-trip-form")
        form.locator("[name=title]").fill("Автопутешествие в Норвегию")
        form.locator("[name=country]").fill("Норвегия")
        form.locator("[name=city]").fill("Берген")
        form.locator("[name=from]").fill("Варшава")
        form.locator("[name=budget]").fill("1750")
        form.locator("[name=desc]").fill("Поездка для тестирования фильтров и групп")
        form.get_by_role("button", name="Опубликовать демо-поездку").click()
        assert page.get_by_text("Автопутешествие в Норвегию").count() > 0
        page.get_by_role("button", name="Фильтры").click()
        page.locator("#filter-form [name=maxBudget]").fill("1000")
        page.get_by_role("button", name="Показать предложения").click()
        assert page.get_by_text("Автопутешествие в Норвегию").count() == 0
        page.get_by_role("button", name="Фильтры").click()
        page.locator("#filter-form").get_by_role("button", name="Сбросить всё").click()
        assert page.get_by_text("Автопутешествие в Норвегию").count() > 0
        page.get_by_role("button", name="Поездки").click()
        page.get_by_role("button", name="Добавить точку").click()
        page.locator("#stop-form [name=stop]").fill("Новый пляж")
        page.locator("#stop-form button").click()
        assert page.get_by_text("Новый пляж").count() == 1
        assert not errors, errors
        browser.close()
    print("PASS: responsive layout, create trip, price filter, stop creation")

if __name__ == "__main__":
    main()
