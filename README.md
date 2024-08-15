# WhatFeed

News Feed Automation, in Python

## Information

This is a simple application that loads the news headings from the BBC, which is considered a leading neutral news publication. Next, the application splits the news headings into syntactical elements and the application cleans those syntax elements to remove punctuation and stop words. Then, the application uses a histogram-based clustering to develop a similarity matrix, which we then use to index the news headings to develop a summary. Then, using the similarity matrix indices, we group the sentences into a contextual summary of breaking news and headings. The final summary is saved in the ```report.txt``` file for easy viewing of the news summary, after removing junk headings artifacts. Lastly, the application generates a plot of sample words and their counts and saves it to the ```words.png``` file.

## Usage

To use the application, simple use the Bash or Batch files listed in the main directory. If you use Windows, run the batch script by running ```whatfeed.bat``` in the command prompt. If you use MacOS, Linux, or GitBash, run the following command in the terminal: ```bash whatfeed.sh```.

## Dependencies

- requests
- beautifulsoup4
- matplotlib

To install these dependencies simply run the ```pip``` commands listed below.

```
pip install requests
pip install beautifulsoup4
pip install matplotlib
```