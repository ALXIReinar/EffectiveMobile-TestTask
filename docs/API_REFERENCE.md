# 📡 API Reference

Полная документация всех API эндпоинтов с примерами запросов.

---

## 📋 Содержание

- [Авторизация](#авторизация)
- [Пользователи](#пользователи)
- [Матрица доступа](#матрица-доступа)
- [Сервисы](#сервисы)

---

## Базовый URL

- **Docker:** `http://127.0.0.1:8100/api/v1`
- **Локально:** `http://127.0.0.1:8000/api/v1`

---

## Авторизация

### Регистрация

```bash
POST /public/users/register
```

**Body:**
```json
{
  "email": "user@example.com",
  "passw": "SecurePass123!",
  "first_name": "John",
  "surname": "Doe",
  "last_name": "Smith"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "surname": "Doe",
  "last_name": "Smith",
  "is_active": true
}
```

### Вход

```bash
POST /public/users/login
```

**Body:**
```json
{
  "email": "user@example.com",
  "passw": "SecurePass123!"
}
```

**Response:** `200 OK`
```json
{
  "message": "Успешный вход"
}
```

**Cookies:**
```
Set-Cookie: access_token=eyJhbGc...; HttpOnly; Secure; SameSite=Strict
Set-Cookie: refresh_token=eyJhbGc...; HttpOnly; Secure; SameSite=Strict
```

### Обновление токена

```bash
POST /public/users/refresh
Cookie: refresh_token=eyJhbGc...
```

**Response:** `200 OK`

**Cookies:**
```
Set-Cookie: access_token=eyJhbGc...; HttpOnly; Secure; SameSite=Strict
```

### Выход

```bash
POST /users/logout
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Успешный выход"
}
```

---

## Пользователи

### Получить профиль

```bash
GET /users/me
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "surname": "Doe",
  "last_name": "Smith",
  "role": "data_analyst",
  "is_active": true
}
```

---

## Матрица доступа

### Roles (Роли)

#### Получить все роли

```bash
GET /admin/matrix/roles
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "admin",
    "description": "Полный доступ к системе"
  },
  {
    "id": 2,
    "name": "data_analyst",
    "description": "Аналитика данных"
  }
]
```

#### Создать роль

```bash
POST /admin/matrix/roles
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "content_manager",
  "description": "Управление контентом"
}
```

**Response:** `201 Created`
```json
{
  "id": 7,
  "name": "content_manager",
  "description": "Управление контентом"
}
```

#### Обновить роль

```bash
PUT /admin/matrix/roles/7
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "content_manager",
  "description": "Управление контентом и медиа"
}
```

**Response:** `200 OK`

#### Удалить роль

```bash
DELETE /admin/matrix/roles/7
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Роль удалена"
}
```

### Services (Сервисы)

#### Получить все сервисы

```bash
GET /admin/matrix/services
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "analytics",
    "description": "Аналитика и метрики"
  },
  {
    "id": 2,
    "name": "finance",
    "description": "Финансы и бюджет"
  }
]
```

#### Создать сервис

```bash
POST /admin/matrix/services
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "reporting",
  "description": "Отчеты и аналитика"
}
```

**Response:** `201 Created`
```json
{
  "id": 4,
  "name": "reporting",
  "description": "Отчеты и аналитика"
}
```

#### Обновить сервис

```bash
PUT /admin/matrix/services/4
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "reporting",
  "description": "Отчеты, аналитика и дашборды"
}
```

**Response:** `200 OK`

#### Удалить сервис

```bash
DELETE /admin/matrix/services/4
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Сервис удален"
}
```

### Actions (Действия)

#### Получить все действия

```bash
GET /admin/matrix/actions
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "read",
    "description": "Чтение данных"
  },
  {
    "id": 2,
    "name": "write",
    "description": "Запись данных"
  }
]
```

#### Создать действие

```bash
POST /admin/matrix/actions
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "export",
  "description": "Экспорт данных"
}
```

**Response:** `201 Created`
```json
{
  "id": 4,
  "name": "export",
  "description": "Экспорт данных"
}
```

#### Обновить действие

```bash
PUT /admin/matrix/actions/4
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "name": "export",
  "description": "Экспорт данных в различных форматах"
}
```

**Response:** `200 OK`

#### Удалить действие

```bash
DELETE /admin/matrix/actions/4
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Действие удалено"
}
```

### Permissions (Права)

#### Получить все права

```bash
GET /admin/matrix/permissions
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "service_id": 1,
    "action_id": 1,
    "service_name": "analytics",
    "action_name": "read"
  },
  {
    "id": 2,
    "service_id": 1,
    "action_id": 2,
    "service_name": "analytics",
    "action_name": "write"
  }
]
```

#### Создать право

```bash
POST /admin/matrix/permissions
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "service_id": 4,
  "action_id": 1
}
```

**Response:** `201 Created`
```json
{
  "id": 10,
  "service_id": 4,
  "action_id": 1,
  "service_name": "reporting",
  "action_name": "read"
}
```

#### Удалить право

```bash
DELETE /admin/matrix/permissions/10
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Право удалено"
}
```

### Role Permissions (Назначение прав)

#### Получить права роли

```bash
GET /admin/matrix/roles/2/permissions
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
[
  {
    "permission_id": 1,
    "service_name": "analytics",
    "action_name": "read"
  },
  {
    "permission_id": 2,
    "service_name": "analytics",
    "action_name": "write"
  }
]
```

#### Назначить право роли

```bash
POST /admin/matrix/roles/2/permissions
Cookie: access_token=eyJhbGc...
```

**Body:**
```json
{
  "permission_id": 10
}
```

**Response:** `201 Created`
```json
{
  "message": "Право назначено роли"
}
```

#### Отозвать право у роли

```bash
DELETE /admin/matrix/roles/2/permissions/10
Cookie: access_token=eyJhbGc...
```

**Response:** `200 OK`
```json
{
  "message": "Право отозвано у роли"
}
```

---

## Сервисы

### Analytics

#### Получить метрики

```bash
GET /analytics/metrics
Cookie: access_token=eyJhbGc...
```

**Требуется:** `analytics:read`

**Response:** `200 OK`
```json
{
  "metrics": [
    {"name": "users", "value": 1000},
    {"name": "revenue", "value": 50000}
  ]
}
```

### Finance

#### Получить бюджет

```bash
GET /finance/budget
Cookie: access_token=eyJhbGc...
```

**Требуется:** `finance:read`

**Response:** `200 OK`
```json
{
  "budget": {
    "total": 1000000,
    "spent": 750000,
    "remaining": 250000
  }
}
```

### Infrastructure

#### Получить статус серверов

```bash
GET /infrastructure/servers
Cookie: access_token=eyJhbGc...
```

**Требуется:** `infrastructure:read`

**Response:** `200 OK`
```json
{
  "servers": [
    {"name": "web-1", "status": "running"},
    {"name": "db-1", "status": "running"}
  ]
}
```

---

## Коды ответов

| Код | Описание |
|-----|----------|
| 200 | OK - успешный запрос |
| 201 | Created - ресурс создан |
| 400 | Bad Request - неверные данные |
| 401 | Unauthorized - требуется авторизация |
| 403 | Forbidden - недостаточно прав |
| 404 | Not Found - ресурс не найден |
| 500 | Internal Server Error - ошибка сервера |

---

## Ошибки

### 401 Unauthorized

```json
{
  "detail": "Требуется авторизация"
}
```

### 403 Forbidden

```json
{
  "detail": "Недостаточно прав для доступа к ресурсу"
}
```

### 400 Bad Request

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## Swagger UI

Интерактивная документация API:

- **Docker:** http://127.0.0.1:8100/api/v1/public/docs
- **Локально:** http://127.0.0.1:8000/api/v1/public/docs

---
