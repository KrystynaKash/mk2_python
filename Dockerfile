FROM python:3.12-slim

WORKDIR /kashtanova

COPY programs/ /kashtanova/

CMD ["bash"]