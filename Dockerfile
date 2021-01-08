#First we are going to inherit the file python file that we going to use. This file will have all the dependencies that we need.
#The FROM will locate which file we want to inherit from
#Then we put the file name that is python and the version.
FROM python:3.9-alpine

#Now we add the maintainers name it can be your company's name.
MAINTAINER Aryan Pandhare

#Now we set the environment to the run the python code.
#The environment here we use is PYTHONUNBUFFERED which is
#the python running in unbuffered environment.
ENV PYTHONUNBUFFERED 1

#Now we are going to copy the requirements.txt file in the local directory to dockers image requirement.txt file which will store all the file dependencies.
#The requiremnt.txt file in docker file will have all the libraries that are required to build the project.
COPY ./requirements.txt /requirements.txt

#Now we will download all the porject dependencies(all the library or frameworks) in the docker image to required to build this project.
#pip install is the command to install the libraries. -r is the flag and reads the file file passed along with it and downloads all the libraries or frameworks in requirements.txt file.
RUN pip install -r /requirements.txt

#Now this run command will create the /app directory in docker image.
RUN mkdir /app

#This command will set the our /app as working directory.
#In other words this will be our default directory.
WORKDIR /app

#Now we will copy all the files that are in the ./app local directory to docker /app directory
COPY ./app /app

# Now we will create the user that is going to run the application using the docker
# The -D will only allow user to run the application and make any changes to application.
# The -D is for security purposes.
RUN adduser -D user

#Now we are going to switch to the user created above
USER user
