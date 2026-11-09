# VIAMI TEST — публикация через GitHub

> **Демо, не production.** Данные сохраняются только на устройстве. Нет реальных входов Apple/Google, серверной авторизации, безопасной админ-панели, покупки билетов, настоящего KYC и платежей. **Не вводите настоящие паспортные или платежные данные.**

## Как создать GitHub-репозиторий

1. На сайте `https://github.com/new` создайте новый репозиторий с названием **viamitest**, без начального README, .gitignore и лицензии. Для просмотра по общедоступной ссылке через GitHub Pages удобнее выбрать **Public**. В прототипе нет серверных секретов, однако демонстрационная админка не защищена — не подключайте реальную базу до security review.
2. Загрузите файлы из распакованного проекта. Удобнее сделать это в GitHub Desktop либо локально через Git.
3. В настройках репозитория перейдите в **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Откройте **Actions**: workflow `Publish VIAMI TEST to GitHub Pages` автоматически опубликует сайт после push в `main`.
5. Адрес демо обычно `https://<ваш-логин>.github.io/viamitest/`. Адрес появится в **Settings → Pages** после успешного деплоя. На iPhone откройте его в Safari.

## Самый короткий способ выгрузить файлы с Windows через Git

В папке, куда распакован проект, откройте PowerShell/Terminal (установите Git, если его нет) и выполните:

```powershell
git init -b main
git add .
git commit -m "Initial VIAMI TEST interactive prototype"
git remote add origin https://github.com/<ВАШ_ЛОГИН>/viamitest.git
git push -u origin main
```

При необходимости GitHub попросит пройти аутентификацию через Git Credential Manager. Не вставляйте пароль или токен в чат.

## Что размещать

Публикуйте `index.html`, `style.css`, `app.js`, `manifest.webmanifest`, `sw.js`, `assets/`, `.github/workflows/pages.yml`, `.nojekyll`, `.gitignore`, `README_RU.md`, `GITHUB_START_HERE.md`, а также при желании тесты. `preview-offline.html` можно оставить как удобный офлайн-просмотр, он не попадёт в собранный GitHub Pages сайт.

## Запуск локально

```bash
python -m http.server 8765
```

Откройте `http://localhost:8765`.

## Важно о публикации

GitHub Pages делает файлы веб-сайта публично доступными по интернет-ссылке даже тогда, когда над проектом работают только тестировщики. Все демо-данные хранятся на конкретном устройстве в `localStorage`. Сброс данных браузера удалит их. Не используйте настоящие личные данные в демонстрационных полях.