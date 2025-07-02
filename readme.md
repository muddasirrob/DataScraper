# DataScraper: A Smart, Automatic, Fast and Lightweight Web Scraper for Python

![img](https://user-images.githubusercontent.com/17881612/91968083-5ee92080-ed29-11ea-82ec-d99ec85367a5.png)

This project is made for automatic web scraping to make scraping easy.  
It gets a URL or the HTML content of a web page and a list of sample data which we want to scrape from that page.  
**This data can be text, URL, or any HTML tag value of that page.**  
It learns the scraping rules and returns the similar elements. Then you can use this learned object with new URLs to get similar content or the exact same element from those new pages.

---

## 📦 Installation

Compatible with Python 3.

- Install latest version from Git repository using pip:

```bash
pip install git+https://github.com/muddasirrob/datascraper.git
Install from PyPI:

bash
Copy
Edit
pip install datascraper
Install from source:

bash
Copy
Edit
python setup.py install
🚀 How to Use
Getting Similar Results
Say we want to fetch all related post titles from a StackOverflow page:

python
Copy
Edit
from datascraper import DataScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# Add one or more target elements you want to scrape
wanted_list = ["What are metaclasses in Python?"]

scraper = DataScraper()
result = scraper.build(url, wanted_list)
print(result)
Sample output:

python
Copy
Edit
[
    'How do I merge two dictionaries in a single expression in Python (taking union of dictionaries)?', 
    'How to call an external command?', 
    'What are metaclasses in Python?', 
    'Does Python have a ternary conditional operator?', 
    'How do you remove duplicates from a list whilst preserving order?', 
    'Convert bytes to a string', 
    'How to get line count of a large file cheaply in Python?', 
    "Does Python have a string 'contains' substring method?", 
    'Why is “1000000000000000 in range(1000000000000001)” so fast in Python 3?'
]
Use the same object on another page:

python
Copy
Edit
scraper.get_result_similar('https://stackoverflow.com/questions/606191/convert-bytes-to-a-string')
Getting Exact Result
Say we want to scrape live stock prices from Yahoo Finance:

python
Copy
Edit
from datascraper import DataScraper

url = 'https://finance.yahoo.com/quote/AAPL/'
wanted_list = ["124.81"]  # update this value as per current data

scraper = DataScraper()
result = scraper.build(url, wanted_list)
print(result)
You can also use proxies or headers:

python
Copy
Edit
proxies = {
    "http": 'http://127.0.0.1:8001',
    "https": 'https://127.0.0.1:8001',
}

result = scraper.build(url, wanted_list, request_args=dict(proxies=proxies))
Scrape the same type of data from another symbol:

python
Copy
Edit
scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/')
Scraping Multiple Elements
Example: Scrape GitHub repo details:

python
Copy
Edit
from datascraper import DataScraper

url = 'https://github.com/muddasirrob/datascraper'
wanted_list = [
    'A Smart, Automatic, Fast and Lightweight Web Scraper for Python',
    '6.2k',
    'https://github.com/muddasirrob/datascraper/issues'
]

scraper = DataScraper()
scraper.build(url, wanted_list)
💾 Saving the Model
Save the model:

python
Copy
Edit
scraper.save('yahoo-finance')
Load the model later:

python
Copy
Edit
scraper.load('yahoo-finance')
📚 Tutorials
Gist: Advanced Usage

AutoScraper & Flask: Create an API From Any Website in 5 Minutes

❗ Issues
Feel free to open an issue if you run into any problems using the module.

☕ Support the Project
<a href="https://www.buymeacoffee.com/muddasirrob" target="_blank"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-black.png" alt="Buy Me A Coffee" height="45" width="163" > </a>
📧 Contact
Author: Muddasir Rob

Email: muddasirrob@gmail.com

Happy Coding ♥️
vbnet
Copy
Edit

If you’d like a downloadable `README.md` file or want me to generate the `datascraper` package structure to match this documentation, just let me know!








Ask ChatGPT
