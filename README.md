# ToDoList-DEPI-Project

## Intiallization

- Step 1: Clone the Repository: (<https://github.com/E-963/ToDoList-DEPI-Project>)

- Step 2: Create a virtual environment and install dependencies

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Run App

### Development

```bash
python3 main.py
```

### Production

```bash
gunicorn wsgi
```

## **Testing**

```bash
pytest
```
