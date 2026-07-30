import socket

def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 5 в очереди)
    server_socket.listen(5)

    server_socket.settimeout(1.0)

    print("Сервер запущен и ждет подключений...")

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue

            print(f"Подключение от {client_address}")

            data = client_socket.recv(1024).decode()
            print(f"Получено сообщение: {data}")

            response = f"Сервер получил: {data}"
            client_socket.send(response.encode())

            client_socket.close()

    except KeyboardInterrupt:
        print("Сервер остановлен")

    finally:
        server_socket.close()

# Запуск TCP-сервера: Проверяем, запущен ли файл напрямую. Если да, вызываем server(), и сервер начинает работу.
if __name__ == '__main__':
    server()