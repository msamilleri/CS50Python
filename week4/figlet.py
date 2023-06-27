import pyfiglet
import sys
def main():
  print_with_pyfiglet()

def print_with_pyfiglet():
  font = input()
  font_new=font.startswith('-f')
  if font_new:
    font = font.strip('-f ')
    text = input("Input:")
    figlet_text = pyfiglet.figlet_format(text, font=font)
    print(figlet_text)
  else:
    sys.exit('Invalid usage')

main()