FROM python:3.9-alpine3.13

LABEL maintainer="najah"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000

# devだけ使うパッケージをインストールする用のフラグ
ARG DEV=false

    # venv作成
RUN python -m venv /py && \
    # pipのインストール
    /py/bin/pip install --upgrade pip && \
    # postgreSQL用の追加のパッケージ（apkはAlpine Linuxのpakage manager）
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # pythonのパッケージをインストール
    /py/bin/pip install -r /tmp/requirements.txt && \
    # dev用のパッケージをインストール
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # 後処理（もう使わないものを削除）
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # ユーザを作成
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user