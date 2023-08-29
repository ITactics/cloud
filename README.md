# Задание 1: 

## Ansible Плейбук: Настройка SSH и создание пользователя

## Описание

Этот Ansible плейбук предназначен для автоматической настройки `SSH`, создания нового пользователя и отключения входа под пользователем `root` на удаленном хосте. Он использует `vault` для безопасного хранения конфиденциальных данных, таких как пароли и SSH-ключи. Плейбук выполняется для относительно чистого дистрибутива `ОС Ubuntu Server 22.04.3`.

## Задачи

### Include encrypted variables

Эта задача подключает зашифрованные переменные, такие как пароли и SSH-ключи, из файла `secrets.vault`. Они будут использоваться в других задачах для обеспечения безопасности и конфиденциальности.

### Создание нового пользователя

С помощью этой задачи создается новый пользователь `cloudru` на удаленном хосте. Пароль для этого пользователя берется из зашифрованных переменных.

### Include the encrypted SSH public key

Эта задача подключает зашифрованный публичный SSH-ключ пользователя из файла `ssh_keys.vault`. Он будет использоваться для разрешения аутентификации по ключу для пользователя `cloudru`.

### Разрешить аутентификацию на основе ключей SSH для нового пользователя

Задача разрешает аутентификацию на основе ключей `SSH` для нового пользователя `cloudru`. Публичный ключ будет взят из зашифрованных переменных. Это повысит безопасность, так как вход по паролю будет отключен.

### Отключить root-вход по SSH

Эта задача отключает возможность входа под пользователем `root` через SSH, устанавливая опцию PermitRootLogin в значение no в файле `/etc/ssh/sshd_config`. Это повышает безопасность, так как уменьшает возможность атак на удаленный хост. 

### Примечание

В `Ubuntu` по умолчанию вход через `SSH` под пользователем `root` обычно запрещен. Однако, это задание может иметь смысл в контексте повышения безопасности системы дополнительно. Хотя вход по `SSH` под пользователем root запрещен, существуют сценарии, когда взломщик может попытаться подключиться к системе с использованием учетных данных root или попытаться атаковать SSH-сервер исключительно с этим пользователем в качестве цели. Путем явного отключения возможности входа через `SSH` для пользователя `root`, мы создаем дополнительный уровень защиты. 


## Handlers

### Restart SSH

handler перезапускает службу `SSH` (sshd), чтобы внести изменения в конфигурацию `sshd_config` в действие.

## Запуск плейбука

`--ask-vault-pass`: Этот флаг используется для запроса пароля от vault в интерактивном режиме, который используется для расшифровки зашифрованных данных в файле `secrets.vault` и `ssh_keys.vault`.
--become: Этот флаг указывает Ansible использовать привилегии `sudo` или `root` (если это необходимо) при выполнении задач, которые требуют повышения привилегий.
-K: Этот флаг запрашивает пароль для доступа к привилегированным командам (обычно это пароль пользователя sudo).

Для запуска этого плейбука на удаленном хосте, выполните следующую команду:

``` bash
ansible-playbook playbook/configure_ssh_and_user.yaml --ask-vault-pass --become -K
```

# Задание 2: 

## Python Web-приложение с использованием Docker

Этот репозиторий содержит простое веб-приложение на Python, которое использует фреймворк Flask и Docker для контейниризации.

## Как запустить

1. Убедитесь, что у вас установлен Docker на вашей машине.

2. Склонируйте этот репозиторий:

``` bash
git clone https://github.com/ITactics/cloud.git
```

## Собираем Docker-образ:

``` bash
docker build -t simple-web-app .
```

## Запускаем Docker-контейнер:

``` bash
docker run -d -p 8000:8000 --name my-web-app simple-web-app
```

## Откройте веб-браузер и перейдите по адресу `http://localhost:8000`, чтобы увидеть приветственное сообщение.


## Дополнительные эндпоинты

* http://localhost:8000/hostname — Возвращает имя хоста, на котором запущено приложение.
* http://localhost:8000/author — Возвращает имя автора приложения (может быть установлено через переменную окружения).
* http://localhost:8000/id — Возвращает произвольный UUID.

## Зависимости
Для запуска этого приложения потребуется следующее:

* Docker
* Python 3.9
* Flask
