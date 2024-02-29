FROM python:3.12-alpine AS builder
WORKDIR /app
COPY . .
RUN chmod +x start.sh
RUN chmod +x wait-for.sh
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD [ "python3", "manage.py", "runserver" ]