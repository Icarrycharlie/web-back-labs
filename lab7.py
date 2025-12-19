from flask import Blueprint, render_template, request, jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab():
    return render_template('lab7/index.html')

films = [
    {
        "title": "Lock, Stock and Two Smoking Barrels",
        "title_ru": "Карты, деньги, два ствола",
        "year": 1998,
        "description": "Четверо друзей собирают деньги на покерный турнир, но проигрывают крупному мафиози. Чтобы отдать долг, они планируют ограбление своих соседей-наркодилеров."
    },
    {
        "title": "Snatch",
        "title_ru": "Большой куш",
        "year": 2000,
        "description": "Переплетающиеся истории боксера-цыгана, алмазного вора, подпольных боксерских промоутеров и русского гангстера в лондонском криминальном мире."
    },
    {
        "title": "Revolver",
        "title_ru": "Револьвер",
        "year": 2005,
        "description": "Мошенник, только что вышедший из тюрьмы, бросает вызов криминальному боссу, который его посадил, с помощью загадочных незнакомцев."
    },
    {
        "title": "RocknRolla",
        "title_ru": "Рок-н-рольщик",
        "year": 2008,
        "description": "Лондонские гангстеры, русский олигарх, коррумпированный чиновник и пропавшие 7 миллионов фунтов в центре криминальной истории."
    },
    {
        "title": "Sherlock Holmes",
        "title_ru": "Шерлок Холмс",
        "year": 2009,
        "description": "Эксцентричный детектив Шерлок Холмс и его верный помощник доктор Ватсон расследуют серию ритуальных убийств, связанных с черной магией."
    },
    {
        "title": "Sherlock Holmes: A Game of Shadows",
        "title_ru": "Шерлок Холмс: Игра теней",
        "year": 2011,
        "description": "Шерлок Холмс и доктор Ватсон путешествуют по Европе, чтобы остановить профессора Мориарти, планирующего развязать мировую войну."
    },
    {
        "title": "The Man from U.N.C.L.E.",
        "title_ru": "Агенты А.Н.К.Л.",
        "year": 2015,
        "description": "Агент ЦРУ и офицер КГБ вынуждены объединить силы против тайной международной преступной организации в разгар Холодной войны."
    },
    {
        "title": "King Arthur: Legend of the Sword",
        "title_ru": "Меч короля Артура",
        "year": 2017,
        "description": "Молодой Артур, выросший на улицах Лондона, не подозревает о своем королевском происхождении, пока не вытаскивает меч Эскалибур из камня."
    },
    {
        "title": "The Gentlemen",
        "title_ru": "Джентльмены",
        "year": 2019,
        "description": "Американский наркобарон, построивший империю марихуаны в Лондоне, решает продать бизнес, что вызывает войну за влияние в криминальном мире."
    },
    {
        "title": "Operation Fortune: Ruse de Guerre",
        "title_ru": "Операция «Фортуна»: Искусство побеждать",
        "year": 2023,
        "description": "Элитный агент и его команда должны выследить и остановить торговца оружием, продающего смертоносное новое оружие."
    }
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        return '', 404

    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    # Проверка на корректность ID
    if id < 0 or id >= len(films):
        return '', 404
    
    # Удаление фильма
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    films[id] = film
    return films[id]

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    data = request.get_json()
    
    if not data:
        return '', 400
    
    required_fields = ['title', 'title_ru', 'year', 'description']
    for field in required_fields:
        if field not in data:
            return f'Missing required field: {field}', 400
    
    new_film = {
        'title': data['title'],
        'title_ru': data['title_ru'],
        'year': data['year'],
        'description': data['description']
    }
    
    films.append(new_film)
    return str(len(films) - 1), 201