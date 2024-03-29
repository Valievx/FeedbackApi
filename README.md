# FeedbackApi
## О проекте
Проект ReviewRadar собирает отзывы пользователей на произведения. 
Сами произведения в ReviewRadar не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, 
в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», 
а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. 

Список категорий может быть расширен 
(например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 

Произведению может быть присвоен жанр из списка предустановленных 
(например, «Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы 
и ставят произведению оценку в диапазоне от одного до десяти (целое число); 
из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число).
На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

## Стек
* Django Rest Framework
* Simple JWT 
* SQLite 
* Git 
* Postman

## Как развернуть проект

* Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Valievx/FeedbackApi.git
```

* Создать и активировать виртуальную среду, установить зависимости
```bash
python -m venv venv
Win: source venv/bin/activate
Unix: source venv/Scripts/activate
pip install -r requirements.txt
```

* Перейти в директорию проекта
```bash
cd api_yamdb
```

* Выполнить миграции
```bash
python manage.py migrate
```
Запустить проект
```bash
python manage.py runserver
```

Открыть документацию проекта
```http request
GET http://127.0.0.1:8000/redoc/
```

### Импорт данных:
Для загрузки готовых объектов в БД, перейдите в директорию с файлом manage.py и воспользуйтесь этой командой в терминале 
(Имейте в виду, что если в БД уже были какие-то записи, то они будут удалены!)
```bash
python manage.py load_data
```

## Авторы проекта
# Первый разработчик 
**Сазонов Егор**
- регистрация и аутентификация
- права доступа
- работа с токеном
- система подтверждения через e-mail
# Второй разработчик 
**Валиев Александр**
- модели, view и эндпойнты
- произведения
- категории
- жанры
- реализация импорта данных из csv файла
# Третий разработчик
**Овинцев Сергей**
- отзывы
- комментарии
- рейтинг произведений
