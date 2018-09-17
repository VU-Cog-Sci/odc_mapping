from knapenlab/nd:0.0.10gillesdev

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "zsh"]

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

COPY spynoza /spynoza
RUN bash -c "source activate neuro && pip uninstall -y spynoza && cd /spynoza && python setup.py develop"

COPY ./analysis /src
WORKDIR /src
RUN echo "source activate neuro" >> ~/.zshrc
RUN bash -c "source activate neuro && pip install lxml --upgrade"
COPY nipype.cfg /root/.nipype/nipype.cfg

RUN apt-get update -qq && apt-get install -y python python-pip python-dev build-essential software-properties-common openjdk-8-jdk
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)" /docker-java-home
ENV JAVA_HOME /docker-java-home
ENV JCC_JDK /docker-java-home

RUN apt-get install -y jcc

RUN conda create --name nighres python=2.7 numpy scipy ipython jcc

RUN git clone https://github.com/nighres/nighres /nighres && \
    cd /nighres && /bin/bash -c "cd /nighres && source activate nighres && ./build.sh && python setup.py install && pip install pybids"
    
