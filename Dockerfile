FROM ubuntu:20.04
FROM python:3.9

# Allows docker to cache installed dependencies between builds
COPY requirement.txt requirement.txt
RUN pip install --no-cache-dir -r requirement.txt

RUN apt update && apt install python3-dev -y

#RUN apt install libpython3.9-dev -y

# Mounts the application code to the image
COPY . code

WORKDIR /code

RUN pip install web3_auth_django-0.7-py3-none-any.whl

RUN python manage.py makemigrations


RUN python manage.py migrate
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
