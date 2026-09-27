import re

csproj_path = "source_code/bảo  sâm nuôi nick lol/FastBoxPhone.csproj"

with open(csproj_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the resource tag to include logical name
old_resource = '<Resource Include="testTuongTacWPF\\Images\\anime_bg.jpg" />'
new_resource = '<Resource Include="testTuongTacWPF\\Images\\anime_bg.jpg" LogicalName="Images/anime_bg.jpg" />'

content = content.replace(old_resource, new_resource)

with open(csproj_path, "w", encoding="utf-8") as f:
    f.write(content)
