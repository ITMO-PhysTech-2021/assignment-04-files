# Json

## `save_color`

Аргумент `color` - это `dict` с ключами `r`, `g`, `b` -
красный, зелёный и синий компонент соответственно (целые числа 0 - 255),
а также `a` - прозрачность (число с плавающей точкой от 0 до 1).

Необходимо записать переданный цвет в файл с именем `filename` в формате JSON,
используя стандартные средства Python.

Пример:
```python
color = {
    'r': 255,
    'g': 0,
    'b': 0,
    'a': 0.5
}
save_color(color, 'output.json')
```

Результат в output.json:
```json
{ "r": 255, "g": 0, "b": 0, "a": 0.5 }
```

## `load_color`
Аналогично предыдущему заданию, нужно загрузить цвет из указанного JSON-файла
и вернуть в виде `dict` описанной ранее структуры.

## `links`
В указанном JSON-файле хранится структура, представляющая
некоторое подмножество веб-страниц со списком исходящих ссылок на другие страницы:


```json
{
  "websites": [
    {
      "url": "google.com/search",
      "links": [
        "microsoft.com",
        "aliexpress.com",
        "google.com/search/2"
      ]
    },
    {
      "url": "microsoft.com",
      "links": []
    },
    {
      "url": "twitter.com",
      "links": [
        "google.com",
        "facebook.com/post/1271",
        "facebook.com/post/3411",
        "microsoft.com"
      ]
    }
  ]
}
```

Реализованная функция должна вернуть список всех страниц
с количеством ссылок для каждой из них.

Пример результата для приведённого выше файла:
```python
[
    ('google.com', 1),
    ('google.com/search', 0),
    ('google.com/search/2', 1),
    ('microsoft.com', 2),
    ('aliexpress.com', 1),
    ('facebook.com', 1),
    ('facebook.com/post/1271', 1),
    ('facebook.com/post/3411', 1)
]
```

Порядок записей в возвращаемом списке не важен.
