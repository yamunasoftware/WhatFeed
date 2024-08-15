### PROCESSING SETUP ###

# Import String Items:
import string

# Python array of English letters, number digits, currency symbols, and punctuation marks:
characters = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  '$', '€', '£', '¥', '₹', '₽', '¢', '₩', '₪', '₫',
  '.', ',', '!', '?', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '-', '_', '+', '=', '*', '/', '\\', '|', '<', '>', '@', '#', '%', '^', '&', '`', '~'
]

# Removal Sets:
punctuation = list(string.punctuation)
stops = set([
  'after','the', 'a', 'an', 'i', 'he', 'she', 'they', 'to', 'of', 'it', 'from', 's', 'is', 'in', 'on', 'with', 'for', 
  'how', 'as', 'at', 'be', 'have', 'has', 'had', 'and', 'are', 'by', 'says', 'over', 'us', 'can', 'what', 'why', 'about',
  'where', 'around', 'up'
])

### PROCESSING FUNCTIONS ###

# Clean Sentence Matrix:
def clean_sentences(sentences):
  punctuation_sentences = [removal(sentence, punctuation) for sentence in sentences]
  lowercase_sentences = [sentence.lower() for sentence in punctuation_sentences]

  split_sentences = [sentence.split() for sentence in lowercase_sentences]
  processed_sentences = [" ".join(list(filter(lambda a: a not in stops, sentence))) for sentence in split_sentences]
  unique_sentences = remove_duplicates(processed_sentences)

  flattened_sentences = flatten_sentences(unique_sentences)
  delimited_sentences = flattened_sentences.split(' ')[:-1]
  return delimited_sentences

# Combine All Tokens:
def combine_all_tokens(sentences):
  new_sentences = []
  for sentence in sentences:
    new_sentences.append(combine_tokens(sentence))
  return new_sentences

# Combine Tokens:
def combine_tokens(tokens):
  sentence = ''
  for token in tokens:
    sentence = sentence + ' ' + token
  return sentence

# Filter News:
def filter_news(data, token_count):
  headings = []
  for entry in data:
    if len(entry) > token_count:
      headings.append(entry)
  return headings

# Delimit Heading Data:
def delimit(data):
  delimited_data = []
  for entry in data:
    tokens = entry.split(' ')
    no_empty = remove_empty_tokens(tokens)
    chars = remove_non_text(no_empty)
    delimited_data.append(chars)
  return delimited_data

### PROCESSING HELPER FUNCTIONS ###

# Character Removal:
def removal(array, set):
  local_array = array
  for item in set:
    local_array = local_array.replace(item, ' ')
  return local_array

# Flatten Sentences:
def flatten_sentences(sentences):
  flattened = ''
  for sentence in sentences:
    flattened = flattened + sentence + ' '
  return flattened

# Remove Duplicate Sentences:
def remove_duplicates(sentences):
  unique_sentences = []
  for sentence in sentences:
    if sentence not in unique_sentences:
      unique_sentences.append(sentence)
  return unique_sentences

# Remove Empty Tokens:
def remove_empty_tokens(tokens):
  new_tokens = []
  for token in tokens:
    if token != '':
      new_tokens.append(token)
  return new_tokens

# Remove Non-Text Items:
def remove_non_text(tokens):
  new_tokens = []
  for token in tokens:
    new_token = ''
    for character in token:
      if character in characters:
        new_token = new_token + character
    new_tokens.append(new_token)
  return new_tokens