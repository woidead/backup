import psycopg2

# Параметры подключения к базе данных PostgreSQL
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

# Функция для вывода денег
def withdraw_money(account_id, amount):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Проверяем, есть ли достаточно средств на счете
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        # Обновляем баланс счета
        new_balance = balance - amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s", (new_balance, account_id))
        conn.commit()
        print("Снято", amount, "руб. со счета", account_id)
    else:
        print("Недостаточно средств на счете")

    cursor.close()
    conn.close()

# Функция для показа баланса
def show_balance(account_id):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    balance = cursor.fetchone()[0]
    print("Баланс счета", account_id, "составляет", balance, "руб.")

    cursor.close()
    conn.close()

# Функция для пополнения баланса
def deposit_money(account_id, amount):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Получаем текущий баланс счета
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id,))
    balance = cursor.fetchone()[0]

    # Обновляем баланс счета
    new_balance = balance + amount
    cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s", (new_balance, account_id))
    conn.commit()
    print("Пополнено", amount, "руб. на счет", account_id)

    cursor.close()
    conn.close()

# Пример использования функций
account_id = 1

withdraw_money(account_id, 100)  # Снять 100 руб. со счета
show_balance(account_id)  # Показать баланс
deposit_money(account_id, 50)  # Пополнить счет на 50 руб.
show_balance(account_id)  # Показать обновленный баланс
