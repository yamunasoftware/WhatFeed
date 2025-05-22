# WhatFeed

News Feed Automation, in Python

## Information

This is a simple application that loads the news headings from the BBC, which is considered a leading neutral news publication. Next, the application splits the news headings into syntactical elements and the application cleans those syntax elements to remove punctuation and stop words. Then, the application uses a hierarchical clustering algorithm to develop a similarity matrix, which we then use to index the news headings to develop a summary. Then, using the similarity matrix indices, we group the sentences into a contextual summary of breaking news and headings. The final summary is saved in the ```report.txt``` file for easy viewing of the news summary, after removing junk headings artifacts. Lastly, the application generates a plot of sample words and their counts and saves it to the ```words.png``` file.