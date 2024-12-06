# HabitSaga - Machine Learning API

This is the source code of the API for the tasks prioritization model.

## POST `/predict`

### Request
Content-Type: `application/json`    
Request Body:
```jsonc
{
    "tasks": [
        "task1",
        "task2",
        // ...
    ]
}
```

### Response
Content-Type: `application/json`    
Response Body:
```jsonc
{
    "labels": [
        "label for task1",
        "label for task2",
        // ...
    ]
}
```
The label is one of 
- `urgent important`
- `not-urgent important`
- `urgent not-important`
- `not-urgent not-important`