# pull official base image
FROM python:3.9.5-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./entrypoint.sh /code/entrypoint.sh
COPY . /code/app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
ENV PYTHONPATH "${PYTHONPATH}:/code/app"
CMD ["/code/entrypoint.sh"]
