-- создаём пользователя
CREATE ROLE crud_db_user WITH LOGIN PASSWORD 'SomePassword123!';

-- даём доступ к БД
GRANT CONNECT ON DATABASE em_auth_db TO crud_db_user;
-- даём доступ к схеме
GRANT USAGE ON SCHEMA public TO crud_db_user;

-- даём CRUD на все текущие таблицы
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO crud_db_user;

-- чтобы новые таблицы тоже были доступны автоматически:
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO crud_db_user;
