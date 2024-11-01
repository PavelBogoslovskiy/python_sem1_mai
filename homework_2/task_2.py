class Buffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        print(f'Добавление данных в буффер {data}')
        if len(self.buffer) >= 5:
            print("Переполнение буфера. Очищаю буфер")
            self.buffer = []

    def get_data(self):
        if len(self.buffer) == 0:
            print("Буфер пуст")
        else:
            print(self.buffer)
            return self.buffer

# Пример
buffer = Buffer()

# Добавление данных
buffer.add_data(1)
buffer.get_data()
buffer.add_data(2)
buffer.get_data()
buffer.add_data([3,324])
buffer.get_data()
buffer.add_data('124')
buffer.get_data()
buffer.add_data(5)
buffer.get_data()