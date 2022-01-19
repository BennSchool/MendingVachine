import time, os, sys, colorama
with open('receipt.txt', 'w') as f:
    f.write('---RECEIPT---')
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
scrollSpeed = 0
def scrollTxt(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(scrollSpeed)
scrollTxt("Welcome to Vend Inc. Vending Machine \n" + colorama.Fore.RED + "(by Benneasy)" + colorama.Fore.RESET)
time.sleep(5)
clearConsole()
items = [["A1", "Crisps - Plain", "1", 1], ["A2", "Crisps - Not Plain", "1", 1]]
i = 0
scrollTxt("Welcome! Here are our options \n")
while i < len(items):
  print(items[i][0] + " - " + items[i][1] + " - £" + items[i][2])
  i += 1
while True:
  scrollTxt("What would you like? (Please input the alphanumerical code)\n")
  want = input("")
  if want == items[0][0]:
    with open('receipt.txt', 'a') as f:
      f.write('\n' + items[0][1] + " - £" + items[0][2])
    scrollTxt("Thank you!")
  elif want == items[1][0]:
    with open('receipt.txt', 'a') as f:
      f.write('\n' + items[1][1] + " - £" + items[1][2])
    scrollTxt("Thank you!\n")
  else:
    scrollTxt("Invalid!\n")
    continue
  wan2 = input("\nAnything else? (y/n)\n")
  if wan2 == "y":
    scrollTxt("Ok!")
    clearConsole()
    continue
  elif wan2 == "n":
    break
  else:
    scrollTxt("Invalid! Exiting...\n")
    time.sleep(3)
    break
scrollTxt("Goodbye!")