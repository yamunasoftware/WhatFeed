### REPORTING IMPORTS ###

import similarity
import scrape

from datetime import date
import matplotlib.pyplot as plt

### REPORTING HELPER FUNCTIONS ###

# Bad Phrases:
stop_phrases = [
  'Latest on the',
  'Sign up'
]

# Pair Words:
def pair_words(words, counts, data):
  paired_words = []
  for entry in data:
    index = counts.index(entry)
    paired_words.append(words[index])
  return paired_words

# Remove Bad Headings:
def remove_bad_headings(combined):
  processed_sentences = []
  present = False

  for sentence in combined:
    present = False

    for phrase in stop_phrases:
      if phrase in sentence:
        present = True
    
    if present == False:
      processed_sentences.append(sentence)
  return processed_sentences

### REPORTING FUNCTIONS ###

# Visualize Cluster Matrix:
def visualize_cluster_matrix(paired_matrix):
  words = []
  counts = []
  i = len(paired_matrix)
  
  for list in paired_matrix:
    words.append(list[0])
    counts.append(i)  
    i -= 1
  
  plt.figure(figsize=(10,5))
  plt.bar(words, counts, width=0.1)
  plt.xlabel('Words')
  plt.ylabel('Counts')
  plt.title('Sample of Words and Occurrences')
  plt.show()

# Summarization Processing:
def summarization_processing(data):
  words, counts = similarity.vectorization(data)
  track, occurrences = similarity.vector_counts(counts)
  matrix = similarity.combine_vectors(track, occurrences)

  if matrix != []:
    clusters, final_counts = similarity.cluster(matrix)
    indices = similarity.index_order(final_counts)
    paired_matrix = []
    
    for index in indices:
      paired_words = pair_words(words, counts, clusters[index])
      paired_matrix.append(paired_words)
    return paired_matrix
  else:
    return None
    
# Summarize News:
def summarize_news(data, combined):
  today_date = str(date.today())
  summary = 'News Report for ' + today_date + ':\n\n'

  paired_matrix = summarization_processing(data)
  processed_sentences = remove_bad_headings(combined)
  index = 1

  for item in paired_matrix:
    if index == 1:
      summary = summary + 'Breaking News:\n\n'
    else:
      summary = summary + 'News Index ' + str(index) + ':\n\n'

    for element in item:
      for sentence in processed_sentences:
        if element in sentence.lower().split(' ') and sentence not in summary:
          summary = summary + sentence + '\n'
    if index < len(paired_matrix):
      summary = summary + '\n\n'
    index += 1
  return summary, paired_matrix

# Output News Report to File:
def output_report(news):
  with open('report.txt', 'w') as report:
    report.write(news)

### SUMMARIZATION RUNNING ###

# Runs the Report:
final, combined = scrape.run_scraping()
summary, paired_matrix = summarize_news(final, combined)

# Outputs the Report:
output_report(summary)
visualize_cluster_matrix(paired_matrix)