import socket


def socket_client(batch_data):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the server address and port to connect
    server_address = ('localhost', 12345)  # Change the IP and port to match the server

    try:
        # Connect to the server
        client_socket.connect(server_address)
        print("Connected to the server.")

        # Send data to the server
        data_to_send = "Hello, server!"
        for data in batch_data:
            client_socket.sendall(data.encode())

        # Receive data from the server
        response = client_socket.recv(2048)  # 1024 is the buffer size in bytes
        print("Received response from the server:", response.decode())

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and the correct address is used.")
    except socket.error as e:
        print("Socket error:", e)
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")


