from flask import Blueprint, render_template, request, redirect, url_for

lab2 = Blueprint('lab2', __name__)

flowers = [
    {"name": "Роза", "price": 150},
    {"name": "Тюльпан", "price": 90},
    {"name": "Незабудка", "price": 120},
    {"name": "Ромашка", "price": 80}
]

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')
@lab2.route('/lab2/flowers')
def show_flowers():
    return render_template('flowers.html', flowers=flowers)

@lab2.route('/lab2/flowers/add', methods=['POST'])
def add_flower():
    name = request.form.get('name')
    price = request.form.get('price')

    if not name:
        return "Вы не задали имя цветка", 400
    if not price or not price.isdigit():
        return "Цена должна быть числом", 400

    flowers.append({"name": name, "price": int(price)})
    return redirect('/lab2/flowers') 

@lab2.route('/lab2/flowers/delete/<int:flower_id>')
def delete_flower(flower_id):
    if 0 <= flower_id < len(flowers):
        flowers.pop(flower_id)
    return redirect('/lab2/flowers')

@lab2.route('/lab2/flowers/clear')
def clear_flowers():
    flowers.clear()
    return redirect('/lab2/flowers')

@lab2.route('/lab2/example')
def example():
    name = 'Гришти Максим'
    nomer = '2'
    group = 'ФБИ-33'
    kurs = '3 курс'
    lab_num = '2'
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 100}, 
        {'name': 'апельсины', 'price': 100},
        {'name': 'мандарины', 'price': 100}, 
        {'name': 'манго', 'price': 100}
    ]
    return render_template('example.html', name=name, nomer=nomer, kurs=kurs, group=group, lab_num=lab_num, fruits=fruits)

@lab2.route('/lab2/filters')
def filters():
    phrase = "0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filters.html', phrase=phrase)

books = [
        {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 640},
        {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман-эпопея", "pages": 1225},
        {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Роман в стихах", "pages": 320},
        {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 480},
        {"author": "Николай Гоголь", "title": "Мёртвые души", "genre": "Поэма", "pages": 352},
        {"author": "Антон Чехов", "title": "Рассказы", "genre": "Рассказы", "pages": 280},
        {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 288},
        {"author": "Александр Грибоедов", "title": "Горе от ума", "genre": "Комедия", "pages": 160},
        {"author": "Михаил Лермонтов", "title": "Герой нашего времени", "genre": "Роман", "pages": 224},
        {"author": "Александр Островский", "title": "Гроза", "genre": "Драма", "pages": 128},
        {"author": "Иван Гончаров", "title": "Обломов", "genre": "Роман", "pages": 576},
        {"author": "Николай Лесков", "title": "Левша", "genre": "Повесть", "pages": 96},
        {"author": "Фёдор Тютчев", "title": "Стихотворения", "genre": "Поэзия", "pages": 192},
        {"author": "Афанасий Фет", "title": "Вечерние огни", "genre": "Поэзия", "pages": 144},
        {"author": "Владимир Маяковский", "title": "Облако в штанах", "genre": "Поэма", "pages": 112},
        {"author": "Сергей Есенин", "title": "Стихотворения", "genre": "Поэзия", "pages": 256},
        {"author": "Анна Ахматова", "title": "Вечер", "genre": "Поэзия", "pages": 128},
        {"author": "Александр Блок", "title": "Стихи о Прекрасной Даме", "genre": "Поэзия", "pages": 176},
        {"author": "Марина Цветаева", "title": "Версты", "genre": "Поэзия", "pages": 160},
        {"author": "Борис Пастернак", "title": "Доктор Живаго", "genre": "Роман", "pages": 592}
    ]
@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=books)

@lab2.route('/lab2/Furniture')
def show_furniture():
    furniture = [
        {"name": "Диван", "img": "lab2/furniture/sofa.jpg", "desc": "Мягкий трёхместный диван для гостиной"},
        {"name": "Кресло", "img": "lab2/furniture/armchair.jpg", "desc": "Удобное кресло для отдыха"},
        {"name": "Стол", "img": "lab2/furniture/table.jpg", "desc": "Обеденный стол на 6 персон"},
        {"name": "Стул", "img": "lab2/furniture/chair.jpg", "desc": "Классический деревянный стул"},
        {"name": "Кровать", "img": "lab2/furniture/bed.jpg", "desc": "Двуспальная кровать с матрасом"},
        {"name": "Шкаф", "img": "lab2/furniture/wardrobe.jpg", "desc": "Вместительный шкаф-купе"},
        {"name": "Комод", "img": "lab2/furniture/dresser.jpg", "desc": "Комод с выдвижными ящиками"},
        {"name": "Тумба", "img": "lab2/furniture/nightstand.jpg", "desc": "Прикроватная тумба"},
        {"name": "Полка", "img": "lab2/furniture/shelf.jpg", "desc": "Книжная полка"},
        {"name": "Стеллаж", "img": "lab2/furniture/rack.jpg", "desc": "Металлический стеллаж"},
    ]
    return render_template('furniture.html', furniture=furniture)