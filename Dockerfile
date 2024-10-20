FROM python:3.9

RUN apt-get update && \
    apt-get install -y pandoc texlive texlive-xetex texlive-latex-extra && \
    pip install --upgrade pip && \
    pip install Flask flask-cors


COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
