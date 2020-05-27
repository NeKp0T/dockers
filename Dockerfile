FROM httpd:2.4

# ADD server/contents/* /usr/local/apache2/htdocs/
EXPOSE 8000
EXPOSE 8001

# CMD ["python", "-m", "http.server", "8000"]