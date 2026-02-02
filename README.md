# Flask Server with GitHub Auto-Update

Flask сервер в Docker с автоматическим обновлением через GitHub webhooks.

## Запуск

1. Создай `.env` файл:
```
REPO_URL=https://github.com/username/repo.git
```

2. Запусти контейнер:
```bash
docker compose up --build
```

3. Сервер доступен на `http://localhost:5009`

## GitHub Webhook

Настрой webhook в репозитории:

1. GitHub → Settings → Webhooks → Add webhook
2. Payload URL: `http://your-server:5009/webhook`
3. Content type: `application/json`
4. Events: Just the push event

При каждом push файлы в контейнере автоматически синхронизируются с GitHub.


git add .
git commit -m "v0.0.2 - port fixed"
git push


v0.0.1 - Server auto update example 02.02.2026
v0.0.2 - port fixed
