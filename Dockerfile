# base image  
FROM python:3.9
# setup environment variable  

WORKDIR /home/app/webapp/

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY ./requirements.txt .

RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  

# copy whole project to your docker home directory. 
COPY . /home/app/webapp/

# port where the Django app runs  
EXPOSE 8000 
# start server  
# CMD python manage.py runserver 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]