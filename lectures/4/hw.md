# Домашняя работа 3

(HW3_3)=
## Задание 0. Система учёта оценок студентов

**Структура данных:**
```python
students = [
    {'name': 'Анна', 'grades': [4, 5, 4], 'group': 'ФИЗ-101'},
    # ...
]
```

**Функции:**
1. `add_student(name, group)` — добавляет нового студента (список оценок пустой).
2. `add_grade(name, grade)` — добавляет оценку студенту по имени.
3. `average_grade_by_group(group)` — возвращает средний балл по группе.
4. `remove_student(name)` — удаляет студента из списка по имени.

---

(HW3_1)=
## Задание 1. Учёт книг в домашней библиотеке

**Структура данных:**
```python
books = [
    {'title': 'Война и мир', 'author': 'Л.Н. Толстой', 'year': 1869, 'read': True},
    # ...
]
```

**Функции:**
1. `add_book(title, author, year)` — добавляет новую книгу в список (по умолчанию `read=False`).
2. `mark_as_read(title)` — меняет статус книги на «прочитана» (`read=True`).
3. `get_unread_books()` — возвращает список названий непрочитанных книг.
4. `remove_book(title)` — удаляет книгу из списка по названию.

---
(HW3_2)=
## Задание 2. Планирование бюджета на месяц

**Структура данных:**
``` python
expenses = [
    {'category': 'продукты', 'amount': 1500, 'date': '2023-10-01'},
    # ...
]
```

**Функции:**
1. `add_expense(category, amount, date)` — добавляет новый расход в список.
2. `total_by_category(category)` — возвращает общую сумму расходов по категории.
3. `filter_by_date(start_date, end_date)` — возвращает список расходов за указанный период.
4. `delete_expense_by_id(index)` — удаляет расход по его индексу в списке.

---

(HW3_4)=
## Задание 3. Трекер привычек

**Структура данных:**
```python
habits = [
    {'name': 'зарядка', 'frequency': 5, 'completed_days': ['2023-10-01', '2023-10-02']},
    # ...
]
```

**Функции:**
1. `add_habit(name, frequency)` — добавляет привычку (сколько дней в неделю планируется выполнять).
2. `complete_habit(name, date)` — добавляет дату в `completed_days` для привычки.
3. `habit_progress()` — возвращает словарь `{название: процент выполнения}` (сколько дней выполнено / сколько запланировано).
4. `delete_habit(name)` — удаляет привычку по названию.

---
(HW3_5)=
## Задание 4. Список фильмов для просмотра

**Структура данных:**
```python
movies = [
    {'title': 'Интерстеллар', 'year': 2014, 'genre': 'фантастика', 'watched': False},
    # ...
]
```

**Функции:**
1. `add_movie(title, year, genre)` — добавляет фильм (по умолчанию `watched=False`).
2. `mark_watched(title)` — меняет `watched` на `True`.
3. `filter_by_genre(genre)` — возвращает список названий фильмов заданного жанра.
4. `remove_movie(title)` — удаляет фильм по названию.

---
(HW3_6)=
## Задание 5. Планирование тренировок

**Структура данных:**
```python
workouts = [
    {'type': 'бег', 'duration': 30, 'date': '2023-10-01', 'intensity': 'средняя'},
    # ...
]
```

**Функции:**
1. `add_workout(type, duration, date, intensity)` — добавляет тренировку.
2. `total_duration_by_type(type)` — возвращает суммарную длительность тренировок типа.
3. `last_workouts(n)` — возвращает последние `n` тренировок (последние элементы списка).
4. `delete_workout_by_date(date)` — удаляет все тренировки за указанную дату.

---
(HW3_7)=
## Задание 6. Учёт расходов в поездке

**Структура данных:**
```python
trip_expenses = [
    {'category': 'жильё', 'amount': 3000, 'city': 'Москва', 'date': '2023-10-01'},
    # ...
]
```

**Функции:**
1. `add_trip_expense(category, amount, city, date)` — добавляет расход.
2. `total_by_city(city)` — возвращает общие расходы в городе.
3. `most_expensive_day()` — возвращает дату и сумму самого дорогого дня поездки.
4. `clear_city_expenses(city)` — удаляет все расходы по указанному городу.

---
(HW3_8)=
## Задание 7. Дневник питания

**Структура данных:**
```python
food_log = [
    {'item': 'яблоко', 'calories': 95, 'date': '2023-10-01', 'meal': 'перекус'},
    # ...
]
```

**Функции:**
1. `add_food(item, calories, date, meal)` — добавляет продукт в дневник.
2. `daily_calories(date)` — считает калории за день.
3. `top_calorie_items(n)` — возвращает топ‑`n` самых калорийных продуктов.
4. `remove_meal_by_date_and_meal(date, meal)` — удаляет приём пищи по дате и типу (завтрак, обед и т. д.).

---
(HW3_9)=
## Задание 8. Учёт задач проекта

**Структура данных:**
```python
tasks = [
    {'name': 'написать код', 'priority': 'высокий', 'status': 'в работе', 'deadline': '2023-10-15'},
    # ...
]
```

**Функции:**
1. `add_task(name, priority, deadline)` — добавляет задачу (по умолчанию `status='планируется'`).
2. `update_status(name, status)` — меняет статус задачи.
3. `overdue_tasks()` — возвращает список задач с просроченным дедлайном.
4. `delete_completed_tasks()` — удаляет все задачи со статусом `status='завершена'`.

---
(HW3_10)=
## Задание 9. Каталог книг в библиотеке

**Структура данных:**
```python
library = [
    {'title': 'Мастер и Маргарита', 'author': 'М.А. Булгаков', 'year': 1966, 'available': True},
    # ...
]
```

**Функции:**
1. `add_book_to_library(title, author, year)` — добавляет книгу (по умолчанию `available=True`).
2. `borrow_book(title)` — меняет `available` на `False`.
3. `oldest_books(n)` — возвращает топ‑`n` самых старых книг.
4. `remove_missing_books()` — удаляет книги, которых нет в наличии более года (можно добавить поле `borrow_date` для усложнения).

(HW3_11)=
## Задание 10. Учёт сотрудников компании

**Структура данных:**
```python
employees = [
    {'name': 'Иван Петров', 'position': 'разработчик', 'salary': 80000, 'department': 'IT'},
    # ...
]
```

**Функции:**
1. `add_employee(name, position, salary, department)` — добавляет нового сотрудника.
2. `raise_salary(name, percent)` — увеличивает зарплату сотрудника на указанный процент.
3. `avg_salary_by_department(department)` — возвращает среднюю зарплату по отделу.
4. `fire_employee(name)` — удаляет сотрудника из списка по имени.

---
(HW3_12)=
## Задание 11. Каталог автомобилей

**Структура данных:**
```python
cars = [
    {'brand': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 2500000},
    # ...
]
```

**Функции:**
1. `add_car(brand, model, year, price)` — добавляет автомобиль в каталог.
2. `apply_discount(brand, percent)` — применяет скидку к цене всех автомобилей указанной марки.
3. `find_cheapest_by_year(year)` — возвращает самый дешёвый автомобиль заданного года выпуска.
4. `remove_discontinued(brand, model)` — удаляет автомобиль по марке и модели.

---
(HW3_13)=
## Задание 12. Журнал погоды

**Структура данных:**
```python
weather_log = [
    {'date': '2023-10-01', 'temp': 15, 'rainfall': 0.5, 'wind_speed': 3},
    # ...
]
```

**Функции:**
1. `record_weather(date, temp, rainfall, wind_speed)` — записывает данные о погоде за день.
2. `avg_temperature(start_date, end_date)` — рассчитывает среднюю температуру за период.
3. `rainy_days(threshold)` — возвращает список дат, когда осадков было больше указанного порога.
4. `delete_old_records(days)` — удаляет записи старше указанного количества дней.

---
(HW3_14)=
## Задание 13. Список рецептов

**Структура данных:**
```python
recipes = [
    {'name': 'Борщ', 'ingredients': ['свёкла', 'картофель'], 'time': 60, 'difficulty': 'средняя'},
    # ...
]
```

**Функции:**
1. `add_recipe(name, ingredients, time, difficulty)` — добавляет новый рецепт.
2. `update_difficulty(name, new_difficulty)` — меняет уровень сложности рецепта.
3. `quick_recipes(max_time)` — возвращает рецепты, готовящиеся не дольше указанного времени.
4. `remove_recipe(name)` — удаляет рецепт по названию.

---
(HW3_15)=
## Задание 14. Учёт задач на день

**Структура данных:**
```python
tasks = [
    {'title': 'Купить продукты', 'priority': 'высокий', 'completed': False, 'category': 'быт'},
    # ...
]
```

**Функции:**
1. `add_task(title, priority, category)` — добавляет задачу (по умолчанию `completed=False`).
2. `complete_task(title)` — отмечает задачу как выполненную.
3. `urgent_tasks()` — возвращает список задач с приоритетом «высокий».
4. `clear_completed()` — удаляет все выполненные задачи.

---
(HW3_16)=
## Задание 15. Каталог музыки

**Структура данных:**
```python
music_catalog = [
    {'artist': 'Queen', 'title': 'Bohemian Rhapsody', 'genre': 'rock', 'duration': 355},
    # ...
]
```

**Функции:**
1. `add_track(artist, title, genre, duration)` — добавляет трек в каталог.
2. `change_genre(artist, title, new_genre)` — меняет жанр трека.
3. `longest_tracks(n)` — возвращает топ‑`n` самых длинных треков.
4. `remove_artist_tracks(artist)` — удаляет все треки указанного исполнителя.

---
(HW3_17)=
## Задание 16. Журнал тренировок

**Структура данных:**
```python
workout_journal = [
    {'date': '2023-10-01', 'exercise': 'приседания', 'reps': 20, 'sets': 3, 'weight': 50},
    # ...
]
```

**Функции:**
1. `log_workout(date, exercise, reps, sets, weight)` — записывает тренировку.
2. `total_reps_by_exercise(exercise)` — считает суммарное количество повторений для упражнения.
3. `best_weight_by_exercise(exercise)` — возвращает максимальный вес, использованный для упражнения.
4. `delete_workout_by_date(date)` — удаляет все записи за указанную дату.

---
(HW3_18)=
## Задание 17. Учёт подписок

**Структура данных:**
```python
subscriptions = [
    {'service': 'Netflix', 'cost': 799, 'renewal_date': '2023-11-01', 'active': True},
    # ...
]
```

**Функции:**
1. `add_subscription(service, cost, renewal_date)` — добавляет подписку (по умолчанию `active=True`).
2. `renew_subscription(service)` — обновляет дату продления подписки на следующий месяц.
3. `monthly_cost()` — рассчитывает общую стоимость активных подписок за месяц.
4. `cancel_subscription(service)` — отменяет подписку (`active=False`).

---
(HW3_19)=
## Задание 18. Список мест для посещения

**Структура данных:**
```python
places_to_visit = [
    {'name': 'Эйфелева башня', 'city': 'Париж', 'country': 'Франция', 'visited': False},
    # ...
]
```

**Функции:**
1. `add_place(name, city, country)` — добавляет место (по умолчанию `visited=False`).
2. `mark_visited(name)` — отмечает место как посещённое.
3. `places_by_country(country)` — возвращает список мест в указанной стране.
4. `remove_place(name)` — удаляет место по названию.

---
(HW3_20)=
## Задание 19. Учёт расходов на транспорт

**Структура данных:**
```python
transport_expenses = [
    {'type': 'автобус', 'cost': 60, 'date': '2023-10-01', 'passenger_count': 1},
    # ...
]
```

**Функции:**
1. `add_transport_expense(type, cost, passenger_count)` — добавляет расход на транспорт.
2. `total_by_type(type)` — считает общие расходы по типу транспорта.
3. `most_expensive_trip()` — возвращает самую дорогую поездку.
4. `delete_expenses_by_date(date)` — удаляет расходы за указанную дату.

---
(HW3_21)=
## Задание 20. Список целей на год

**Структура данных:**
```python
goals = [
    {'name': 'Выучить Python', 'target': 'свободно программировать', 'progress': 30, 'deadline': '2024-12-31'},
    # ...
]
```

**Функции:**
1. `add_goal(name, target, deadline)` — добавляет цель (по умолчанию `progress=0`).
2. `update_progress(name, new_progress)` — обновляет прогресс цели.
3. `achieved_goals()` — возвращает список целей с прогрессом 100 %.
4. `delete_overdue_goals()` — удаляет цели, срок которых истёк, а прогресс < 100 %.

---
(HW3_22)=
## Задание 21. Каталог фильмов

**Структура данных:**
```python
movie_catalog = [
    {'title': 'Интерстеллар', 'director': 'Кристофер Нолан', 'year': 2014, 'rating': 8.6},
    # ...
]
```

**Функции:**
1. `add_movie(title, director, year, rating)` — добавляет фильм в каталог.
2. `update_rating(title, new_rating)` — меняет рейтинг фильма.
3. `top_rated_movies(n)` — возвращает топ‑`n` фильмов с наивысшим рейтингом.
4. `remove_movie_by_year(year)` — удаляет фильмы заданного года выпуска.

---
(HW3_23)=
## Задание 22. Учёт домашних животных

**Структура данных:**
```python
pets = [
    {'name': 'Барсик', 'species': 'кошка', 'age': 3, 'owner': 'Анна Иванова'},
    # ...
]
```

**Функции:**
1. `add_pet(name, species, age, owner)` — добавляет нового питомца в список.
2. `update_age(name, new_age)` — обновляет возраст питомца.
3. `pets_by_owner(owner)` — возвращает список питомцев указанного владельца.
4. `remove_pet(name)` — удаляет питомца из списка по имени.

---
(HW3_24)=
## Задание 23. Каталог растений

**Структура данных:**
```python
plants = [
    {'name': 'Фиалка', 'type': 'цветущее', 'watering_freq': 7, 'sunlight': 'рассеянный'},
    # ...
]
```

**Функции:**
1. `add_plant(name, type, watering_freq, sunlight)` — добавляет растение в каталог.
2. `change_watering_freq(name, new_freq)` — меняет частоту полива для растения.
3. `shade_loving_plants()` — возвращает список растений, предпочитающих тень/рассеянный свет.
4. `remove_plant(name)` — удаляет растение по названию.

---
(HW3_25)=
## Задание 24. Учёт оборудования в лаборатории

**Структура данных:**
```python
equipment = [
    {'name': 'Микроскоп', 'type': 'оптический', 'status': 'исправен', 'last_calibration': '2023-09-01'},
    # ...
]
```

**Функции:**
1. `add_equipment(name, type, status, last_calibration)` — добавляет оборудование в список.
2. `mark_maintenance(name)` — меняет статус на «в обслуживании».
3. `overdue_calibrations()` — возвращает список оборудования, требующего калибровки (если прошло > 365 дней).
4. `retire_equipment(name)` — удаляет оборудование из списка.

---
(HW3_26)=
## Задание 25. Список контактов

**Структура данных:**
```python
contacts = [
    {'name': 'Мария Сидорова', 'phone': '+79161234567', 'email': 'maria@mail.ru', 'category': 'работа'},
    # ...
]
```

**Функции:**
1. `add_contact(name, phone, email, category)` — добавляет новый контакт.
2. `update_phone(name, new_phone)` — обновляет номер телефона контакта.
3. `contacts_by_category(category)` — возвращает контакты заданной категории.
4. `delete_contact(name)` — удаляет контакт по имени.

---
(HW3_27)=
## Задание 26. Журнал успеваемости студентов

**Структура данных:**
```python
grades_journal = [
    {'student': 'Иван Петров', 'subject': 'Физика', 'grade': 5, 'date': '2023-10-05'},
    # ...
]
```

**Функции:**
1. `add_grade(student, subject, grade, date)` — добавляет оценку в журнал.
2. `avg_grade_by_student(student)` — рассчитывает средний балл студента.
3. `failing_students(subject, threshold)` — возвращает студентов с оценками ниже порога по предмету.
4. `clear_old_grades(days)` — удаляет оценки старше указанного количества дней.

---
(HW3_28)=
## Задание 27. Каталог книг в библиотеке

**Структура данных:**
```python
library_catalog = [
    {'title': 'Война и мир', 'author': 'Л.Н. Толстой', 'year': 1869, 'available': True},
    # ...
]
```

**Функции:**
1. `add_book(title, author, year)` — добавляет книгу (по умолчанию `available=True`).
2. `borrow_book(title)` — меняет статус `available` на `False`.
3. `books_by_author(author)` — возвращает книги указанного автора.
4. `remove_lost_books()` — удаляет книги со статусом `available=False` более 365 дней.

---
(HW3_29)=
## Задание 28. Учёт заказов в кафе

**Структура данных:**
```python
orders = [
    {'table': 5, 'items': ['кофе', 'круассан'], 'total': 450, 'status': 'в работе'},
    # ...
]
```

**Функции:**
1. `add_order(table, items, total)` — добавляет заказ (по умолчанию `status='в работе'`).
2. `complete_order(table)` — меняет статус заказа на «выполнен».
3. `revenue_today()` — считает общую выручку за день (можно добавить поле `date`).
4. `cancel_order(table)` — отменяет заказ и удаляет его из списка.

---
(HW3_30)=
## Задание 29. Список задач для волонтёров

**Структура данных:**
```python
volunteer_tasks = [
    {'task': 'Раздача еды', 'volunteer': 'Алексей', 'date': '2023-10-15', 'completed': False},
    # ...
]
```

**Функции:**
1. `assign_task(task, volunteer, date)` — назначает задачу волонтёру (по умолчанию `completed=False`).
2. `mark_completed(task)` — отмечает задачу как выполненную.
3. `tasks_by_volunteer(volunteer)` — возвращает задачи указанного волонтёра.
4. `remove_expired_tasks(date)` — удаляет задачи с датой раньше указанной.

---
(HW3_31)=
## Задание 30. Каталог фильмов для стриминга

**Структура данных:**
```python
streaming_catalog = [
    {'title': 'Интерстеллар', 'genre': 'фантастика', 'duration': 169, 'watched': 1250},
    # ...
]
```

**Функции:**
1. `add_movie_to_catalog(title, genre, duration)` — добавляет фильм (по умолчанию `watched=0`).
2. `increment_watches(title)` — увеличивает счётчик просмотров на 1.
3. `most_watched_movies(n)` — возвращает топ‑`n` самых просматриваемых фильмов.
4. `remove_movie(title)` — удаляет фильм из каталога.

---
(HW3_32)=
## Задание 31. Учёт инвентаря спортивного зала

**Структура данных:**
```python
gym_inventory = [
    {'item': 'гантели', 'quantity': 10, 'condition': 'хорошее', 'location': 'зал №1'},
    # ...
]
```

**Функции:**
1. `add_item(item, quantity, condition, location)` — добавляет инвентарь в список.
2. `update_quantity(item, new_quantity)` — обновляет количество предметов.
3. `low_stock_items(threshold)` — возвращает инвентарь с количеством ниже порога.
4. `dispose_item(item)` — удаляет предмет из инвентаря.

