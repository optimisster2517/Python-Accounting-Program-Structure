#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Основной модуль программы "Бухгалтерия"
"""

from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    """Основная функция программы"""
    print("=== Программа 'Бухгалтерия' ===")
    print(f"Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Получаем список сотрудников
    print("Получаем список сотрудников...")
    employees = get_employees()
    print()

    # Рассчитываем зарплату
    print("Рассчитываем зарплату...")
    calculate_salary()
    print()

    print("Программа завершена успешно!")


if __name__ == '__main__':
    main()