def read_cookbook(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()  # Считываем название блюда
            if not dish_name:
                break  # Если строка пустая, выходим из цикла
            ingredient_count = int(file.readline().strip())  # Считываем количество ингредиентов
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_data = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между блюдами
    return cook_book

# Использование функции
file_name = 'recipes.txt'  # Имя вашего файла
cook_book = read_cookbook(file_name)
print(cook_book)
