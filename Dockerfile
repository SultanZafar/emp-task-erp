FROM python:3.12-slim
RUN apt-get update && apt-get install -y \
libpq-dev \
build-essential \
libldap2-dev \
libsasl2-dev \
libsasl2-dev \
libsasl2-dev \
WORKDIR /odoo
COPY custom-addons/ ./custom-addons/
EXPOSE 8069
CMD ["odoo", "--addons-path=custom-addons"]
