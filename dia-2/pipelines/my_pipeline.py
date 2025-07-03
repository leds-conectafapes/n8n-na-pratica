from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
import requests, json

class Pipeline:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.id = "pipeline_webhook_simple"
        self.name = "Simple Webhook Pipeline"
        self.api_url = "http://host.docker.internal:5678/webhook-test/webui_pipe_webhook"
        self.verify_ssl = True

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    async def on_valves_updated(self):
        pass

    async def inlet(self, body: dict, user: dict) -> dict:
        return body

    async def outlet(self, body: dict, user: dict) -> dict:
        return body

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        try:
            # Envia o body completo para o webhook
            response = requests.post(
                self.api_url,
                json=body,
                verify=self.verify_ssl
            )
            
            if response.status_code == 200:
                # Retorna o que o webhook responder
                response_text = response.text.strip()
                
                try:
                    # Tenta parsear como JSON
                    json_response = json.loads(response_text)
                    yield str(json_response)
                except json.JSONDecodeError:
                    # Se não for JSON, retorna o texto bruto
                    yield response_text
            else:
                yield f"Erro: status code {response.status_code}"
                
        except Exception as e:
            yield f"Erro no processamento: {str(e)}"