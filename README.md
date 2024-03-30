
# Web Service Iris

Web Service ทำนายประเภทดอก IRIS พัฒนาโดยใช้ flask


## API Reference

#### Get (Parameter)

```http
  GET /api/<sepal_length>/<sepal_width>/<petal_length>/<petal_width>

  ตัวอย่าง http://localhost:5001/api/1/2/3/4
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sepal_length` | `float` | ความยาวกลีบเลี้ยง **Required**. |
| `sepal_width` | `float` | ความกว้างกลีบเลี้ยง **Required**. |
| `petal_length` | `float` | ความยาวกลีบดอกไม้ **Required**. |
| `petal_width` | `float` | ความกว้างกลีบดอกไม้ **Required**. |

#### POST (Body (json))

```http
  POST /api

  ตัวอย่าง http://localhost:5001/api

{
    "sepal_length": 1,
    "sepal_width": 1,
    "petal_length": 1,
    "petal_width": 1
}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sepal_length` | `float` | ความยาวกลีบเลี้ยง **Required**. |
| `sepal_width` | `float` | ความกว้างกลีบเลี้ยง **Required**. |
| `petal_length` | `float` | ความยาวกลีบดอกไม้ **Required**. |
| `petal_width` | `float` | ความกว้างกลีบดอกไม้ **Required**. |


