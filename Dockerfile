FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    libldap2-dev \
    libsasl2-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /odoo

COPY odoo-18/ ./odoo-18/
COPY custom-addons/ ./custom-addons/
RUN pip install -r odoo-18/requirements.txt

COPY odoo.conf ./odoo.conf

EXPOSE 8069

CMD ["python3", "odoo-18/odoo-bin", "-c", "odoo.conf"]