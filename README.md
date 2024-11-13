# itmo-containers-course

Практика и лабораторные курса "Контейнеризация и оркестрация" AITH в ИТМО.

## Лабы

- [lab 1](https://github.com/boomb0om/itmo-containers-course/tree/lab1)
- [lab 2](https://github.com/boomb0om/itmo-containers-course/tree/lab2)
- [lab 3](https://github.com/boomb0om/itmo-containers-course/tree/lab3)
- [lab 4](https://github.com/boomb0om/itmo-containers-course/tree/lab4)

## Лаба 1

### Задание:
- Написать два Dockerfile – плохой и хороший. 
- Написать две плохие практики по использованию контейнеров
- Плохой Dockerfile должен запускаться и работать корректно, но в нём должно быть не менее 3 “bad practices”. В хорошем они должны быть исправлены. В Readme описать все плохие практики из кода Dockerfile и почему они плохие, как они были исправлены в хорошем Dockerfile, а также две плохие практики по использованию этого контейнера. Написать два случая, когда НЕ стоит использовать контейнеры в целом
- Монтирование volume в контейнере - обязательно

### Плохие практики написания Dockerfile

#### Использовать для базового образа тэг `:latest`
- **Почему плохо:** нарушается воспроизводимость, так как новая версия образа может оказаться несовместимой с приложением. Поэтому нужно всегда фиксировать версию (тэг) базового образа
- **Как исправлено:** зафиксирована версия образа `3.12`

#### Использовать "толстые" базовые образы, если есть возможность использовать "тонкие" образы 
- **Почему плохо:** увеличивается размер образа. Если есть возможность, то лучше использовать `slim`, `alpine` или другие версии.
- **Как исправлено:** базовый образ заменен на `python:3.12-slim`

#### Устанавливать лишние зависимости и устанавливать их в разных командах
- **Почему плохо:** при использовании нескольких команд, увеличивается количество слоев и растет размер образа, поэтому лучше их объединять, где есть такая возможность. Команды `apt-get update && apt-get install` нужно выполнять в одну строку, чтобы работало хеширование слоев. Чтобы уменьшить размер образа при использовании Python, можно отключить `cache_dir` в `pip`
- **Как исправлено:** `apt-get update && apt-get install` выполняются вместе. Отключен `cache_dir` в `pip`.

#### Копировать все файлы проекта сразу
- **Почему плохо:** каждый раз, когда вносится изменения в любой из файлов, то сборка будет производится заново.
- **Как исправлено:** сначала копируется файл с зависимостями (`requirements.txt`), а затем ближе к концу файла копируются остальные файлы проекта. 

### Когда не стоит использовать контейнеры

- **Приложения с высокими требованиями к производительности**: если софт или приложение требует высокой эффективности (например, трейдинг и высокочастотная торговля), накладные расходы на виртуализацию могут ухудшить качество работы.
- **Облака и виртуальные машины**: виртуальные машины могут быть более подходящими, если требуется высокая степень изоляции между приложениями и разделение аппаратных ресурсов.

### Запуск

Запустить "плохой" докерфайл:
```bash
docker build -f Dockerfile.bad -t lab1_docker_bad . && docker run -p 8080:8080 -it lab1_docker_bad
```

Запустить "хороший" докерфайл:
```bash
docker build -f Dockerfile.good -t lab1_docker_good . && docker run -p 8080:8080 -it lab1_docker_good
```

Проверить корректность запуска контейнера:
```bash
curl http://0.0.0.0:8080
```