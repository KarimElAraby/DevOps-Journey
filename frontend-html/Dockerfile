FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install --no-cache-dir -r requirements.txt
ADD . /code/
EXPOSE 5001
CMD ["python3", "front.py" ]
