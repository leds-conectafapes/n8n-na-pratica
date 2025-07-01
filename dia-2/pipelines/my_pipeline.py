from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
from pprint import pprint
import requests, json, base64

class Pipeline:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.id = "pipelin_files"
        self.name = "Pipeline"
        self.api_url = "http://host.docker.internal:5678/webhook/webui_pipe_webhook"     
        self.api_key = ""                                    
        self.verify_ssl = True
        self.debug = False
        self.img = ""
        self.texto_extraido = ""
        

    async def on_startup(self):
        # This function is called when the server is started.
        #print(f"on_startup:{__name__}")
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        #print(f"on_shutdown:{__name__}")
        pass

    async def on_valves_updated(self):
        # This function is called when the valves are updated.
        pass

    async def inlet(self, body: dict, user: dict) -> dict:
        # This function is called before the OpenAI API request is made. You can modify the form data before it is sent to the OpenAI API.
        #print(f"inlet:{__name__}")
        
        # Extrai texto de arquivo se disponível
        if (body["messages"][-1]["content"] == "") :
            try:
                print("Entered files to save file")
                self.texto_extraido = body["files"][-1]["file"]["data"]["content"]
                print("File content saved!")
            except (KeyError, IndexError, TypeError) as e:
                print(f"Erro ao acessar conteúdo de arquivos: {e}")
        # Tenta extrair imagem 
        elif(type(body["messages"][-1]["content"]) != str):
            try:
                print("Entered messages")
                self.img = body["messages"][-1]["content"][1]["image_url"]["url"]
                print("Image content saved!")
            except (KeyError, IndexError, TypeError) as e:
                print(f"Erro ao acessar imagem em mensagem: {e}")
                
        

        return body


    async def outlet(self, body: dict, user: dict) -> dict:
        # This function is called after the OpenAI API response is completed. You can modify the messages after they are received from the OpenAI API.
        #print(f"outlet:{__name__}")

        self.texto_extraido = ""
        self.img = ""

        return body

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        # This is where you can add your custom pipelines like RAG.
        
        print(f"pipe: {__name__}")
        
        print("Aqui: ", messages)

        if self.debug:
            print(f"pipe: {__name__} - received message from user: {user_message}")
        
        
        if(messages[-1]["content"] == ""):
            print("File pipe entered!")
            data = {
                "inputs": {"chatInput": self.texto_extraido,
                           "formato": "pdf"}
            }

            
            response = requests.post(
            self.api_url,
            json=data,
            verify=self.verify_ssl
            )

            if response.status_code == 200:
            # Process and yield each chunk from the response
                try:
                    for line in response.iter_lines():
                        if line:
                            # Decode each line assuming UTF-8 encoding and directly parse it as JSON
                            json_data = json.loads(line.decode('utf-8'))
                            # Check if 'output' exists in json_data and yield it
                            if 'isValid' in json_data.keys():
                                yield str(json_data['isValid'])
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON from line. Error: {str(e)}")
                    yield "Error in JSON parsing."
            else:
                yield f"Workflow request failed with status code: {response.status_code}"
        elif(type(messages[-1]["content"]) != str):

            print("Image pipe entered!")
            # Remove o cabeçalho (data:image/jpeg;base64,...) se existir
            header, self.img = self.img.split(',', 1)

            # Decodifica base64 para bytes
            image_bytes = base64.b64decode(self.img)

            # Prepara o arquivo para upload
            files = {
                'image': ('imagem.jpg', image_bytes, 'image/jpeg')  # ou 'image/png' dependendo do formato
            }

            response = requests.post(
            self.api_url,
            files=files,
            verify=self.verify_ssl
            )
            if response.status_code == 200:
            # Process and yield each chunk from the response
                try:
                    for line in response.iter_lines():
                        if line:
                            # Decode each line assuming UTF-8 encoding and directly parse it as JSON
                            json_data = json.loads(line.decode('utf-8'))
                            # Check if 'output' exists in json_data and yield it
                            if 'isValid' in json_data.keys():
                                yield str(json_data['isValid'])
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON from line. Error: {str(e)}")
                    yield "Error in JSON parsing."
            else:
                yield f"Workflow request failed with status code: {response.status_code}"

        else:
            print("Default pipe entered!")
            yield "Ainda não aceitamos mensagens em texto! Só imagens e PDF :)"