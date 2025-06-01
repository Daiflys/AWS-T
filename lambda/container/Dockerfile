# Use AWS python base image
FROM public.ecr.aws/lambda/python:3.13

#Copy over function specific code
COPY function/function.py function/requirements.txt /var/task/

#Install requirements
RUN python 3.13 -m pip install -r /var/task/requirements.txt

# Set the file function.py and the function handler as the lambda function.
CMD ["function.handler"]