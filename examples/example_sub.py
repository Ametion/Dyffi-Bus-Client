from client import DyffiClient


def order_handler(message):
    print("Got Message:", message)
    print("Order ID:", message["payload"]["order_id"])


def topic_handler(message):
    print("Got Message:", message)


client = DyffiClient("http://127.0.0.1:8000")

client.subscribe("orders", order_handler, blocking=False)

client.subscribe("myTopic", topic_handler, blocking=True)
