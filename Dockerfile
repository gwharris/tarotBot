FROM python:3.9

COPY bot/bot.py /bots/
COPY bot/cards.py /bots/

WORKDIR /bots
CMD ["python3", "bot.py"]