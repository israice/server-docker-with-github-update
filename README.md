# Flask Server with GitHub Auto-Update

Flask сервер в Docker с автоматическим обновлением через GitHub webhooks.

## Запуск

1. Создай `.env` файл:
```
REPO_URL=https://github.com/username/repo.git
WEBHOOK_SECRET=your-secret-key-here
PORT=5009
```

2. Запусти контейнер:
```bash
docker compose up --build
```

3. Сервер доступен на `http://localhost:<PORT>`

## GitHub Webhook

Настрой webhook в репозитории:

1. GitHub → Settings → Webhooks → Add webhook
2. Payload URL: `http://your-server:<PORT>/webhook`
3. Content type: `application/json`
4. Secret: тот же ключ что в `.env` (`WEBHOOK_SECRET`)
5. Events: Just the push event

При каждом push файлы в контейнере автоматически синхронизируются с GitHub.

docker compose up -d
docker logs flask-github-updater -f

git add .
git commit -m "v0.0.4 - auto update test 4"
git push


v0.0.1 - Server auto update example 02.02.2026
v0.0.2 - port fixed
v0.0.3 - added WEBHOOK_SECRET
v0.0.4 - auto update test 1

