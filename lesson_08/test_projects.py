import requests
from .auth import get_token
from .config import BASE_URL


def test_create_project_positive():
    """Позитивный тест создания проекта."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {"title": "Тестовый проект"}
    url = f"{BASE_URL}/api-v2/projects"
    resp = requests.post(url, json=payload, headers=headers)

    assert resp.status_code == 201, (
        f"Ожидался 201, получен {resp.status_code}"
    )
    data = resp.json()
    assert "id" in data, "В ответе нет поля 'id'"
    assert isinstance(data["id"], str), "ID должен быть строкой"

    print(f"✅ Проект создан с ID: {data['id']}")


def test_create_project_negative_missing_title():
    """Негативный тест: попытка создать проект без поля title."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {}
    url = f"{BASE_URL}/api-v2/projects"
    resp = requests.post(url, json=payload, headers=headers)

    assert resp.status_code in [400, 422], (
        f"Ожидался 400/422, получен {resp.status_code}"
    )
    data = resp.json()
    assert "message" in data or "error" in data, (
        "В ответе нет сообщения об ошибке"
    )
    print("✅ Негативный тест для POST прошёл")


def test_get_project_positive():
    """Позитивный тест: получить созданный проект по ID."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    # 1. Создаём проект
    create_payload = {"title": "Проект для GET"}
    create_resp = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=create_payload,
        headers=headers
    )
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    # 2. Получаем проект по ID
    get_resp = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=headers
    )
    assert get_resp.status_code == 200
    data = get_resp.json()

    # 3. Проверяем, что данные совпадают
    assert data["id"] == project_id
    assert data["title"] == "Проект для GET"
    assert "timestamp" in data
    print(f"✅ Проект {project_id} успешно получен")


def test_get_project_negative_not_found():
    """Негативный тест: получить несуществующий проект."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.get(
        f"{BASE_URL}/api-v2/projects/{fake_id}",
        headers=headers
    )

    assert resp.status_code == 404, (
        f"Ожидался 404, получен {resp.status_code}"
    )
    data = resp.json()
    assert "message" in data or "error" in data, (
        "В ответе нет сообщения об ошибке"
    )
    print("✅ Негативный тест для GET прошёл")


def test_update_project_positive():
    """Позитивный тест: обновить название проекта."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # 1. Создаём проект
    create_payload = {"title": "Старое название"}
    create_resp = requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=create_payload,
        headers=headers
    )
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    # 2. Обновляем название
    update_payload = {"title": "Новое название"}
    update_resp = requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json=update_payload,
        headers=headers
    )
    assert update_resp.status_code == 200, (
        f"Ожидался 200, получен {update_resp.status_code}"
    )
    data = update_resp.json()
    assert data.get("id") == project_id, "ID не совпадает"

    # 3. Проверяем, что изменение применилось (GET)
    get_resp = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=headers
    )
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Новое название"

    print(f"✅ Проект {project_id} обновлён")


def test_update_project_negative_not_found():
    """Негативный тест: обновить несуществующий проект."""
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    fake_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": "Любое название"}
    resp = requests.put(
        f"{BASE_URL}/api-v2/projects/{fake_id}",
        json=payload,
        headers=headers
    )

    assert resp.status_code == 404, (
        f"Ожидался 404, получен {resp.status_code}"
    )
    data = resp.json()
    assert "message" in data or "error" in data, (
        "В ответе нет сообщения об ошибке"
    )
    print("✅ Негативный тест для PUT прошёл")
