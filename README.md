## Rest Api - Dart WeekRest

### Request POST

http://localhost:5000/user/create

```json
{
	"login":  "example",
	"password":  "123",
}
```

###Response
```json
{
    "create": status,
    "user":  login
}
```

### Request POST

http://localhost:5000/user/login

```json
{
	"login":  "example",
	"password":  "123",
}
```

###Response
```json
{
    "token": "Bearer.......",
    "validate": true
}
```

### Request POST

http://localhost:5000/category

```json
{
	"name":"Salário",
	"category": "expense" or "income"
}
```

###Response
```json
{
    "category": "expense",
    "id": 2,
    "name": "Salário"
}
```


### Request GET

http://localhost:5000/category/type
```json
types = {
	"0": "expense",
	"1": "income"
}
```
0 =>  expense
1 => income

```json
{
	"name":"Salário",
	"category": "expense" or "income"
}
```

###Response
```json
[
    {
        "id": 2,
        "nome": "Salário"
    }
]
```
### Request GET

http://localhost:5000/category/dell/id

###Response
```json
{
    "deleted": "category name"
}
```

### Request POST

http://localhost:5000/transaction/id
*id referente a categoria*

```json
{
	"value": 123.00,
	"description": "alguma coisa ",
	"date": "2020/04/02" (Opcional)
}
```

###Response
```json
{
    "category": {
        "id": 2,
        "name": "Salário",
        "type": "expense"
    },
    "date": "02/04/2020",
    "description": "alguma coisa",
    "id": 1,
    "user": "Yuri",
    "value": 123
}
```

### Request GET

http://localhost:5000/transaction/total/ano-mes
*EX: 2020-04*

###Response
```json
{
    "balance": 0,
    "expenses": 369,
    "incomes": 0,
    "total": 369
}
```

### Request GET

http://localhost:5000/transaction/month/ano-mes
*EX: 2020-04*

###Response
```json
[
    {
        "category": {
            "id": 1,
            "name": "Salário",
            "type": "expense"
        },
        "date": "02/04/2020",
        "description": "alguma coisa 1",
        "id": 1,
        "user": "Yuri",
        "value": 100
    },
    {
        "category": {
            "id": 1,
            "name": "Salário",
            "type": "expense"
        },
        "date": "02/04/2020",
        "description": "alguma coisa 2",
        "id": 2,
        "user": "Yuri",
        "value": 99
    },
    {
        "category": {
            "id": 1,
            "name": "Salário",
            "type": "expense"
        },
        "date": "02/04/2020",
        "description": "alguma coisa 3",
        "id": 3,
        "user": "Yuri",
        "value": 101
    }
]
```