FROM python:3.7
LABEL maintainer="r_jeka@mail.ru"

RUN pip install pytelegrambotapi && mkdir -p /opt/app

COPY ../*.py /opt/app/



WORKDIR /opt/app
ENTRYPOINT ["python3", "bot.py"]
