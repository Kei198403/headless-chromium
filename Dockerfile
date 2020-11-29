FROM ubuntu:20.04

USER root

ADD bin/headless-chromium /usr/local/bin/.
ADD bin/chromedriver /usr/local/bin/.

RUN \
  chmod +x /usr/local/bin/headless-chromium && \
  chmod +x /usr/local/bin/chromedriver

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

# Install.
RUN \
  apt-get update && \
  apt-get install -y wget git gnupg sudo tzdata && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
  apt-get update && \
  apt-get install -y google-chrome-stable && \
  apt-get install -y language-pack-ja-base language-pack-ja && \
  locale-gen ja_JP.UTF-8 && \
  apt-get autoremove -y python3.8 && \
  apt-get remove -y google-chrome-stable && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables.
ENV LANG ja_JP.UTF-8
ENV PYTHONIOENCODIND utf_8

# Define default command.
CMD ["/bin/bash"]
