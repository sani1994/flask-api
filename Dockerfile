FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV HOST=0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0" ]