#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Альтернативный модуль с импортом через *
(Необязательное задание #5)
"""

from datetime import datetime
# Импортируем все функции из модулей
from application.salary import *
from application.db.people import *


def main():
    """Основная функция с использованием import *"""
    print("=== Программа 'Бухгалтерия' (dirty version) ===")
    print(f"Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("⚠️  Используется импорт через '*' - не рекомендуется в production!")
    print()

    # Используем функции, импортированные через *
    print("Получаем сотрудников через import *...")
    employees = get_employees()
    print()

    print("Рассчитываем зарплату через import *...")
    calculate_salary()
    print()

    # Можем использовать и дополнительные функции
    print("Дополнительные функции:")
    print(f"- {get_salary_report()}")
    print(f"- {update_employee_data()}")
    print()

    print("Dirty main завершен!")


if __name__ == '__main__':
    main()