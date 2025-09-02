FastAPI is a modern, high-performance web framework for building APIs (Application Programming Interfaces) with Python. It is designed to be fast, efficient, and easy to use, leveraging standard Python type hints for data validation and automatic documentation generation. 

## required 
- uvicorn
- pydantic

```bash
$ pip install fastapi uvicorn
# or if using uv then
$ uv add fastapi uvicorn

# to run the file
$ uvicorn main:app --reload
```

### Access the app on
http://127.0.0.1:8000/ 
http://127.0.0.1:8000/docs