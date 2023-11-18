    new_data = cursor.fetchall()
    for row in new_data:
        print(row)
    conn.commit()
