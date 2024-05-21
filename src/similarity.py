### SIMILARITY FUNCTIONS ###

# Index Order:
def index_order(counts):
  local_counts = counts
  indices = []
  i = 0

  while i < len(counts):
    value, index = find_largest_index(local_counts)
    local_counts = remove_index(local_counts, index)
    indices.append(counts.index(value))
    i += 1
  return indices

# Find Largest Index:
def find_largest_index(counts):
  value = 0
  index = 0
  
  i = 0
  while i < len(counts):
    if i == 0:
      value = counts[i]
      index = i
    elif counts[i] > value:
      value = counts[i]
      index = i
    i += 1
  return value, index

# Remove Index:
def remove_index(array, index):
  local_array = []
  i = 0
  
  while i < len(array):
    if i != index:
      local_array.append(array[i])
    i += 1
  return local_array

# Cluster Vectors:
def cluster(data):
  clusters = []
  counts = []

  for entry in data:
    if entry[1] not in counts:
      counts.append(entry[1])
      clusters.append([entry[0]])
    else:
      index = counts.index(entry[1])
      clusters[index].append(entry[0])
  return clusters, counts

# Combine Vectors:
def combine_vectors(track, occurrences):
  matrix = []
  if len(track) == len(occurrences):
    i = 0
    while i < len(track):
      local_array = [track[i], occurrences[i]]
      matrix.append(local_array)
      i += 1
  return matrix

# Vector Counts:
def vector_counts(counts):
  track = []
  occurrences = []
  for count in counts:
    local_count = 0
    if count not in track:
      track.append(count)
      for element in counts:
        if element == count:
          local_count += 1
      occurrences.append(local_count)
  return track, occurrences

# Vectorization Function:
def vectorization(data):
  counts = []
  words = []
  i = 1

  for entry in data:
    if entry not in words:
      words.append(entry)
      counts.append(i)
      i += 1
    else:
      index = words.index(entry)
      words.append(entry)
      counts.append(counts[index])
  return words, counts