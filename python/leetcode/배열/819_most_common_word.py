import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL Flew far after it was hit."
banned = ["hit"]
print(Counter([s for s in re.sub("[^\w]", " ",paragraph).lower().split() if s not in banned]).most_common(1)[0][0])