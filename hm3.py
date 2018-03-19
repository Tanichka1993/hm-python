import datetime

theatres = [
    {
        'name': 'Національний академічний театр опери та балету України ім. Т. Г. Шевченка',
        'places': 1000,
        'actors': ["Анатолій Кочерга", "Людмила Монастирська", "Володимир Гришко", "Михайло Дідик"],
        'performances': [
            {
                'date': datetime.datetime(day=13, month=3, year=2018),
                'name': 'Фауст',
                'price': 250,
                'actors': ["Володимир Гришко", "Людмила Монастирська"],
                'sold_tickets': 20,
            },
            {
                'date': datetime.datetime(day=14, month=5, year=2018),
                'name': 'Галька',
                'price': 150,
                'actors': ["Анатолій Кочерга", "Людмила Монастирська"],
                'sold_tickets': 50,
            },
            {
                'date': datetime.datetime(day=15, month=5, year=2018),
                'name': 'Травіата',
                'price': 50,
                'actors': ["Володимир Гришко", "Михайло Дідик"],
                'sold_tickets': 80,
            },
            {
                'date': datetime.datetime(day=25, month=6, year=2018),
                'name': 'Казки Гофмана',
                'price': 100,
                'actors': ["Володимир Гришко", "Михайло Дідик"],
                'sold_tickets': 60,
            },
        ]
    },
    {
        'name': 'Львівський національний академічний театр опери та балету',
        'places': 2000,
        'actors': ["Олекса Лупій", "Святослава Коваленко", "Сергій Тарасенко", "Симон Радченко"],
        'performances': [
            {
                'date': datetime.datetime(day=13, month=6, year=2018),
                'name': 'Любов-чарівниця',
                'price': 150,
                'actors': ["Олекса Лупій", "Святослава Коваленко"],
                'sold_tickets': 30,
            },
            {
                'date': datetime.datetime(day=14, month=6, year=2018),
                'name': 'Наталка-Полтавка',
                'price': 300,
                'actors': ["Святослава Коваленко", "Сергій Тарасенко"],
                'sold_tickets': 50,
            },
            {
                'date': datetime.datetime(day=15, month=6, year=2018),
                'name': 'Летюча миша',
                'price': 50,
                'actors': ["Сергій Тарасенко", "Симон Радченко"],
                'sold_tickets': 80,
            },
            {
                'date': datetime.datetime(day=25, month=6, year=2018),
                'name': 'Родимий краю',
                'price': 100,
                'actors': ["Симон Радченко", "Святослава Коваленко"],
                'sold_tickets': 60,
            },
        ]
    }
]


def is_performance_actual(performance):
    return datetime.datetime.now() < performance['date']


is_performance_actual(theatres[0]['performances'][0])

print('Назви всіх вистав: ')
for theatre in theatres:
    for performance in theatre['performances']:
        print(performance['name'], ",",  "актуальна" if is_performance_actual(performance) else "неактуальна")

print('Кількість акторів в першому театрі:', len(theatres[0]['actors']))

theatres[1]['performances'].append({
    'date': datetime.datetime(day=13, month=7, year=2018),
    'name': 'Лісова пісня',
    'price': 90,
    'actors': ["Володимир Монастирський ", "Людмила Гришко"],
    'sold_tickets': 40,
})

print('Play "{name}", availiable tickets num = {money}'.format(name=theatres[0]['performances'][0]['name'], money=(
    theatres[0]['places'] - theatres[0]['performances'][0]['sold_tickets'])))

print('Play “{name}”, profit = {money}'.format(name=theatres[1]['performances'][0]['name'], money=(
    theatres[1]['performances'][0]['price'] * theatres[1]['performances'][0]['sold_tickets'])))

theatres[1]['performances'][1]['sold_tickets'] += 1
print(theatres[1]['performances'][1]['sold_tickets'])
