import re 

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
result = [item.strip() for item in result if item.strip()]
print(result)
