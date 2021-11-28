FROM tiangolo/uvicorn-gunicorn-starlette:python3.9

RUN pip install aiofiles aiohttp jinja2 pytest

COPY ./app /app