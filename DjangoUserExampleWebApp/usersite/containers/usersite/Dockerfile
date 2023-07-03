FROM python:3.9.6

ENV PYENV_VERSION="v2.3.17"

# TODO: dockerfile itself cannot be run because it cannot connect to postgresql container,
# need to use docker-compose to run

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

RUN mkdir -p /usersite

WORKDIR /usersite

RUN ls

COPY ../../. /usersite/

# TODO: ugly since we didn't use different .env for different environment, just overwrite, change later
RUN rm /usersite/etc/usersite.env
RUN mv /usersite/etc/prod-usersite.env /usersite/etc/usersite.env
# RUN rm -rf /usersite/static
RUN rm -rf /usersite/logs
RUN rm -f /usersite/usersite/settings/dev.py

RUN echo $DB_HOST

RUN pwd
RUN ls

RUN mkdir /usersite/logs
RUN ls /usersite/logs

RUN make install

# # expose port
EXPOSE 9001

ENTRYPOINT ["make", "gunicorn-run"]