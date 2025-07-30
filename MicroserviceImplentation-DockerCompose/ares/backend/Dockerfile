from python:3.8-slim

ADD backend/requirements.txt /tmp/requirements.txt

ENV BACKEND_URL=http://0.0.0.0:8000

RUN pip install -r /tmp/requirements.txt

ADD backend /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["app.py"]

