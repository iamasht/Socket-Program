import socket


def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the server address and port to bind
    server_address = ('localhost', 12345)  # Change the IP and port as needed

    try:
        # Bind the socket to the specified address and port
        server_socket.bind(server_address)

        # Listen for incoming connections
        server_socket.listen(1)
        print("Server is listening for connections...")

        while True:
            # Accept incoming connection
            connection, client_address = server_socket.accept()
            print("Connection established with:", client_address)

            # Receive data from the client
            data = connection.recv(2048)  # 1024 is the buffer size in bytes
            print("Received data:", data.decode())

            # Process the received data (do your data processing here)
            # ...

            # Send data back to the client
            response = "Data processed successfully!"
            connection.sendall(response.encode())

            # Close the connection with the current client
            connection.close()
            print("Connection closed with:", client_address)

    except socket.error as e:
        print("Socket error:", e)
    except KeyboardInterrupt:
        print("Server interrupted by the user.")
    finally:
        # Close the server socket
        server_socket.close()
        print("Server closed.")


if __name__ == "__main__":
    main()
