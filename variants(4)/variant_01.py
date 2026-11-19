import requests


def get_item(base_url: str, resource: str, item_id: int) -> dict | None:
    """Виконує один GET-запит і обробляє коди стану."""
    if isinstance(item_id, bool) or not isinstance(item_id, int) or item_id < 1:
        raise ValueError(f"Некоректний ідентифікатор: {item_id}")

    url = f"{base_url}/api/v1/{resource}/{item_id}"
    headers = {
        "Accept": "application/json",
        "User-Agent": "pp-p05-student",
    }

    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            raise ValueError("Відповідь не є JSON") from None

    if response.status_code == 404:
        return None

    raise RuntimeError(f"Помилка API: {response.status_code}")
