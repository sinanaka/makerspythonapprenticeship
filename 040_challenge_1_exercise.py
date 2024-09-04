# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  # Get 10 characters long words
  long_words = extract_long_words_than_10(words)
  # Remove words those contains hyphens
  long_words_without_hpyhens = reject_words_contain_hypens(long_words)
  # Map the ones contains more than 15 characters
  # with adding elipsis
  shorten_if_long_15 = shorten_very_long_words(long_words_without_hpyhens)
    # Summarizind of the strings
  return format_long_word_report(shorten_if_long_15)

def extract_long_words_than_10(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words
 
def reject_words_contain_hypens(words):
  unhypheneted_words = []
  for word in words:
    if "-" not in word:
      unhypheneted_words.append(word)
  return unhypheneted_words

def shorten_very_long_words(words):
  prechecked_words = []
  for word in words:
    if len(word) > 15:
      shortened_word = word [0:15] + "..."
      prechecked_words.append(shortened_word)
    else:
      prechecked_words.append(word)
  return prechecked_words
def format_long_word_report(long_words):
  report = "These words are quite long: "
  return report + ", ".join(long_words)
    
check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
