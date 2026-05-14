import re

file_path = 'c:/Projects/Brother_Kitchen_website/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('Questions aria-controls:')
qs = re.findall(r'<button[^>]*aria-controls="(radix-_r_[^"]*)"', text)
for q in qs:
    print(q)

print('Answers ids:')
ans = re.findall(r'<div data-state="(?:open|closed)" id="(radix-_r_[^"]*)"', text)
for a in ans:
    print(a)
