FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt
ADD . /code/
CMD ./run.sh
