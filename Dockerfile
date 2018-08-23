from knapenlab/nd:0.0.10nvtest

ENV PATH /opt/conda/envs/neuro/bin:$PATH

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "zsh"]

RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

COPY spynoza /spynoza
RUN bash -c "source activate neuro && pip uninstall -y spynoza && cd /spynoza && python setup.py develop"

COPY ./analysis /src
WORKDIR /src
RUN echo "source activate neuro" >> ~/.zshrc
