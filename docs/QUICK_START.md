# 🚀 Быстрый старт

Запуск проекта за 5 минут.

---

## 1. Генерация JWT ключей (опционально)

Ключи уже есть в репозитории для упрощения проверки. Если нужны новые:

```bash
# Приватный ключ
openssl genrsa -out secrets/keys/private_jwt.pem 2048

# Публичный ключ
openssl rsa -in secrets/keys/private_jwt.pem -outform PEM -pubout -out secrets/keys/public_jwt.pem
```

---

## 2. Запуск через Docker (рекомендуется)

```bash
# Запустить все сервисы
docker-compose up --build -d

# Проверить статус
docker-compose ps

# Должно быть:
# pg_db     Up (healthy)
# redis     Up
# web_app   Up (healthy)
```

---

## 3. Проверка

```bash
# Healthcheck
curl http://127.0.0.1:8100/api/v1/public/healthcheck

# Ожидается: {"status":"ok"}
```

---

## 4. Swagger UI

Откройте в браузере:

**http://127.0.0.1:8100/api/v1/public/docs**

---

## 5. Тестовые запросы

### Регистрация

```bash
curl -X POST http://127.0.0.1:8100/api/v1/public/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "passw": "SecurePass123!",
    "first_name": "Test",
    "surname": "User",
    "last_name": "Testovich"
  }'
```

### Вход

```bash
curl -X POST http://127.0.0.1:8100/api/v1/public/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "passw": "SecurePass123!"
  }' -v
```

Сохраните cookies из ответа для дальнейших запросов.

---

## 6. Остановка

```bash
# Остановить все сервисы
docker-compose down

# Остановить и удалить volumes
docker-compose down -v
```

---

## Локальный запуск (для разработки)

```bash
# Активировать окружение
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Запустить приложение
python -m core.main
```

**URL:** http://127.0.0.1:8000/api/v1/public/docs

---

## Troubleshooting

### Порт занят

```bash
# Изменить порт в docker-compose.yml
ports:
  - "127.0.0.1:8200:8000"  # Используем 8200 вместо 8100
```

### Контейнер не запускается

```bash
# Проверить логи
docker-compose logs web_app

# Проверить healthcheck
docker inspect web_app --format='{{.State.Health.Status}}'
```

### База данных недоступна

```bash
# Проверить статус PostgreSQL
docker-compose ps pg_db

# Проверить логи
docker-compose logs pg_db
```

---

## Следующие шаги

- [Документация по авторизации](AUTHORIZATION.md)
- [Документация по БД](DATABASE.md)
- [Документация по матрице доступа](ACCESS_MATRIX.md)
- [API Reference](API_REFERENCE.md)

---

**Готово!** Проект запущен и готов к использованию! 🎉
