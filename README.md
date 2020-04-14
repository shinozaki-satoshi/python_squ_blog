# python_squ_blog

this is a program that conbinaes specialized scraping with SQL

# DEMO
 I analyzed assuming that blog comments are proportional to popularity.

1.scraping blog site
2.obtain links for menbers who belong to this site
3.get the last five names and comments from there
4.write to a text file as a SQL command
5.run file ,"source (textfile)"

+a:sort by SQL

-----------Details---------------
command(in sql server and use someone database:"mysql> " this condition)
1.sorce test0.txt
2.sorce test.txt
(you should handle the files with drugs)

3.bring down
SELECT*FROM comments
ORDER BY countCome DESC;
# Features

specialized programs for this web page
apply to SQL for data utilization


# Requirement

*requests
*from bs4 import BeautifulSoup
*from urllib.parse import urljoin
*import time,re

# Installation

pip3 install requests
pip install beautifulsoup4

# Usage

python squ_sql_txt.py

(sql)
source ./text.txt

# Note

Although I set pause timeout of three seconds per page, you have to take time to avoid over-access.
I am unwilling to put a load on thier server.

# Author


* Shinozaki Satoshi
* Shibaura institute of Technology
* shinozakisatoshi0706@gmail.com

# License

this is not Confidential.
