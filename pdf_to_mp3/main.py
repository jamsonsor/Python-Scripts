import objc
from pypdf import PdfReader
from gtts import gTTS


pdfreader = PdfReader("flask-intro.pdf")

for page_num in range(len(pdfreader.pages)):
  text = pdfreader.pages[page_num].extract_text()
  clean_text = text.strip().replace('\n', '')
  print(clean_text)

tts = gTTS(text=clean_text)
tts.save("output.mp3")
