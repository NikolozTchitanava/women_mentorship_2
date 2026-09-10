import socket


SERVER_HOST = "127.0.0.1"  # The computer running udp_server.py
SERVER_PORT = 5001
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print(f"Sending UDP messages to {SERVER_HOST}:{SERVER_PORT}")
    print("Type /quit to end the chat.")

    while True:
        message = input("You: ")
        client_socket.sendto(
            message.encode("utf-8"),
            (SERVER_HOST, SERVER_PORT),
        )

        if message.lower() == "/quit":
            print("Chat ended.")
            break

        data, server_address = client_socket.recvfrom(BUFFER_SIZE)
        reply = data.decode("utf-8")
        print(f"Server {server_address}: {reply}")

        if reply.lower() == "/quit":
            print("Chat ended by the server.")
            break
