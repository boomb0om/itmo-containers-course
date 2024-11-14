# itmo-containers-course

Практика и лабораторные курса "Контейнеризация и оркестрация" AITH в ИТМО.

## Лабы

- [lab 1](https://github.com/boomb0om/itmo-containers-course/tree/lab1)
- [lab 2](https://github.com/boomb0om/itmo-containers-course/tree/lab2)
- [lab 3](https://github.com/boomb0om/itmo-containers-course/tree/lab3)
- [lab 4](https://github.com/boomb0om/itmo-containers-course/tree/lab4)

## Лаба 2

На основе `Dockerfile` из ЛР 1 создать композ проект. Обязательные требования:
- минимум 1 init + 2 app сервиса (одноразовый init + приложение + бд или что-то другое, главное чтоб работало в связке)
- автоматическая сборка образа из лежащего рядом `Dockerfile` и присваивание ему (образу) имени
- жесткое именование получившихся контейнеров
- минимум один из сервисов обязательно с `depends_on`
- минимум один из сервисов обязательно с `volume`
- минимум один из сервисов обязательно с прокидыванием порта наружу
- минимум один из сервисов обязательно с ключом `command` и/или `entrypoint` (можно переиспользовать тот же, что в `Dockerfile`)
- добавить `healthcheck`
- все env-ы прописать не в сам docker-compose.yml, а в лежащий рядом файл `.env`
- должна быть явно указана `network` (одна для всех)

**Вопросы**:
- Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему, если да, то как?
- Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?

### Реализация

В качестве БД используется `postgres:13.3`, файлы и `Dockerfile` для миграции к нему находится в папке `migrations/`. В качестве сервиса, который ходит в базу, используется модифицированный сервис из 1 лабы `demo_service/`.

### Запуск

```bash
docker-compose up --build
```

Протестировать работу сервиса (см. логи контейнера с приложением):
```bash
curl http://0.0.0.0:8080
```

### Ответы на вопросы

**Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему, если да, то как?**

Да, в docker-compose.yml можно ограничивать ресурсы для сервисов. Например, можно управлять кол-вом RAM и CPU для каждого контейнера/сервиса.

Для этого нужно указать в `deploy.resources` у сервиса параметры:
- `limits` - для жестких лимитов, то есть максимальных
- `reservations` - для мягких лимитов, то есть сколько у сервиса будет ресурсов минимально

```yaml
services:
  my_service:
    image: example_image
    deploy:
      resources:
        limits:
          memory: 1024M   # "hard limits" на RAM
          cpus: 2         # "hard limits" на CPU
        reservations:
          memory: 256M    # "soft limits" на RAM
          cpus: 0.4       # "soft limits" на CPU
```

**Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?**

Достаточно после `up` написать название сервиса в `docker-compose`. 
```bash
docker compose up <service-name>
```

Например:
```bash
docker compose up db
```