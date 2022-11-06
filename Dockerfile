FROM python:3.10
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
EXPOSE 8080
COPY ./ /app

# Utility that enables this container to wait for other one before it starts
#ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
#RUN chmod +x /wait

#CMD /wait && python main.py
CMD ["python", "main.py"]