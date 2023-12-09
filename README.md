# ChatGPT-Linebot using python flask on vercel 

> 作者註：本專案因為作者我的免費 API 額度已經用完了，然後我現在使用的是 `ChatGPT Plus`，
> 
> 如果之後要我本人更新可能要等我哪天改用 ChatGPT API 了...
> 
> 現在最新的版本感謝網友 @willismax 提供的 PR：https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel/pull/17
> 
> 但同樣的因為我沒有 ChatGPT API 的額度了... 所以也沒辦法測就直接 merge 了，
>
> 如果不能動再請大家幫忙發個 Issues/PR，感謝大大們🙏

* last updated: 2023/10/9
  - 更新說明 by @willismax，與修正的 [repo](https://github.com/willismax/GPT-Linebot-python-flask-on-vercel) (merged)
    - vercel.json修正，改為第2版
    - 修正單純安裝Flask==2.2.2 會與 Werkzeug 衝突的問題，在 requirements.txt 添加 Werkzeug==2.3.7 ([參考stack overflow](https://stackoverflow.com/questions/77213053/importerror-cannot-import-name-url-quote-from-werkzeug-urls))

> `本篇教學無經驗的新手也可學習，無須寫任何程式。`
> 
> 無經驗預計 15 ~ 20 分鐘都可以完成。老手最快可能 5 分鐘就搞定

* 這是使用 python flask 套件撰寫的 ChatGPT-Linebot
* `不需寫 code`，只需去網頁設定一些內容，新手 15 分鐘內也能建立自己的 ChatGPT-Linebot
* Why flask? 簡單好用，且支援 vercel
* Why vercel? `免費`！！！免費額度就很夠一般使用，是 heroku 不再免費後的好選擇

> ~~註：ChatGPT 與 gpt 是同樣任務的模型，而目前透過 API 只能使用到 GPT-3 (本程式使用的方法)~~
> 
> ~~而非 ChatGPT 使用的 GPT-3.5~~
>
> 已經改為 GPT-4，與最新的 ChatGPT 相同，只是改為使用 OpenAI API 的方式實現

# 安裝步驟

主要會有四個地方要去：(`這部份不看也沒關係，以下照著做就可以了！`)

* 我的 github repo：透過 python 串接 openai 的 API，並透過 linebot sdk 提供簡單的訊息回復
* openai：申請 OpenAI 的 API KEY
* line developer：創建機器人
* vercel：提供訊息回復，雖然是 serverless 但已經很符合我們的需求



## step 1. 至 github fork 專案

去我這個專案的 [github repo](https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel "github repo")



按下面的按鈕，
fork 一份檔案到自己的帳號底下，等等我們會使用到

> `可以的話，旁邊的 Star 也幫我按一下，是對創作者最大的鼓勵！`

[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午7.27.12.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%887-27-12/)

## step 2. 申請 OpenAI 的 API KEY

可以直接去[這裡]( https://beta.openai.com/docs/quickstart/build-your-application "這裡")，一直往下拉，找到這個按鈕，並生成一個 API KEY



[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.11.22.png)](https://www.wongwonggoods.com/?attachment_id=8016)


> 請務必複製下來，這個 KEY 我們取名為 `OPENAI_API_KEY `

## step 3. 去 line developer 建立一個新的機器人

> 這邊熟悉的人動作應該超快，可以略過，
>
> 以下教學是針對完全沒經驗的新手

我們先到[ line developer 的首頁](https://developers.line.biz/zh-hant/ " line developer 的首頁")註冊一下，
註冊完後，點選 Messaging API。

[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.32.33.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%886-32-33/)

### step 3-1. 創建新的 channel

第一次使用要創建一個新的 provider 與 channel，
一個 provider 可以有很多 channel，
「`而一個 channel 對應的就是一個 chatbot`」，
這邊以下都照自己想要的名字跟事實填就好。


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.36.49.png)](https://www.wongwonggoods.com/?attachment_id=8019)

### step 3-2. 在 Basic Settings 的分頁，取得 LINE_CHANNEL_SECRET


在 Basic Settings 的分頁，往下找到 channel secret


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.40.36.png)](https://www.wongwonggoods.com/?attachment_id=8021)



> 請務必複製下來，這個 KEY 我們取名為 `LINE_CHANNEL_SECRET `


### step 3-3. 在 Messaging API 的分頁，進行一些機器人初始設定 (並加機器人好友)

再來我們去上方，選擇 Messaging API 的分頁，
我們先關閉一些可能會吵的東西 (預設的自動回復之類的)，


> `這邊可以順便掃一下 QR code 或透過 line ID ，加機器人的 line 好友！　`


我自己是設定如下：


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.41.06.png)](https://www.wongwonggoods.com/?attachment_id=8022)


* 允許加入群組要注意使用 openai 額度可能會超快
* 「`自動回復訊息必關！！！`」，那是 line 的自動回復，不是我們要的
* 歡迎訊息也可以關，這邊我是開著

### step 3-4. 在 Messaging API 的分頁，取得 LINE_CHANNEL_ACCESS_TOKEN

最後，在 Messaging API 的分頁的最下面，
找到 channel access token，點選右邊發行，並把他記下來。



[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午6.41.14.png)](https://www.wongwonggoods.com/?attachment_id=8020)



> 請務必複製下來，這個 KEY 我們取名為 `LINE_CHANNEL_ACCESS_TOKEN `
>
> 請不要把這金鑰分享給別人，別人可能會拿去作壞事！！！


`然後這邊網頁先不要關，等等還會用到！！！！`


## step 4. 去 vercel 設定相關的環境變數，完成啟動機器人！


### step 4-1. 新增 project

去 [vercel 首頁](https://vercel.com/ "vercel 首頁")，add new project



Import Git Repository，選擇你剛剛 fork 的專案 import

[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午7.39.19.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%887-39-19/)

### step 4-2. 設定環境變數

選擇「Environment Variables」，把我們剛剛紀錄的 OPENAI_API_KEY、LINE_CHANNEL_SECRET、LINE_CHANNEL_ACCESS_TOKEN 都設定至環境變數，
按下 Deploy 等待一下就完成囉！




[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午7.46.13.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%887-46-13/)


* 完成後我們可以看到會有以下的三個環境變數


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午7.47.23.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%887-47-23/)

###  step 4-3. deploy 完成後，可以簡單確認是否有成功

去部屬完成的 vercel 頁面，紅框處可以拿到我們要用的網址，

`把這個網址複製下來，等等要用`

這個網址我們也可以點開，應該會出現我們在程式預先寫好的 Hello, World! (應該是一個只有 Hello, World! 的網頁)
我們可以藉此確定程式有正常的被 Deploy


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-14-上午1.25.48.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-14-%e4%b8%8a%e5%8d%881-25-48/)


## step 5. 設定 webhook


回到 line developer 的 Messaging API 分頁，
將剛剛 step 4-3. 的網址填入，並在後面加上 「/webhook」，例如下圖
可以用 Verify 看看有沒有問題，通常應該會是寫「Success」

* 「`記得開啟下面的使用 Use webhook `」



[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-13-下午9.29.23.png)](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/attachment/%e6%88%aa%e5%9c%96-2022-12-13-%e4%b8%8b%e5%8d%889-29-23/)



# 完成圖範例


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-12-下午11.24.29.png)](https://www.wongwonggoods.com/?attachment_id=8017) 


[![](https://www.wongwonggoods.com/wp-content/uploads/2022/12/截圖-2022-12-12-下午11.21.45.png)](https://www.wongwonggoods.com/?attachment_id=8018)




# 此 linebot 的其他一些內建功能 

## 機器人「說話開關」

這個本來是我除錯用的，因為有時候回復一些怪東西會很吵，
意外得到好評，所以這個功能就被保留下來

* 輸入「說話」：機器人開啟說話模式，預設是開啟的
* 輸入「閉嘴」：機器人暫停說話模式 (`但一段時間會自動再起動`)，閉嘴後將不會對任何對話有反應。輸入「說話」可再次開啟對話。

## 其他環境參數功能

參考自 [memochou1993/gpt-ai-assistant](https://github.com/memochou1993/gpt-ai-assistant?fbclid=IwAR25uqLdKoDKEQd591fSjyM2sDJJR3Xb-VgcXDIFV_7i3RMWWv2oiyG26RQ) 的作法，下列參數也可藉由設定 vercel 的環境變數來作調控。

|環境變數名稱             |預設值           |說明 |
|------------------------|--------------- |-----|
| OPENAI_MODEL            | text-davinci-003| 請參考 OpenAI 對 [model](https://beta.openai.com/docs/api-reference/completions/create#completions/create-model) 的敘述|
| OPENAI_TEMPERATURE      | 0               | 請參考 OpenAI 對 [temperature](https://beta.openai.com/docs/api-reference/completions/create#completions/create-temperature) 的敘述|
| OPENAI_FREQUENCY_PENALTY| 0               | 請參考 OpenAI 對 [frequency_penalty](https://beta.openai.com/docs/api-reference/completions/create#completions/create-frequency_penalty) 的敘述|
| OPENAI_PRESENCE_PENALTY | 0.6             | 請參考 OpenAI 對 [presence_penalty](https://beta.openai.com/docs/api-reference/completions/create#completions/create-presence_penalty) 的敘述|
| OPENAI_MAX_TOKENS       | 240             | 請參考 OpenAI 對 [max_tokens](https://beta.openai.com/docs/api-reference/completions/create#completions/create-max_tokens) 的敘述|
| MSG_LIST_LIMIT          | 20              | prompt 參數往回參照的句數|
| INIT_LANGUAGE           | zh              | 決定初始語言，可設置為 "zh" 或 "en"|



# TODO List & Future Work


> 目前基本功能都已經有了，然後我比較忙可能沒空一直更新QQ
>
> `還有很多可以優化的地方，歡迎提供 PR！`

- [x] (已調整完成) 回復文字感覺不是很順 (可能需要研究一下 API 使用方法)
- [x] (已調整完成) 記憶功能 
...

> 目前算法是「`紀錄使用者與 AI 的前20句對話`」，嘗試推論出下一句話應該要說什麼。以達成延續話題的效果。


# 靈感來源
* 本文同步更新至我的個人網站：[【Side Project】(全圖文教學) 用 Python flask 實作類似 ChatGPT 的 Linebot，並部屬至 vercel 上](https://www.wongwonggoods.com/portfolio/personal_project/gpt-linebot-python-flask-for-vercel/)
* 感謝 [memochou1993/gpt-ai-assistant](https://github.com/memochou1993/gpt-ai-assistant?fbclid=IwAR25uqLdKoDKEQd591fSjyM2sDJJR3Xb-VgcXDIFV_7i3RMWWv2oiyG26RQ) 提供的 node.js 版本串接 vercel 示範，讓我有了想把 python linebot 也串進 vercel 的靈感，(目前感覺下來，免費又好用(?))
* 感謝 [Lanznx/HealthLineBot](https://github.com/Lanznx/HealthLineBot) 給了一個很好的 python Django 範例，然而我不會 Django XD，vercel 官方文件好像也沒有提到這部份，總之後來就改成了 flask 版本，也符合 linebot 推薦的範例。



# 參考資料

* Line 官方提供的 python flask 製作 linebot 的 sample code [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
* Vercel 官方提供的 python runtime Flask 範例 [Deploy an example with Flask](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python#python-version)


