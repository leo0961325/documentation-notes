FROM nginx
COPY ./index.html /usr/share/nginx/html
# f0, f1 只有這裡不同
EXPOSE 80:8080
# f0, f1 只有這裡不同