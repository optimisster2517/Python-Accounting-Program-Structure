#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пример использования пакета click для создания CLI интерфейса
"""

import click
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


@click.command()
@click.option('--verbose', '-v', is_flag=True, help='Подробный вывод')
@click.option('--employee-id', '-e', type=int, help='ID сотрудника для расчета')
def accounting_cli(verbose, employee_id):
    """
    CLI интерфейс для программы Бухгалтерия

    Пример использования интересного пакета click из PyPI
    """
    click.echo(click.style("=== CLI Бухгалтерия ===", fg='green', bold=True))
    click.echo(f"Запуск: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if verbose:
        click.echo(click.style("Режим подробного вывода включен", fg='yellow'))

    if employee_id:
        click.echo(f"Обработка сотрудника с ID: {employee_id}")

    # Используем наши функции
    with click.progressbar(range(3), label='Загрузка данных') as bar:
        for i in bar:
            if i == 0:
                get_employees()
            elif i == 1:
                calculate_salary()
            else:
                click.echo("Генерация отчетов...")

    click.echo(click.style("✅ Обработка завершена!", fg='green'))


if __name__ == '__main__':
    accounting_cli()