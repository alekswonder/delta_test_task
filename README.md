# Тестовое задание для DELTA:
### Задача:
Сделать небольшую социальную сеть для фотографов.

Есть страны, города, вещи, пользователи. Каждый тип имеет разный набор полей. <br>
Каждая сущность типа может иметь несколько фотографий. <br>
Фотография может быть как одобренная администратором, так и нет.
### Уточнение:
У каждой сущности может быть много фотографий. <br>
Сущности должны быть представлены в моделях. <br>
Сущности не должны дублироваться (город должен быть всегда один). <br>
Менеджер модели должен включать в себя метод получения фото _подчинённых_ моделей (страна включает в себя города, город - вещи, вещи - пользователей)

###### С помощью менеджеров нужно:
1) работать со всеми одобренными фото каждой сущности (получить все фото столов);
2) работать со всеми одобренными фото отдельного типа (получить все фото из Албании - и самой Албании, и столов, и стульев из неё);
3) работать со всеми неодобренными фото (чтобы вывести список для модераторов).

###### Что должно получиться:
Оптимальный набросок models.py django, с моделями и менеджерами, на основе которого будет ПРОЩЕ ВСЕГО развернуть rest api (DRF), которое бы позволило:
1) работать со всеми одобренными фото каждой сущности;
2) работать со всеми одобренные фото отдельного типа;
3) работать со всеми неодобренными фото.
## Установка:
Создать и активировать виртуальное окружение
```
python3 -m venv venv (Linux/macOS) | python -m venv venv (Windows)
```
* Активация для Linux/macOS:
    ```
    source venv/bin/activate
    ```
* Активация для Windows:
    ```
    source venv/Scripts/activate
    ```
#### Обновить pip:
```
python3 -m pip install --upgrade pip (Linux/macOS) | python -m pip install --upgrade pip (Windows)
```
#### Установить зависимости из requirements.txt:
```
pip install -r requirements.txt
```
#### Запустить проект:
```
python3 manage.py runserver (Linux/macOS) | python manage.py runserver (Windows)
```
## Примеры запросов к API:

#### Отобразить все одобренные фото:

###### GET запрос:

```
http://127.0.0.1:8000/api/photos/
```

###### RESPONSE:

```
[
    {
        "title": "string",
        "description": "text",
        "image": "/photos/images/img.jpg",
        "owner": {
            "id": 1,
            "username": "string"
        },
        "city": {
            "id": 1,
            "country": "string",
            "name": "string",
            "slug": "slug",
            "founding_date": "2023-07-23",
            "demonym": "string",
            "ruler": "string",
            "area": int,
            "population": int
        }
    },
    ...
    {
        "title": "string",
        "description": "string",
        "image": "/photos/images/another_img.jpg",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "item": {
            "title": "string",
            "description": "string",
            "owner": {
                "id": 1,
                "username": "admin"
            }
        }
    }
]
```
#### Получить все фото определенной сущности и другие фото, которые относятся к ней и смежным:
_Например получить все фото из Албании - и самой Албании, и столов, и стульев из неё_

###### GET запрос:

```
http://127.0.0.1:8000/api/photos/countries/Россия/
```

###### RESPONSE:

```
[
    {
        "title": "Фото Бразилия",
        "description": "Изображение Бразилия на карте",
        "image": "/photos/images/brasil_on_map.png",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "country": {
            "id": 1,
            "capital": "Бразилиа",
            "name": "Бразилия",
            "slug": "brasil",
            "founding_date": "1882-09-07",
            "demonym": "Бразильцы",
            "ruler": "Луис Инасиу Лула да Силва",
            "area": 8515767,
            "population": 207353391,
            "official_language": "Португальский",
            "government_type": "president_republic",
            "currency": "Бразильский реал"
        }
    },
    {
        "title": "Фото флага Бразилии",
        "description": "Флаг Бразилия",
        "image": "/photos/images/brasil_flag.png",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "country": {
            "id": 1,
            "capital": "Бразилиа",
            "name": "Бразилия",
            "slug": "brasil",
            "founding_date": "1882-09-07",
            "demonym": "Бразильцы",
            "ruler": "Луис Инасиу Лула да Силва",
            "area": 8515767,
            "population": 207353391,
            "official_language": "Португальский",
            "government_type": "president_republic",
            "currency": "Бразильский реал"
        }
    },
    {
        "title": "Фото Бразилии",
        "description": "Фото столицы Бразилии",
        "image": "/photos/images/capital_of_Brasil.jpg",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "city": {
            "id": 1,
            "country": "Бразилия",
            "name": "Бразилиа",
            "slug": "brasilia",
            "founding_date": "1960-04-21",
            "demonym": "Бразильянец",
            "ruler": "Жайме Лернер",
            "area": 5761000,
            "population": 3094325
        }
    },
    {
        "title": "Фото памятника",
        "description": "Фотография какого-то случайного памятника",
        "image": "/photos/images/random_monument.jpg",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "item": {
            "title": "Памятник",
            "description": "Какой-то памятник",
            "owner": {
                "id": 1,
                "username": "admin"
            }
        }
    },
    {
        "title": "Фото пляжа",
        "description": "Фото случайного пляжа",
        "image": "/photos/images/random_beach.jpg",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "item": {
            "title": "Пляж",
            "description": "Какой-то пляж",
            "owner": {
                "id": 1,
                "username": "admin"
            }
        }
    }
]
```
#### Отобразить все неодобренные фото (только для админов/модераторов):

###### GET запрос:

```
http://127.0.0.1:8000/api/photos/unapproved-photos/
```

###### RESPONSE:

```
[
    {
        "title": "string",
        "description": "text",
        "image": "/photos/images/img.jpg",
        "owner": {
            "id": 1,
            "username": "string"
        },
        "city": {
            "id": 1,
            "country": "string",
            "name": "string",
            "slug": "slug",
            "founding_date": "2023-07-23",
            "demonym": "string",
            "ruler": "string",
            "area": int,
            "population": int
        }
    },
    ...
    {
        "title": "string",
        "description": "string",
        "image": "/photos/images/another_img.jpg",
        "owner": {
            "id": 1,
            "username": "admin"
        },
        "item": {
            "title": "string",
            "description": "string",
            "owner": {
                "id": 1,
                "username": "admin"
            }
        }
    }
]
```