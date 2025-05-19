# 🎥 IMDB Top 250 Movies

A data engineering project that scrapes IMDb's Top Rated Movies, processes the data, and stores it in AWS S3. Designed with modular components for future orchestration using Apache Airflow.


## 📌 Project Goals

- 🔍 **Scrape** the latest IMDb Top 250 movies
- 🧹 **Clean and transform** the scraped data (e.g., convert runtime to hours/minutes)
- ☁️ **Upload** processed data to **Amazon S3**
- ⏱️ Designed for future **Airflow automation**


## ⚙️ How It Works

1. **Scraper** pulls the Top 250 movies from IMDb.
2. **Transformer** cleans/standardizes the data (e.g., formats runtime, removes extra characters).
3. **Uploader** pushes the cleaned file to a specified AWS S3 bucket.
4. **Future**: Airflow DAG will automate these steps on a schedule.


## 🧰 Technologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Beautiful Soup 4](https://img.shields.io/badge/Beautiful%20Soup%204-000000.svg?style=for-the-badge&logo=beautifulsoup4-aws&logoColor=white) ![S3](https://img.shields.io/badge/Amazon%20S3-FF9900?style=for-the-badge&logo=amazons3&logoColor=white) ![dotenv](https://img.shields.io/badge/dotenv-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=black) 

## 🔧 Data Arcitecture
...

