import asyncio
import asyncpg
from core.config_dir.config import pool_settings, encryption


async def create_test_users():
    conn = await asyncpg.connect(**pool_settings)
    
    # Хешируем пароль "test123"
    hashed_password = encryption.hash("test123")
    
    test_users = [
        ('admin@company.com', 'Admin', 'User', 'Adminovich', 'admin'),
        ('devops@company.com', 'DevOps', 'Engineer', 'Devopsov', 'devops'),
        ('dev@company.com', 'John', 'Developer', 'Doe', 'developer'),
        ('pm@company.com', 'Jane', 'Manager', 'Smith', 'project_manager'),
        ('analyst@company.com', 'Data', 'Analyst', 'Johnson', 'data_analyst'),
        ('finance@company.com', 'Finance', 'Manager', 'Brown', 'finance_manager'),
        ('hr@company.com', 'HR', 'Specialist', 'Wilson', 'hr'),
        ('security@company.com', 'Security', 'Officer', 'Davis', 'security'),
    ]
    
    query = '''
    INSERT INTO users (email, passw, first_name, surname, last_name, role, is_active)
    VALUES ($1, $2, $3, $4, $5, $6, true)
    ON CONFLICT (email) WHERE is_active = true DO NOTHING
    RETURNING id
    '''
    
    print("Создаю тестовых пользователей...")
    print(f"Пароль для всех: test123")
    print(f"Хеш пароля: {hashed_password}\n")
    
    for email, first_name, surname, last_name, role in test_users:
        user_id = await conn.fetchval(query, email, hashed_password, first_name, surname, last_name, role)
        if user_id:
            print(f"✅ Создан: {email} (role: {role}, id: {user_id})")
        else:
            print(f"⚠️  Уже существует: {email}")
    
    await conn.close()
    print("\n✅ Готово! Все тестовые пользователи созданы.")


if __name__ == '__main__':
    asyncio.run(create_test_users())
