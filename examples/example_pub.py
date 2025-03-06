from dyffi_bus_client.client import DyffiBusClient

client = DyffiBusClient("http://127.0.0.1:8000")

message_id = client.publish_async("orders", {"order_id": 1, "customer": "Alice"})
print("Sent message with ID:", message_id)

message_id = client.publish_async("orders", {"order_id": 2, "customer": "Evelone"})
print("Sent message with ID:", message_id)

message_id = client.publish_async("orders", {"order_id": 3, "customer": "Leron_Baron"})
print("Sent message with ID:", message_id)


message_id = client.publish("myTopic", {"msg_id": 123, "user": "Alice"})
print("Sent message with ID:", message_id)

message_id = client.publish("myTopic", {"msg_id": 246, "user": "Alex"})
print("Sent message with ID:", message_id)

message_id = client.publish("myTopic", {"msg_id": 2145, "user": "Evelone"})
print("Sent message with ID:", message_id)


message_id = client.publish_async("orders", {"order_id": 4, "customer": "Lix"})
print("Sent message with ID:", message_id)

message_id = client.publish_async("orders", {"order_id": 5, "customer": "Skillz"})
print("Sent message with ID:", message_id)

message_id = client.publish_async("orders", {"order_id": 6, "customer": "Alex"})
print("Sent message with ID:", message_id)

message_id = client.publish_async("orders", {"order_id": 7, "customer": "stasik"})
print("Sent message with ID:", message_id)

