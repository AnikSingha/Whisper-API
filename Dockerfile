FROM ubuntu:22.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git ffmpeg
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
