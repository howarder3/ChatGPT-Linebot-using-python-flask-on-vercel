# GPT-Linebot using python flask on local

- [GPT-Linebot using python flask on local](#gpt-linebot-using-python-flask-on-local)
- [使用方式](#使用方式)
  - [步驟一，建立並執行虛擬環境](#步驟一建立並執行虛擬環境)
    - [建立虛擬環境](#建立虛擬環境)
    - [執行虛擬環境](#執行虛擬環境)
  - [步驟二，安裝套件](#步驟二安裝套件)
  - [步驟三，申請 openAI API 與 LINE Bot API](#步驟三申請-openai-api-與-line-bot-api)
    - [openAI API 申請](#openai-api-申請)
    - [LINE Bot 機器人申請](#line-bot-機器人申請)
  - [步驟四，建立 .env 檔案](#步驟四建立-env-檔案)
    - [建立 .env](#建立-env)
    - [填入 .env](#填入-env)
  - [步驟五，執行 Flask](#步驟五執行-flask)
  - [步驟六，使用 ngrok 進行連線](#步驟六使用-ngrok-進行連線)
  - [完成](#完成)

> 此為本地端版，也可以當作雲端版。

與原分支 [howarder3/GPT-Linebot-python-flask-on-vercel](https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel) 程式檔案完全一模一樣。

只是不想使用 vercel 來造福大家了，因為我只是想玩一下。

> 已經整理出來所有環境變數，接下來建立檔案 + 申請 API 就可以使用了

# 使用方式

## 步驟一，建立並執行虛擬環境

### 建立虛擬環境

```shell
# windows
py -3.7 -m venv .venv
# linux
python3.7 -m venv .venv
```

### 執行虛擬環境

```shell
# windows
.\.venv\Scripts\activate
# linux
source .venv/bin/activate
```

## 步驟二，安裝套件

```shell
pip install -r requirements.txt
```

## 步驟三，申請 openAI API 與 LINE Bot API

### openAI API 申請

> 建議點擊網址前按下 ctrl ，會另開分頁喔 !

申請步驟：<https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel#step-2-%E7%94%B3%E8%AB%8B-openai-%E7%9A%84-api-key>

### LINE Bot 機器人申請

> 建議點擊網址前按下 ctrl ，會另開分頁喔 !

申請步驟：<https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel#step-3-%E5%8E%BB-line-developer-%E5%BB%BA%E7%AB%8B%E4%B8%80%E5%80%8B%E6%96%B0%E7%9A%84%E6%A9%9F%E5%99%A8%E4%BA%BA>

## 步驟四，建立 .env 檔案

### 建立 .env

建立這個檔案在與 ```api``` 資料夾同一層。

```shell
.
├─.venv
├ .env # 這邊
└─api

```

### 填入 .env

***必填*** 的部分一定要填 !

```dotenv
# 必填
LINE_CHANNEL_ACCESS_TOKEN = ??
LINE_CHANNEL_SECRET = ??
OPENAI_API_KEY = ??

# 選填
# OPENAI_MODEL = ??
# OPENAI_TEMPERATURE = ??
# OPENAI_FREQUENCY_PENALTY = ??
# OPENAI_PRESENCE_PENALTY = ??
# OPENAI_MAX_TOKENS = ??
# DEFALUT_TALKING = ??
# INIT_LANGUAGE = ??
# MSG_LIST_LIMIT = ??
```

選填的參考說明：<https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel#%E5%85%B6%E4%BB%96%E7%92%B0%E5%A2%83%E5%8F%83%E6%95%B8%E5%8A%9F%E8%83%BD>

## 步驟五，執行 Flask

```shell
python .\api\index.py
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

注意：

注意：

注意：

不要點 CTRL+C，程式會關閉。

不要點 CTRL+C，程式會關閉。

不要點 CTRL+C，程式會關閉。

## 步驟六，使用 ngrok 進行連線

下載 ngrok <https://ngrok.com/>

1. 解壓縮在桌面
2. 使用 cd C:\Users\yen\Desktop (假設我在這裡)

```shell
# 執行指令
./ngrok.exe http 5000
```

> 這邊的 5000 指的是 我們剛剛執行 127.0.0.1:5000

找到下面這一段字

```
Forwarding                    https://b199-210-59-249-181.jp.ngrok.io -> http://localhost:5000
```

把 ```https://b199-210-59-249-181.jp.ngrok.io``` 複製起來。

加上 ```/webhook``` 變成 ```https://b199-210-59-249-181.jp.ngrok.io/webhook```

貼到 LINE Bot -> Webhook settings

可以參考 <https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel#step-5-%E8%A8%AD%E5%AE%9A-webhook>

## 完成

![成功的圖片](https://i.imgur.com/dDX2Dzz.jpg)
