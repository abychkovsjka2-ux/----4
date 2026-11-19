"""Задача 3. Пагінація.

Правила: student.md, розділ «Опис задач», задача 3.
Відкриті тести: pytest tests/test_variant_03.py
"""

import requests  # noqa: F401


def collect_all(base_url: str, resource: str, page_size: int = 5, max_pages: int | None = None) -> list:
    """Читає всі сторінки колекції, переходячи за посиланням next."""
    raise NotImplementedError  # TODO: реалізуйте за описом задачі
