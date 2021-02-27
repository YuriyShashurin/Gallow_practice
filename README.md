# Gallow_practice

[![Build Status](https://travis-ci.com/YuriyShashurin/Gallow_practice.svg?branch=master)](https://travis-ci.com/YuriyShashurin/Gallow_practice)

## Игра "Виселица" с тестами для кода с настроенной непрерывной интеграцией с travis-ci

### Как развернуть на локальном устройстве

* склонировать этот репозиторий ```git clone https://github.com/YuriyShashurin/gallow_practice.git```
* перейти в папку с ним ```cd gallow_practice```
* создать виртуальное окружение ```python -m venv venv```
* активировать его ```venv/bin/activate```
* установить зависимости - ```pip install -r requirements.txt```
* запустить приложение, ввести в консоли - ```python gallow.py```
* следовать инструкциям игры в консоли

### Запуск тестовых cлучаев

* установить пакет coverage ```pip install coverage```
* запустить тесты в консоли ```coverage run --include='gallow.py' -m pytest test_cases.py```
* Проверить покрытие кода тестами - ввести в консоли ```coverage report -m```
