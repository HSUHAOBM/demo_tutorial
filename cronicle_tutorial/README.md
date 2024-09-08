
#  Cronicle
https://cronicle.net/

一個簡單的任務調度和運行平台。

該專案是用 Node.js 寫的 cron 替代品，它開箱即用、自帶 Web 介面、無需資料庫，提供了執行 shell 命令、實時統計、自動故障轉移、自動重試、多時區等功能。



## 安裝
### 方式 1：
* 伺服器上需預先安裝Node.js LTS

https://github.com/jhuckaby/Cronicle/blob/master/docs/Setup.md

### 方式 2：docker 容器啟動（建議）

* 伺服器上需預先安裝 Docker 、 Git
* Docker 教學 http://172.25.202.38/demo/docker_tutorial
* ubuntu 安裝 Docker  https://docs.docker.com/engine/install/ubuntu/

啟用步驟
1. 至 github clone 專案
https://github.com/soulteary/docker-cronicle
```
# ssh
git clone git@github.com:soulteary/docker-cronicle.git

# https
git clone https://github.com/soulteary/docker-cronicle.git
```

2. 使用 compose 啟用 並在背景執行
```
docker compose up -d
```

3. 訪問網站
```
http://localhost:3012

預設帳號密碼為 admin / admin
```

4. 停止服務
```
docker compose dwon
```

## 操作
*  簡易操作 參閱 eu_doc 資料夾
* 詳細操作參閱 官方文檔（配置設定、UI教學、API等等）
https://github.com/jhuckaby/Cronicle/tree/master/docs

### 實機操作與相關延伸
* 操作建立一個排程

<br>

* 如何修改相關配置（ docker ）

```
1.檢視 容器清單
docker ps

舉例
751e0155183d   soulteary/cronicle:0.9.23   "docker-entrypoint.s…"   20 hours ago   Up 4 seconds (health: starting)   0.0.0.0:3012->3012/tcp, :::3012->3012/tcp   docker-cronicle-cronicle-1

2. 進入容器
docker exec -it docker-cronicle-cronicle-1 sh
或
docker exec -it 751e0155183d sh

3. 使用 vi 修改配置
vi /opt/cronicle/conf/config.json

4. 退出容器

5. 停止容器並啟動
docker-compose down && docker-compose up -d
```
<br>

---

<br>


*  webhook 設置 + slack、Discord 通知
https://github.com/jhuckaby/Cronicle/wiki/Slack-Webhook-Integration
https://github.com/jhuckaby/Cronicle/wiki/Discord-Webhook-Integration

<br>

---

<br>

* 寄信(gmail)
修改 config.json

```
# https://nodemailer.com/smtp/
# https://github.com/jhuckaby/Cronicle/issues/440
"smtp_hostname": "smtp.gmail.com",
"smtp_port": 587,

"mail_options": {
    "secure": false,
    "auth": { "user": "youremail@gmail.com", "pass": "google 應用程式密碼 " },
    "tls": {
     "rejectUnauthorized":false,
     "requireTLS":true
  }
},
```

##### 補充
* 信件相關模板 路徑
```
/opt/cronicle/conf/emails # ls
changed_password.txt  event_error.txt       job_fail.txt          job_success.txt       recover_password.txt  welcome_new_user.txt
```
* google 寄信
```
1. gmail 信箱，點右上設定，轉寄和POP/IMAP，選擇 啟用IMAP，
2. 帳戶安全性設置,兩步驟驗證啟用
3. 申請定應用程式密碼 （ config PASSWORD 用）
```

<br>

## 相關連結
> [官方](<https://cronicle.net/>)
>
> [官方開源 github](<https://github.com/jhuckaby/Cronicle>)
>
> [docker 版本 github](<https://github.com/soulteary/docker-cronicle>)
