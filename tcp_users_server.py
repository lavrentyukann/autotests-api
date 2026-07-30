import socket

def server():
    # Хранилище всех сообщений
    messages = []

    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)

    server_socket.settimeout(1.0)

    print("Сервер запущен и ждет подключений...")

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue

            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            # Получаем сообщение от клиента
            data = client_socket.recv(1024).decode()
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

            # Добавляем сообщение в историю
            messages.append(data)

            # Отправляем клиенту всю историю
            history = '\n'.join(messages)
            client_socket.send(history.encode())

            client_socket.close()

    except KeyboardInterrupt:
        print("Сервер остановлен вручную")

    finally:
        server_socket.close()

# Запуск TCP-сервера: Проверяем, запущен ли файл напрямую. Если да, вызываем server(), и сервер начинает работу.
if __name__ == '__main__':
    server()