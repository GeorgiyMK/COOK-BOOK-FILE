def take_recipes(file_name):
    recipes = {}
    with open(file_name,'r', encoding = 'utf-8') as f:
        key = f.readline()
        recipes[key] = []
        items_count = f.readline()
        for line_number in range(items_count):
            item_line = f.readline()
            sublines = item_line.split('|')
            for subline in sublines:

        f.readline

take_recipes('recipes.txt')


