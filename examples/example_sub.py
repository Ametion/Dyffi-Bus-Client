from dyffi_bus_client import DyffiBusClient


def order_handler(message):
    print("Got Message:", message)
    print("Order ID:", message["payload"]["order_id"])


def topic_handler(message):
    print("Got Message:", message)


client = DyffiBusClient("http://127.0.0.1:8000")

client.subscribe("orders", order_handler, blocking=False)

client.subscribe("myTopic", topic_handler, blocking=True)
