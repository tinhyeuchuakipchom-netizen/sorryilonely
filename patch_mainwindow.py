import re

with open("source_code/bảo  sâm nuôi nick lol/testTuongTacWPF/MainWindow.xaml", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Background
content = re.sub(
    r'Background="\{DynamicResource BrushWindowBg\}"',
    r'''Background="White"''',
    content,
    count=1
)

# Add Window.Background ImageBrush and Window.Triggers for animation
animation_xaml = '''
  <Window.Background>
    <ImageBrush ImageSource="/Images/anime_bg.jpg" Stretch="UniformToFill" Opacity="0.9"/>
  </Window.Background>
  <Window.Triggers>
    <EventTrigger RoutedEvent="Window.Loaded">
      <BeginStoryboard>
        <Storyboard>
          <DoubleAnimation Storyboard.TargetProperty="Opacity" From="0.0" To="1.0" Duration="0:0:1"/>
        </Storyboard>
      </BeginStoryboard>
    </EventTrigger>
  </Window.Triggers>
  <shell:WindowChrome.WindowChrome>
'''

content = content.replace('  <shell:WindowChrome.WindowChrome>', animation_xaml, 1)

with open("source_code/bảo  sâm nuôi nick lol/testTuongTacWPF/MainWindow.xaml", "w", encoding="utf-8") as f:
    f.write(content)
