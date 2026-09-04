from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:новый_пароль@localhost:5432/QA"


def get_next_id(conn):
    """Возвращает следующий доступный customer_id (max + 1)."""
    result = conn.execute(
        text("SELECT COALESCE(MAX(customer_id), 0) + 1 FROM customers")
    )
    return result.scalar()


def test_insert_customer():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        name = "Тестовый клиент"
        new_id = get_next_id(conn)
        sql = text(
            "INSERT INTO customers(customer_id, customer_nm) "
            "VALUES (:id, :name)"
        )
        result = conn.execute(sql, {"id": new_id, "name": name})
        assert result.rowcount == 1

        select_sql = text(
            "SELECT * FROM customers WHERE customer_id = :id"
        )
        rows = conn.execute(select_sql, {"id": new_id}).fetchall()
        assert len(rows) == 1

        conn.execute(
            text("DELETE FROM customers WHERE customer_id = :id"),
            {"id": new_id}
        )


def test_update_customer():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        name = "Обновляемый клиент"
        new_id = get_next_id(conn)
        insert_sql = text(
            "INSERT INTO customers(customer_id, customer_nm) "
            "VALUES (:id, :name)"
        )
        conn.execute(insert_sql, {"id": new_id, "name": name})

        new_name = "Новое имя клиента"
        update_sql = text(
            "UPDATE customers SET customer_nm = :new_name "
            "WHERE customer_id = :id"
        )
        upd_result = conn.execute(
            update_sql, {"new_name": new_name, "id": new_id}
        )
        assert upd_result.rowcount == 1

        select_sql = text(
            "SELECT customer_nm FROM customers WHERE customer_id = :id"
        )
        row = conn.execute(select_sql, {"id": new_id}).fetchone()
        assert row[0] == new_name

        conn.execute(
            text("DELETE FROM customers WHERE customer_id = :id"),
            {"id": new_id}
        )


def test_delete_customer():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        name = "Удаляемый клиент"
        new_id = get_next_id(conn)
        insert_sql = text(
            "INSERT INTO customers(customer_id, customer_nm) "
            "VALUES (:id, :name)"
        )
        conn.execute(insert_sql, {"id": new_id, "name": name})

        delete_sql = text(
            "DELETE FROM customers WHERE customer_id = :id"
        )
        del_result = conn.execute(delete_sql, {"id": new_id})
        assert del_result.rowcount == 1

        select_sql = text(
            "SELECT * FROM customers WHERE customer_id = :id"
        )
        rows = conn.execute(select_sql, {"id": new_id}).fetchall()
        assert len(rows) == 0
