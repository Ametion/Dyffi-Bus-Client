import requests
import json
import threading
from websocket import create_connection, WebSocketConnectionClosedException
import time


class DyffiClient:
    """
    Клиентская библиотека для работы с вашим pub/sub сервисом.
    Полностью скрывает детали работы с HTTP и WebSocket.
    """

    def __init__(self, api_url):
        """
        :param api_url: Базовый URL API вашего сервиса, например, "http://localhost:8000"
        """
        self.api_url = api_url.rstrip('/')

    def publish(self, topic, payload):
        """
        Публикует сообщение в указанный топик через REST API.
        """
        url = f"{self.api_url}/publish"
        data = {"topic": topic, "payload": payload}
        print(url)
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("message_id")

    def subscribe(self, topic, handler, blocking=False):
        """
        Подписывается на топик. Если blocking=True, вызывается блокирующий цикл для прослушивания.
        Если blocking=False, запускается в отдельном потоке.
        """
        if blocking:
            self._subscribe_thread(topic, handler)
        else:
            thread = threading.Thread(target=self._subscribe_thread, args=(topic, handler), daemon=True)
            thread.start()

    def _subscribe_thread(self, topic, handler):
        """
        Внутренняя функция для установления WebSocket-соединения и прослушивания сообщений.
        """
        ws_url = self.api_url.replace("http", "ws") + f"/ws/{topic}"
        try:
            ws = create_connection(ws_url)
            while True:
                message_json = ws.recv()
                message = json.loads(message_json)
                handler(message)
        except WebSocketConnectionClosedException:
            print("WebSocket соединение закрыто.")
        except Exception as e:
            print(f"Ошибка в подписке: {e}")

    def listen(self):
        """
        Простой блокирующий цикл, чтобы основной поток не завершался.
        """
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Выход из прослушивания.")
