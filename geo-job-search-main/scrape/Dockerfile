FROM python:3.12
WORKDIR /scrape
ADD . /scrape
RUN pip install -U --no-cache-dir beautifulsoup4 selenium webdriver-manager
RUN pip install -U pytest
RUN pip install -U pytest-cov
RUN pip install -U pylint

RUN pip install -U pylint
RUN apt-get update
RUN apt-get install -y chromium


# Set Chromium as the default browser for Selenium
ENV CHROME_BIN=/usr/bin/chromium

ENV PYTHONPATH="${PYTHONPATH}:."
RUN chmod u+x runscript.sh
CMD ["./runscript.sh"]

