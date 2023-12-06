from functools import reduce

INPUT_TEST = """
Time:      7  15   30
Distance:  9  40  200
"""

INPUT = """
Time:        55     82     64     90
Distance:   246   1441   1012   1111
"""

def parse_input(s: str):
  time_str, dist_str = list(filter(lambda x: x != '', s.split('\n')))
  time_str = time_str.replace('  ', ' ')
  dist_str = dist_str.replace('  ', ' ')
  times = list(filter(lambda x: x != '', map(str.strip, list(map(str.strip, time_str.split(': ')))[1].split(' '))))
  dists = list(filter(lambda x: x != '',map(str.strip, list(map(str.strip, dist_str.split(': ')))[1].split(' '))))
  return times, dists

def solution1(inp: str):

  # 1 * (7 - 1) = 6
  # 2 * (7 - 2) = 10
  # 3 * (7 - 3) = 12
  # 4 * (7 - 4) = 12
  # 5 * (7 - 5) = 10

  times, dists = parse_input(inp)
  wins = []
  for race in zip(times, dists):
    count_wins = 0
    t, d = int(race[0]), int(race[1])
    for x in range(0, t+1):
      travel_dist = x * (t - x)
      if travel_dist > d and travel_dist > 0:
        count_wins += 1
    wins.append(count_wins)
  print(reduce(lambda x, acc: acc*x, wins))

def solution2(inp: str):
  times, dists = parse_input(inp)
  # upd part 2
  times = [''.join(times)]
  dists = [''.join(dists)]
  wins = []
  for race in zip(times, dists):
    count_wins = 0
    t, d = int(race[0]), int(race[1])
    for x in range(0, t+1):
      travel_dist = x * (t - x)
      if travel_dist > d and travel_dist > 0:
        count_wins += 1
    wins.append(count_wins)
  print(reduce(lambda x, acc: acc*x, wins))

solution1(INPUT)
solution2(INPUT)
