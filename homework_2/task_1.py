def read_print_digitfile(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if line.isdigit():
                print(line)
            else:
                raise TypeError(f"Найдено нечисловое значение: {line}")
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    except TypeError as e:
        print(e)

# Пример
read_print_digitfile('data.txt')