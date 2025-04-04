FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN pip install django-minio-storage

RUN mkdir -p /var/www/static
RUN mkdir -p /var/www/media

EXPOSE 80