from thewtex/opengl-mesa

ADD apt-requirements.txt apt-requirements.txt
ADD pip-requirements.txt pip-requirements.txt

RUN apt update -y
RUN apt install -y $(cat apt-requirements.txt)
RUN apt install -y $(cat apt-requirements.txt)
    
RUN pip install -r pip-requirements.txt

WORKDIR /app
ENTRYPOINT python3 setup.py develop && pytest 
