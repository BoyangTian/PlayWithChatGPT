FROM nginx:stable-alpine3.17

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir -p /usersite/var/logs

# Copy custom Nginx configuration
# COPY ../../etc/nginx.conf /etc/nginx/conf.d/
COPY ../../etc/nginx.conf /etc/nginx/nginx.conf
# COPY ../../etc/nginx.conf /etc/nginx/conf.d/default.conf

# Copy static files from the Django application
COPY ../../static /usersite/www/public/static/

# Expose port 80 for web traffic
# EXPOSE 80
EXPOSE 9000

# Start Nginx server
CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]