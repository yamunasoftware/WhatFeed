import similarity
import scrape

### SUMMARIZATION FUNCTIONS ###

# Pair Words:
def pair_words(words, counts, data):
  paired_words = []
  for entry in data:
    index = counts.index(entry)
    paired_words.append(words[index])
  return paired_words

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
  summary = ''
  paired_matrix = summarization_processing(data)
  index = 1

  for item in paired_matrix:
    if index == 1:
      summary = summary + 'Breaking News:\n\n'
    else:
      summary = summary + 'Heading ' + str(index) + ':\n\n'

    for element in item:
      for sentence in combined:
        if element in sentence.lower().split(' ') and sentence not in summary:
          summary = summary + sentence + '\n'
    if index < len(paired_matrix):
      summary = summary + '\n\n'
    index += 1
  return summary

final, combined = scrape.run_scraping()
print(summarize_news(final, combined))