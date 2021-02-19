# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    host:logger:consoleLoggingMode=always

COPY . /home/site/wwwroot

EXPOSE 8080

COPY requirements.txt /
RUN pip install -r /requirements.txt


