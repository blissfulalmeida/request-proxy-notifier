FROM mitmproxy/mitmproxy:10.4.2

WORKDIR /usr/src/app

RUN pip install httpx

COPY ./src/mitmproxy/addon.py .

ENTRYPOINT ["sleep", "infinity"]
