# запуск приложения

./venv/bin/flask --app ./acme-api/server.py run



## cURL тестирование

### добавление новой заметки
curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"


### добавление нового события
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "date|title|text"


### получение всего списка заметок
curl http://127.0.0.1:5000/api/v1/note/

### получение всего списка событий
curl http://127.0.0.1:5000/api/v1/calendar/

### получение заметки по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/note/1/

### получение события по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/calendar/1/

### обновление текста заметки по идентификатору / ID == 1 /  новый текст == "new text"
curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"

### обновление описания события по идентификатору / ID == 1 /  новый текст == "new text"
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "date|title|new text"

### удаление заметки по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE

### удаление события по идентификатору / ID == 1
curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE


## пример исполнения команд с выводом

# для заметок

$ curl http://127.0.0.1:5000/api/v1/note/ -X POST -d "title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/note/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/note/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "title|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 120

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X PUT -d "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 60

$ curl http://127.0.0.1:5000/api/v1/note/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/note/
-- пусто --

## для календаря

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2022-08-21|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
2022-08-21|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
2022-08-21|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2023-08-21|new title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
2023-08-21|new title|new text