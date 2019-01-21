FROM nginx
COPY ./index.html /usr/share/nginx/html
# f0, f1 只有這裡不同
EXPOSE 8080:80
# f0, f1 只有這裡不同