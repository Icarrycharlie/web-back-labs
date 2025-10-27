from flask import Blueprint, render_template, request, make_response, redirect

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)
@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp
@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp
@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните имя!'
    er_age = {}
    age = request.args.get('age')
    if age == '':
        er_age['age'] = 'Заполните возраст!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors, er_age=er_age)
@lab3.route('/lab3/order')
def order():
    return render_template('/lab3/order.html')
@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)
@lab3.route('/lab3/payment')
def payment():
    price = request.args.get('price')
    return render_template('lab3/payment.html', price=price)
@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    if color or bg_color or font_size:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if bg_color:
            resp.set_cookie('bg_color', bg_color)
        if font_size:
            resp.set_cookie('font_size', font_size)
        return resp
    color = request.cookies.get('color', '#000000')
    bg_color = request.cookies.get('bg_color', '#ffffff')
    font_size = request.cookies.get('font_size', '16')
    
    return render_template('lab3/settings.html', 
                         color=color, 
                         bg_color=bg_color, 
                         font_size=font_size)
@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    
    fio = request.args.get('fio')
    shelf = request.args.get('shelf')
    linen = request.args.get('linen') == 'on'
    luggage = request.args.get('luggage') == 'on'
    age_str = request.args.get('age')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    insurance = request.args.get('insurance') == 'on'
    
    form_submitted = any([fio, shelf, age_str, departure, destination, travel_date])
    
    if form_submitted:
        if not fio:
            errors['fio'] = 'Заполните ФИО пассажира'
        if not shelf:
            errors['shelf'] = 'Выберите полку'
        if not age_str:
            errors['age'] = 'Заполните возраст'
        elif not age_str.isdigit() or not (1 <= int(age_str) <= 120):
            errors['age'] = 'Возраст должен быть от 1 до 120 лет'
        if not departure:
            errors['departure'] = 'Заполните пункт выезда'
        if not destination:
            errors['destination'] = 'Заполните пункт назначения'
        if not travel_date:
            errors['travel_date'] = 'Выберите дату поездки'
        
        if errors:
            return render_template('lab3/ticket.html', 
                                 errors=errors,
                                 fio=fio,
                                 shelf=shelf,
                                 linen=linen,
                                 luggage=luggage,
                                 age=age_str,
                                 departure=departure,
                                 destination=destination,
                                 travel_date=travel_date,
                                 insurance=insurance,
                                 show_result=False)
        
        age = int(age_str)
        if age < 18:
            price = 700
        else:
            price = 1000
        
        if shelf in ['lower', 'side_lower']:
            price += 100
        if linen:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150
        
        return render_template('lab3/ticket.html',
                             fio=fio,
                             shelf=shelf,
                             linen=linen,
                             luggage=luggage,
                             age=age,
                             departure=departure,
                             destination=destination,
                             travel_date=travel_date,
                             insurance=insurance,
                             price=price,
                             show_result=True)
    
    return render_template('lab3/ticket.html', show_result=False)
@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('bg_color') 
    resp.delete_cookie('font_size')
    return resp
books = [
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "price": 450, "year": 1967, "genre": "Роман", "pages": 480},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "price": 380, "year": 1866, "genre": "Роман", "pages": 672},
    {"title": "Война и мир", "author": "Лев Толстой", "price": 890, "year": 1869, "genre": "Роман-эпопея", "pages": 1225},
    {"title": "Анна Каренина", "author": "Лев Толстой", "price": 520, "year": 1877, "genre": "Роман", "pages": 864},
    {"title": "Евгений Онегин", "author": "Александр Пушкин", "price": 290, "year": 1833, "genre": "Роман в стихах", "pages": 288},
    {"title": "Мёртвые души", "author": "Николай Гоголь", "price": 410, "year": 1842, "genre": "Поэма", "pages": 352},
    {"title": "Отцы и дети", "author": "Иван Тургенев", "price": 320, "year": 1862, "genre": "Роман", "pages": 288},
    {"title": "Герой нашего времени", "author": "Михаил Лермонтов", "price": 350, "year": 1840, "genre": "Роман", "pages": 224},
    {"title": "Идиот", "author": "Фёдор Достоевский", "price": 480, "year": 1869, "genre": "Роман", "pages": 640},
    {"title": "Братья Карамазовы", "author": "Фёдор Достоевский", "price": 560, "year": 1880, "genre": "Роман", "pages": 824},
    {"title": "Обломов", "author": "Иван Гончаров", "price": 390, "year": 1859, "genre": "Роман", "pages": 576},
    {"title": "Доктор Живаго", "author": "Борис Пастернак", "price": 430, "year": 1957, "genre": "Роман", "pages": 592},
    {"title": "Тихий Дон", "author": "Михаил Шолохов", "price": 680, "year": 1940, "genre": "Роман-эпопея", "pages": 1504},
    {"title": "Петр Первый", "author": "Алексей Толстой", "price": 510, "year": 1945, "genre": "Исторический роман", "pages": 768},
    {"title": "Двенадцать стульев", "author": "Ильф и Петров", "price": 370, "year": 1928, "genre": "Юмористический роман", "pages": 416},
    {"title": "Золотой теленок", "author": "Ильф и Петров", "price": 360, "year": 1931, "genre": "Юмористический роман", "pages": 384},
    {"title": "Мы", "author": "Евгений Замятин", "price": 310, "year": 1924, "genre": "Антиутопия", "pages": 320},
    {"title": "Лолита", "author": "Владимир Набоков", "price": 440, "year": 1955, "genre": "Роман", "pages": 448},
    {"title": "1984", "author": "Джордж Оруэлл", "price": 390, "year": 1949, "genre": "Антиутопия", "pages": 328},
    {"title": "Скотный двор", "author": "Джордж Оруэлл", "price": 280, "year": 1945, "genre": "Сатира", "pages": 144},
    {"title": "Улисс", "author": "Джеймс Джойс", "price": 620, "year": 1922, "genre": "Модернизм", "pages": 832},
    {"title": "Великий Гэтсби", "author": "Фрэнсис Скотт Фицджеральд", "price": 330, "year": 1925, "genre": "Роман", "pages": 218},
    {"title": "Над пропастью во ржи", "author": "Джером Сэлинджер", "price": 340, "year": 1951, "genre": "Роман", "pages": 277},
    {"title": "Сто лет одиночества", "author": "Габриэль Гарсиа Маркес", "price": 470, "year": 1967, "genre": "Магический реализм", "pages": 448},
    {"title": "Портрет Дориана Грея", "author": "Оскар Уайльд", "price": 300, "year": 1890, "genre": "Философский роман", "pages": 254}
]

@lab3.route('/lab3/books')
def books_search():
    min_price_cookie = request.cookies.get('min_price', '')
    max_price_cookie = request.cookies.get('max_price', '')
    
    min_price_arg = request.args.get('min_price', min_price_cookie)
    max_price_arg = request.args.get('max_price', max_price_cookie)
    reset = request.args.get('reset')
    
    if reset:
        resp = make_response(redirect('/lab3/books'))
        resp.delete_cookie('min_price')
        resp.delete_cookie('max_price')
        return resp
    
    min_price_all = min(book['price'] for book in books)
    max_price_all = max(book['price'] for book in books)
    
    filtered_books = books
    message = ""
    
    if min_price_arg or max_price_arg:
        try:
            min_price = int(min_price_arg) if min_price_arg else min_price_all
            max_price = int(max_price_arg) if max_price_arg else max_price_all
            
            if min_price > max_price:
                min_price, max_price = max_price, min_price
            
            filtered_books = [
                book for book in books
                if min_price <= book['price'] <= max_price
            ]
            
            count = len(filtered_books)
            if count == 0:
                message = "Не найдено ни одной книги в заданном диапазоне цен"
            else:
                message = f"Найдено книг: {count}"
                
            if min_price_arg or max_price_arg:
                resp = make_response(render_template('lab3/books.html',
                    books=filtered_books,
                    min_price=min_price,
                    max_price=max_price,
                    min_price_all=min_price_all,
                    max_price_all=max_price_all,
                    message=message
                ))
                if min_price_arg:
                    resp.set_cookie('min_price', min_price_arg)
                if max_price_arg:
                    resp.set_cookie('max_price', max_price_arg)
                return resp
                
        except ValueError:
            message = "Ошибка: введите корректные числовые значения"
    
    return render_template('lab3/books.html',
        books=filtered_books,
        min_price=min_price_arg,
        max_price=max_price_arg,
        min_price_all=min_price_all,
        max_price_all=max_price_all,
        message=message or f"Всего книг: {len(filtered_books)}"
    )