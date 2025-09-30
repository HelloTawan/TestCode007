# Stock Analysis Web Application

เว็บแอปพลิเคชันวิเคราะห์หุ้นด้วย Django ที่ดึงข้อมูลหุ้นจริงจากตลาดหุ้นสหรัฐ

## Features

- 🔍 ค้นหาหุ้นด้วยสัญลักษณ์ (เช่น AAPL, GOOGL, MSFT)
- 📊 แสดงข้อมูลบริษัทและราคาหุ้น
- 📈 ประวัติราคาหุ้นย้อนหลัง 5 วัน
- 🌐 ดึงข้อมูลแบบเรียลไทม์จาก Yahoo Finance API
- 📱 Responsive design

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TestCode007
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
cd stockanalysis
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Open your browser and go to `http://localhost:8000`

## Usage

1. เข้าใช้งานที่ `http://localhost:8000`
2. ป้อนสัญลักษณ์หุ้นในช่องค้นหา (เช่น AAPL, GOOGL, MSFT, TSLA, AMZN)
3. กดปุ่ม "Search Stock" เพื่อดูข้อมูลหุ้น
4. ระบบจะแสดงข้อมูลบริษัทและประวัติราคาหุ้น

## Technology Stack

- **Backend**: Django 5.2.6
- **Data Source**: yfinance library (Yahoo Finance API)
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, JavaScript
- **Dependencies**: pandas, numpy

## API Fallback

หากไม่สามารถเชื่อมต่อ Yahoo Finance API ได้ (เช่น ในสภาพแวดล้อมที่จำกัด) ระบบจะแสดงข้อมูลตัวอย่างแทน เพื่อให้สามารถทดสอบการทำงานได้

## Project Structure

```
stockanalysis/
├── manage.py
├── stockanalysis/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── stocks/
    ├── views.py
    ├── urls.py
    └── templates/
        └── stocks/
            ├── base.html
            ├── home.html
            └── stock_detail.html
```
