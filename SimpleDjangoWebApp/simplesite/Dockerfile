FROM python:3.9.6

ENV PYENV_VERSION="v2.3.17"

# TODO: for docker we even don't need pyenv
# # Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    # cd ~/.pyenv && \
    # git checkout $PYENV_VERSION

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"

RUN git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
# RUN git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv && \
    # cd $(pyenv root)/plugins/pyenv-virtualenv && \
    # git checkout $PYENV_VIRTUALENV_VERSION

RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

RUN pyenv --version
RUN pyenv --help

RUN pyenv virtualenvs

RUN mkdir -p /app

WORKDIR /app

RUN ls

COPY ../. /app/

# TODO: ugly since we didn't use different .env for different environment, just overwrite, change later
RUN rm /app/simplesite.env
RUN mv /app/prod-simplesite.env /app/simplesite.env

RUN echo $DB_HOST

RUN pwd
RUN ls

RUN make install

# # expose port
EXPOSE 8000

ENTRYPOINT ["make", "run"]