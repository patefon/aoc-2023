INPUT_TEST = './data/day-1-test.txt'
INPUT_1 = './data/day-1-1.txt'

word2digit = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

def detect(s:str, words: bool = False) -> str:
  """ Function digit found in string

  Args:
      s (str): input string

  Returns:
      str: detected digit
  """
  sub = ''
  for c in s:
    if words:
      sub += c
      keywords = [d for d in word2digit.keys() if (d in sub) or (d[::-1] in sub)]
      if len(keywords):
        return str(word2digit[keywords[0]])
    if c.isdigit():
      return c

def solution(inp: str, words: bool = False):
  ans = 0
  with open(inp, 'r') as f:
    while True:
      line = f.readline()
      if not line:
          break
      ans += int(''.join([detect(line, words), detect(line[::-1], words)]))
  print(f'Answer {inp}: {ans}')

solution(INPUT_TEST)
solution(INPUT_1)
solution(INPUT_1, words=True)