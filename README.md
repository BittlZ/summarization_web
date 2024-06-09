# summarization_web
### Project for our summarization and federalization product

## Описание файлов

1. Файл app/__init__.py - Инициализация приложения Flask.
2. Файл app/routes.py - Определение маршрутов для веб-приложения.
3. Файл app/summarizer.py - Адаптация существующей логики суммаризации.
4. Файл app/templates/index.html - HTML-шаблон для веб-интерфейса.
5. Файл app/static/styles.css - CSS для стилизации веб-интерфейса.
6. Файл app.py - Точка входа в приложение.
7. Файл requirements.txt - Список зависимостей.
8. Файл Procfile - Конфигурация для развертывания на Heroku.


## Инструкции по запуску

1.Установка зависимостей:
`pip install -r requirements.txt`

2.Запуск приложения локально:
`python app.py`

3.Развертывание на Heroku:
  3.1.Инициализируйте репозиторий Git:
`    git init
    git add .
    git commit -m "Initial commit"`
  3.2. Создайте приложение на Heroku:
  `  heroku create`
  3.3. Загрузите проект на Heroku:
`     git push heroku master`

