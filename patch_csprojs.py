import re
import os

csproj_path = "source_code/bảo  sâm nuôi nick lol/FastBoxPhone.csproj"

with open(csproj_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure Images are included
if "<ItemGroup>" in content and "testTuongTacWPF/Images/anime_bg.jpg" not in content:
    images_item_group = '''
  <ItemGroup>
    <Resource Include="testTuongTacWPF\\Images\\anime_bg.jpg" />
  </ItemGroup>
  <ItemGroup>'''
    content = content.replace("  <ItemGroup>", images_item_group, 1)

    with open(csproj_path, "w", encoding="utf-8") as f:
        f.write(content)
