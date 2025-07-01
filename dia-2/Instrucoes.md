# Como Subir o OpenWebUI e Pipeline com Docker

## 📦 Subir o OpenWebUI

```bash
docker pull ghcr.io/open-webui/open-webui:main

docker run -d \
  -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
````

* A interface ficará disponível em: [http://localhost:3000](http://localhost:3000)

## 🧩 Subir o Pipeline

```bash
docker run -d \
  -p 9099:9099 \
  --add-host=host.docker.internal:host-gateway \
  -v C:\diretório da pasta pipelines \
  --name pipelines \
  --restart always \
  ghcr.io/open-webui/pipelines:main
```

> 📁 Certifique-se de que a pasta `C:..\pipelines` contém os arquivos necessários da pipeline.

---
