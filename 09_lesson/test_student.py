from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:новый_пароль@localhost:5432/QA"


def get_next_user_id(conn):
    """Возвращает следующий доступный user_id (max + 1)."""
    result = conn.execute(
        text("SELECT COALESCE(MAX(user_id), 0) + 1 FROM student")
    )
    return result.scalar()


def test_insert_student():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        user_id = get_next_user_id(conn)
        level = "beginner"
        education_form = "online"
        subject_id = 1

        sql = text(
            "INSERT INTO student(user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
        )
        result = conn.execute(
            sql,
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id,
            },
        )
        assert result.rowcount == 1

        # Проверяем, что запись появилась
        select_sql = text(
            "SELECT * FROM student WHERE user_id = :user_id"
        )
        rows = conn.execute(select_sql, {"user_id": user_id}).fetchall()
        assert len(rows) == 1
        assert rows[0][1] == level
        assert rows[0][2] == education_form

        # Удаляем
        conn.execute(
            text("DELETE FROM student WHERE user_id = :user_id"),
            {"user_id": user_id},
        )


def test_update_student():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        user_id = get_next_user_id(conn)
        level = "intermediate"
        education_form = "offline"
        subject_id = 1

        insert_sql = text(
            "INSERT INTO student(user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
        )
        conn.execute(
            insert_sql,
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id,
            },
        )

        # Обновляем уровень
        new_level = "advanced"
        update_sql = text(
            "UPDATE student SET level = :new_level "
            "WHERE user_id = :user_id"
        )
        upd_result = conn.execute(
            update_sql, {"new_level": new_level, "user_id": user_id}
        )
        assert upd_result.rowcount == 1

        # Проверяем
        select_sql = text(
            "SELECT level FROM student WHERE user_id = :user_id"
        )
        row = conn.execute(select_sql, {"user_id": user_id}).fetchone()
        assert row[0] == new_level

        # Удаляем
        conn.execute(
            text("DELETE FROM student WHERE user_id = :user_id"),
            {"user_id": user_id},
        )


def test_delete_student():
    engine = create_engine(db_connection_string)
    with engine.begin() as conn:
        user_id = get_next_user_id(conn)
        level = "beginner"
        education_form = "online"
        subject_id = 1

        insert_sql = text(
            "INSERT INTO student(user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
        )
        conn.execute(
            insert_sql,
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id,
            },
        )

        # Удаляем
        delete_sql = text(
            "DELETE FROM student WHERE user_id = :user_id"
        )
        del_result = conn.execute(delete_sql, {"user_id": user_id})
        assert del_result.rowcount == 1

        # Проверяем, что запись исчезла
        select_sql = text(
            "SELECT * FROM student WHERE user_id = :user_id"
        )
        rows = conn.execute(select_sql, {"user_id": user_id}).fetchall()
        assert len(rows) == 0
