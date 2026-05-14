import re

file_path = 'c:/Projects/Brother_Kitchen_website/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The FAQs
faqs = [
    "We typically deliver lunch between 12:30 PM and 2:00 PM. Please place your order early for timely delivery.",
    "Yes, we offer weekly and monthly subscription plans for regular meals. Contact us on WhatsApp for pricing and details.",
    "Yes, all our meals are 100% pure vegetarian and homestyle cooked in a dedicated vegetarian kitchen.",
    "Yes, our menu changes daily to provide a variety of fresh, home-cooked meals."
]

# We need to replace the content of the remaining 4 accordion bodies.
# The accordion body content is currently:
# "Yes. It adheres to the WAI-ARIA design pattern."
# "Yes. It comes with default styles that matches the other components\' aesthetic."
# "Yes. It\'s animated by default, but you can disable it if you prefer."
# Wait, let's just use regex to replace them.
# The original text was:
orig_texts = [
    "Yes. It comes with default styles that matches the other components&#x27; aesthetic.",
    "Yes. It&#x27;s animated by default, but you can disable it if you prefer.",
    "Yes. It&#x27;s animated by default, but you can disable it if you prefer.", # Wait, the last two were the same? I will just use regex to match the exact div content.
]

# Let's find all instances of `<div class="pb-4 pt-0 text-[#4A5D54] leading-relaxed">`
# and replace their inner text.
parts = content.split('<div class="pb-4 pt-0 text-[#4A5D54] leading-relaxed">')
if len(parts) == 6: # 1 before first, 5 after
    # first one was already replaced by me successfully!
    # so parts[2], parts[3], parts[4], parts[5] need replacement
    for i in range(2, 6):
        # find the end of the text
        end_idx = parts[i].find('</div>')
        parts[i] = '\n                    ' + faqs[i-2] + '\n                  ' + parts[i][end_idx:]

    new_content = '<div class="pb-4 pt-0 text-[#4A5D54] leading-relaxed">'.join(parts)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success replacing faqs")
else:
    print(f"Error: expected 6 parts, got {len(parts)}")

