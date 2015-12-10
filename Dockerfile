FROM python:2-onbuild

COPY ./ /src
WORKDIR /src

virtualenv .
./bin/python setup.py install

EXPOSE 8080
CMD ["./python", "app.py"]
