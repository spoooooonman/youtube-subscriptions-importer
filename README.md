# youtube-subscriptions-importer

A little script for importing youtube subscriptions to a channel from subscriptions.csv (Google Takeouts)

## What is it about?

It scrapes subscription urls from Google Takeouts **_subscriptions.csv_** file. 
It opens a tab for every single url in the file with [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) and subscribe.

# Built with

- Selenium
- Undetected-chromedriver
- Pandas

# Prerequisties

- Python 3.x

# Installation

- Install the repository.

```
git clone https://github.com/spoooooonman/youtube-subscriptions-importer/
```

- Install requirements from **requirements.txt**

```
pip install -r requirements.txt
```

- Insert your data in the empty variables in youtube-subscriptions-importer.py

- Run the script.
