FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .

CMD ./entrypoint.sh