import os
import urllib.request

if not os.path.exists("the-verdict.txt"):
  url = ("https://raw.githubusercontent.com/Blackstorm-619/LLM_from_scratch/refs/heads/AD/01_tokenization/the-verdict.txt")
  file_path = "the-verdict.txt"
  urllib.request.urlretrieve(url, file_path)

with open ("the-verdict.txt", "r", encoding="utf-8") as f:
  raw_text = f.read()

import re
result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
result = [item.strip() for item in result if item.strip()]
print(result)
