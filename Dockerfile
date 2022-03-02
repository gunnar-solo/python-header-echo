FROM python:3
ENV PYTHONUNBUFFERED=1
ADD main.py /
EXPOSE 8000
CMD [ "python", "/main.py"]