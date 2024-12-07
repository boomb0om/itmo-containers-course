# itmo-containers-course

Практика и лабораторные курса "Контейнеризация и оркестрация" AITH в ИТМО.

## Лабы

- [lab 1](https://github.com/boomb0om/itmo-containers-course/tree/lab1)
- [lab 2](https://github.com/boomb0om/itmo-containers-course/tree/lab2)
- [lab 3](https://github.com/boomb0om/itmo-containers-course/tree/lab3)
- [lab 4](https://github.com/boomb0om/itmo-containers-course/tree/lab4)

## Лаба 4

Развернуть свой собственный сервис в Kubernetes, по аналогии с ЛР 3

Можно использовать Minikube из ЛР 3. Нужно развернуть сервис в связке из минимум 2 контейнеров + 1 init, по аналогии с ЛР 2.

Требования:
- минимум два `Deployment`, по количеству сервисов
- кастомный образ для минимум одного `Deployment` (т.е. не публичный и собранный из своего *Dockerfile*)
- минимум один `Deployment` должен содержать в себе контейнер и инит-контейнер
- минимум один `Deployment` должен содержать `volume` (любой)
- обязательно использование `ConfigMap` и/или `Secret`
- обязательно `Service` хотя бы для одного из сервисов (что логично, если они работают в связке)
- `Liveness` и/или `Readiness` пробы минимум в одном из `Deployment`
- обязательно использование лейблов (помимо обязательных `selector/matchLabel`, конечно)

### Реализация

