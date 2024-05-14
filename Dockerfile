FROM python:latest

LABEL maintaner="Ziyad"
LABEL version="1.0"
LABEL description="docker image for the string separation project"

RUN pip install jupyter numpy pandas matplotlib seaborn plotly dash seaborn scipy scikit-learn torch nltk 

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]