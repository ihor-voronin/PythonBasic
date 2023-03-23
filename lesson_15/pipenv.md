# Pipenv: Python Dev Workflow for Humans
[![pypi version](https://img.shields.io/pypi/v/pipenv.svg)](https://pypi.python.org/pypi/pipenv) [![MIT License](https://img.shields.io/pypi/l/pipenv.svg)](https://pypi.python.org/pypi/pipenv) [![Supported Versions](https://img.shields.io/pypi/pyversions/pipenv.svg)](https://pypi.python.org/pypi/pipenv)

**Pipenv** — це інструмент керування Python virtualenv, який підтримує безліч систем і чудово доповнює прогалини між pip, pyenv і virtualenv. Linux, macOS і Windows є першокласними громадянами pipenv.

Він автоматично створює та керує віртуальним середовищем для ваших проектів, а також додає/видаляє пакунки з вашого `Pipfile`, коли ви встановлюєте/видаляєте пакунки. Він також генерує надзвичайно важливий `Pipfile.lock`, який використовується для створення детермінованих збірок.

Pipenv в першу чергу призначений для того, щоб надати користувачам і розробникам програм простий спосіб налаштування робочого середовища.

Проблеми, які Pipenv прагне вирішити, багатогранні:

- Вам більше не потрібно використовувати `pip` і `virtualenv` окремо. Вони працюють разом.
- Керування файлом `requirements.txt` із хешами пакетів може бути проблематичним. Pipenv використовує `Pipfile` і `Pipfile.lock`, щоб відокремити декларації абстрактних залежностей від останньої перевіреної комбінації.
- Хеші завжди документуються у файлі блокування. Міркування безпеки ставляться на перше місце.
- Наполегливо заохочуйте використання останніх версій залежностей, щоб мінімізувати ризики безпеці [що виникають через застарілі компоненти](https://www.owasp.org/index.php/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities).
- Дає вам уявлення про ваш графік залежностей (наприклад, `$ pipenv graph`).
- Оптимізуйте робочий процес розробки, підтримуючи локальні налаштування за допомогою файлів `.env`.


## Install Pipenv Today!

Рекомендований спосіб інсталяції pipenv на більшості платформ — інсталяція з pypi за допомогою `pip`:

    $ pip install --user pipenv

[Pipfile & Pipfile.lock](https://pipenv.pypa.io/en/latest/pipfile/)

[Pipenv Commands](https://pipenv.pypa.io/en/latest/commands/)