FROM python:2-onbuild

COPY ./ /src
WORKDIR /src

RUN virtualenv myenv
RUN myenv/bin/python setup.py install

EXPOSE 8080
CMD ["myenv/bin/python", "app.py"]
