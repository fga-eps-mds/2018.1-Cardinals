FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
COPY ./ /code/
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt
RUN pip install --pre --upgrade PyGithub