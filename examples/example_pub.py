from dyffi_client.client import DyffiClient

client = DyffiClient("http://127.0.0.1:8000")

message_id = client.publish("orders", {"order_id": 123, "customer": "Alice"})
print("Sent message with ID:", message_id)

message_id = client.publish("orders", {"order_id": 345, "customer": "Evelone"})
print("Sent message with ID:", message_id)

message_id = client.publish("orders", {"order_id": 686, "customer": "Leron_Baron"})
print("Sent message with ID:", message_id)



message_id = client.publish("myTopic", {"msg_id": 123, "user": "Alice"})
print("Sent message with ID:", message_id)

message_id = client.publish("myTopic", {"msg_id": 246, "user": "Alex"})
print("Sent message with ID:", message_id)

message_id = client.publish("myTopic", {"msg_id": 2145, "user": "Evelone"})
print("Sent message with ID:", message_id)



message_id = client.publish("orders", {"order_id": 575, "customer": "Lix"})
print("Sent message with ID:", message_id)

message_id = client.publish("orders", {"order_id": 266, "customer": "Skillz"})
print("Sent message with ID:", message_id)

message_id = client.publish("orders", {"order_id": 222, "customer": "Alex"})
print("Sent message with ID:", message_id)

message_id = client.publish("orders", {"order_id": 456, "customer": "stasik"})
print("Sent message with ID:", message_id)

