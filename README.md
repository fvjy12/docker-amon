<div align="center">

# 🐳 AMON Docker

**Production-ready Docker setup for Python Flask applications**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-22.0-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

**Профессиональная Docker-конфигурация для Python-приложений.**
**Multi-stage build, безопасность, healthcheck и production-ready деплой.**

</div>

---

## ✨ Возможности

| Фича | Описание |
|------|----------|
| 🚀 **Multi-stage build** | Оптимальный размер образа, быстрая сборка |
| 🔒 **Non-root user** | Безопасный запуск без прав root |
| 🩺 **Healthcheck** | Автоматическая проверка здоровья контейнера |
| ⚡ **Gunicorn** | Production WSGI-сервер с несколькими воркерами |
| 📦 **Named volumes** | Сохранение данных между перезапусками |
| 🌐 **Custom network** | Изолированная сеть для контейнеров |
| 📝 **Log rotation** | Автоматическая ротация логов |
| 🔧 **Environment config** | Настройка через .env файл |

---

## 📁 Структура проекта

```
docker/
├── Dockerfile          # Multi-stage build
├── docker-compose.yml  # Оркестрация
├── main.py             # Flask-приложение
├── requirements.txt    # Зависимости
├── .env.example        # Пример конфигурации
├── .dockerignore       # Исключения для сборки
└── README.md           # Документация
```

---

## 🚀 Быстрый старт

### 1. Клонируй и настрой

```bash
git clone https://github.com/fvjy12/docker-amon.git
cd docker-amon


# Настрой окружение
cp .env.example .env
```

### 2. Запусти

```bash
# Собрать и запустить
docker-compose up --build

# Запустить в фоне
docker-compose up -d

# Посмотреть логи
docker-compose logs -f
```

### 3. Проверь

```bash
# Проверка здоровья
curl http://localhost:8080/health

# Информация о приложении
curl http://localhost:8080/info
```

---

## 🌐 API Endpoints

| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/` | GET | Информация о приложении |
| `/health` | GET | Проверка здоровья |
| `/info` | GET | Информация о системе |
| `/time` | GET | Текущее время сервера |
| `/echo` | POST | Эхо-запрос (возвращает данные) |

---

## 🔧 Команды Docker

```bash
# Собрать образ
docker build -t amon-app .

# Запустить контейнер
docker run -p 8080:8080 amon-app

# Остановить
docker-compose down

# Остановить и удалить volume
docker-compose down -v

# Пересобрать
docker-compose up --build --force-recreate

# Посмотреть статус
docker-compose ps

# Логи
docker logs -f amon-app
```

---

## ⚙️ Конфигурация (.env)

| Переменная | По умолчанию | Описание |
|------------|--------------|----------|
| `APP_PORT` | `8080` | Порт приложения |
| `APP_ENV` | `production` | Окружение (production/development) |
| `APP_DEBUG` | `false` | Режим отладки |

---

## 🛡️ Безопасность

- ✅ Запуск от non-root пользователя
- ✅ Healthcheck для мониторинга
- ✅ Изолированная Docker-сеть
- ✅ Ротация логов (10MB x 3 файла)
- ✅ .dockerignore для исключения лишних файлов

---

## 📦 Требования

- Docker 20.10+
- Docker Compose 2.0+

---

## 📫 Контакты

[![GitHub](https://img.shields.io/badge/GitHub-fvjy12-181717?style=for-the-badge&logo=github)](https://github.com/fvjy12)

---

<div align="center">

**Made with ❤️ by [fvjy12](https://github.com/fvjy12)**

</div>
