FROM python:3.7
LABEL maintainer="r_jeka@mail.ru"

RUN pip install pytelegrambotapi && mkdir -p /opt/app

COPY ../bot.py /opt/app/bot.py
COPY ../menu.py /opt/app/menu.py



WORKDIR /opt/app
ENTRYPOINT ["python3", "bot.py"]
