from asyncio import streams
from unicodedata import name
import qrcode

def generation_grc(url="https://google.com", name="default"): # We point to the link to our qrc
  # Create qrc
  qrc = qrcode.make(data=url);
  # We store our qrc  
  qrc.save(stream=f"{name}.png");
  # Return information about the generation 
  return f"""
  ----------------------------------------\n
  |!| Your QRC was created!
  |!| Open this image to see {name}.png \n
  -----------------------------------------
  """;

# Out result
def main():
  # In url, you can set any link
  print(generation_grc(url="https://github.com/Roman-jx/qrc_gen", name="github"));
  print(generation_grc(url="www.linkedin.com/in/roman-malkevich-4ba663207", name="linkedin"));

if __name__ == "__main__":
  main();