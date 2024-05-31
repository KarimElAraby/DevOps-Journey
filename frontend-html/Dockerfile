FROM python:3.8-slim
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 5001
CMD ["python", "front.py"]
