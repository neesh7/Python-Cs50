similar to express.js fastapi is there in python

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