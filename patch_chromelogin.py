import re

filepath = "source_code/bảo  sâm nuôi nick lol/testTuongTacWPF/Automation/ChromeLoginRunner.cs"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Enhance login fallback to Cookie if Cookie exists but login fails or type is UidPass but has cookie.
# We will just make sure it's robust. The current ChromeLoginRunner already supports Cookie and CookieThenUidPass.
# Let's ensure if UidPass is selected but it fails, it tries Cookie if cookie is present as a fallback.

pattern = r'if \(P_1\.LoginType == "Cookie" \|\| \(\(P_1\.LoginType == "CookieThenUidPass"\) & flag\)\)'
replacement = r'if (P_1.LoginType == "Cookie" || ((P_1.LoginType == "CookieThenUidPass" || P_1.LoginType == "UidPass") && flag))'

content = re.sub(pattern, replacement, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
