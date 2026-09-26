from ideas import show_ideas, add_idea

ideas_list = [
    {
        "name": "Трекер привычек",
        "topic": "Консольное приложение",
        "difficult": "Средняя"
    },
    {
        "name": "Космическая викторина",
        "topic": "Игра",
        "difficult": "Легкая"
    },
    {
        "name": "Планировщик задач",
        "topic": "Органайзер времени",
        "difficult": "Средняя"
    }
]

show_ideas(ideas_list)

add = int(input("Добавить новую идею? YES - [1] | NO - [2]: "))
if add == 1:
    name = input('Название: ')
    topic = input('Тема: ')
    difficult = input('Сложность: ')
    add_idea(ideas_list, name, topic, difficult)
    print('Идея добавлена')

show_ideas(ideas_list)
