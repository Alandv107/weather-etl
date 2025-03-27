# 🌤 天氣與 PM2.5 數據清洗上傳系統


此專案會自動從 MongoDB 中擷取天氣與 PM2.5 資料，進行清洗與統整後，依據上午 / 下午時段分類並上傳至 MySQL 資料庫，便於後續分析與報表製作。

---

## 📌 專案功能

- 自動抓取前一天的天氣與 PM2.5 原始資料
- 統整、清洗城市資訊與時間欄位
- 分成「6~14」與「15~23」兩個時段統計
- 輸出至 MySQL 資料庫，包含週次與日夜欄位

---

## 🛠️ 技術棧

- Python 3
- MongoDB / PyMongo
- Pandas / NumPy / SciPy
- SQLAlchemy / MySQL
- dotenv 環境設定

---

## ⚙️ 安裝與執行

```bash
pip install -r requirements.txt
cp .env.example .env
# 編輯 .env 填入 MongoDB / MySQL 資訊
python run_etl.py
