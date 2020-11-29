# headless-chromium
## これは何？
headless-chromium+seleniumのdockerイメージをビルドするための環境です。  

## headless-chromium
https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip

上記のURLより取得したもの。  
ChromiumのLinux用バイナリファイル。  
バージョンは、64.0.3282.167。

## chromedriver
https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip

上記のURLより取得したもの。  
Chromiumをseleniumから操作するためのドライバ。  
バージョンは、2.37.544315。

## Docker環境
### ビルド済みイメージ

https://hub.docker.com/r/kei198403/headless-chromium

```
docker pull kei198403/headless-chromium:latest
```

### base image
ubuntu:20.04

### インストールパス
- /usr/local/bin/headless-chromium
- /usr/local/bin/chromedriver

### 日本語フォントについて
インストールしていません。  
そのため、マルチバイトのページのスクリーンショットを撮ると文字化けします。

解消するには、以下のURLよりIPAフォントをダウンロード。  

https://moji.or.jp/ipafont/ipafontdownload/

Dockerfileに以下を追加（chromiumを実行するユーザのホームディレクトリに.fontsディレクトリを作成して、その下にフォントファイルを格納する。この例ではrootで実行する前提。）
```
RUN mkdir -p /root/.fonts
ADD ipaexg.ttf /root/.fonts/.
ADD ipaexm.ttf /root/.fonts/.
```

## AWS Lambda環境で実行するには

https://note.com/kei198403/n/n24d8f0bfb39a
