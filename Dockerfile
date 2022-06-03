FROM tiangolo/uvicorn-gunicorn-starlette:python3.9

# copy requirements.txt to the directory
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app