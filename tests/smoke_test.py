"""VIAMI TEST browser smoke test.
Requires: pip install playwright && playwright install chromium
Run: python -m http.server 8765 (in a separate shell), then python tests/smoke_test.py
"""
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8765/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.goto(URL, wait_until="domcontentloaded")
        page.get_by_role("button", name="Посмотреть рабочее демо").click()
        assert page.get_by_text("Поездки, которые вдохновляют").count() == 1
        page.get_by_role("button", name="Каталог").click()
        assert page.get_by_text("Исследуй. Находи. Поезжай.").count() == 1
        page.get_by_role("button", name="Автопутешествия").click()
        assert page.get_by_text("Лыжи в словацких Татрах").count() >= 1
        page.get_by_role("button", name="Все", exact=True).click()
        page.locator('[data-action=detail][data-id=slovakia]').first.click()
        page.get_by_role("button", name="Хочу присоединиться").click()
        assert page.get_by_text("Заявка уже отправлена").count() == 1
        page.get_by_role("button", name="Открыть демо-чат").click()
        page.locator("#chat-form input[name=message]").fill("Тестовое сообщение")
        page.locator("#chat-form button").click()
        assert page.get_by_text("Тестовое сообщение").count() == 1
        page.get_by_role("button", name="Поездки").click()
        page.get_by_role("button", name="Начать день").click()
        page.get_by_role("button", name="Посетил", exact=True).first.click()
        assert page.get_by_text("1 из 5 мест посещено").count() == 1
        page.get_by_role("button", name="VIA AI").click()
        page.locator("#flight-form").get_by_role("button", name="Подобрать даты").click()
        assert page.locator(".flight-result").count() > 0
        page.get_by_role("button", name="Профиль", exact=True).last.click()
        page.get_by_role("button", name="Поддержка").last.click()
        page.locator("#support-form input").fill("Тест поддержки")
        page.locator("#support-form button").click()
        assert not errors, errors
        print("PASS: onboarding, catalog, filters, join, chat, itinerary, flights, support")
        browser.close()

if __name__ == "__main__":
    main()
