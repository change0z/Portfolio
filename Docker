FROM python:latest

LABEL maintaner="change0z"
LABEL version="1.0"
LABEL description="docker image to run all the projects mentioned here. NOTE: this image is not meant to be used for production and wont satify all the dependcies requiered to run the linked projects (projects that are not part of this particular repository). Please use the image attached in repository"

RUN pip install jupyter numpy pandas matplotlib seaborn plotly dash seaborn scipy scikit-learn torch nltk beautifulsoup4 requests 

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]