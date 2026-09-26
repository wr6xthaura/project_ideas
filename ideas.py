def show_ideas(ideas):
    print('=== Каталог идей для Python-проектов ===')
    for i, ideas in enumerate(ideas, start=1):
        print(f'{i}. {ideas["name"]}')
        print(f'Тема: {ideas["topic"]}')
        print(f'Сложность: {ideas["difficult"]}')

