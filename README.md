# ВИДЕО -> https://eduiitu-my.sharepoint.com/:f:/g/personal/37614_iitu_edu_kz/IgDmiyPeRURSSKdNuUn8M6uHAdBArJNjsl8E2UnpQ4weiRw?e=G18Pnq

## DevOps — Zholaman Bekbolatov

Учебный проект по DevOps. Простое приложение на Node.js выводит данные студента, запускается в Docker и собирается через Jenkins.

Группа IT2-2314, ID 37614.

### Запуск

Нужен Docker с Compose. Из корня проекта:

```bash
docker compose up -d --build --wait
```

Приложение: http://localhost:37614. Проверка состояния: http://localhost:37614/health.
Остановить: `docker compose down`.

### Тесты

Нужен Node.js 22 или новее:

```bash
npm ci --prefix bekbolatov_zholaman/app
npm test --prefix bekbolatov_zholaman/app
```

### Jenkins

Создай файл `jenkins/secrets/admin_password` со своим паролем, затем запусти:

```bash
docker compose -f jenkins/docker-compose.yml up -d --build
```

Jenkins: http://localhost:18080, логин `zholaman`, пароль из созданного файла.
Задание `Bekbolatov_Zholaman_DevOps` забирает код из GitHub, проверяет приложение, запускает тесты, собирает образ и запускает контейнер.
Перед запуском задания останови приложение через `docker compose down`, чтобы освободить имя контейнера и порт.

В `bekbolatov_zholaman/scripts/` лежит Bash-скрипт для вывода информации о системе Linux.

### Linux и Docker

Linux-часть можно повторить в Ubuntu из корня проекта:

```bash
docker run --rm -v "$PWD/bekbolatov_zholaman:/root/devops/bekbolatov_zholaman" \
  -w /root/devops/bekbolatov_zholaman ubuntu:24.04 bash scripts/linux-demo.sh
```

Скрипт создаёт учебный лог и резервную копию, показывает поиск, права доступа, сведения о системе и процессы.
Файлы `config/app.conf`, `private.txt` и `public.txt` нужны для заданий по Linux.

`bash bekbolatov_zholaman/scripts/verify-docker.sh` проверяет запуск, переменные окружения, stop/start и Compose up/down. Перед этим собери образ через `docker build -t bekbolatov-zholaman-devops .` и освободи контейнер `bekbolatov-zholaman-container`.

[PDF-отчёт](output/pdf/Bekbolatov_Zholaman_DevOps_Report.pdf) · [Скриншоты](docs/screenshots/) · [Результаты проверок](docs/evidence/)

Пароль Jenkins, `.env`, логи, резервные копии и временные файлы остаются локально и не попадают в Git.
