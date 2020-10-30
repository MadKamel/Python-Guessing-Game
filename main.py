import sys, os, random
os.system('clear')

countries = ["czechoslovakia", "switzerland", "great britain", "france", "canada", "poland", "ukraine", "russia", "china"]
languages = ["english", "spanish", "french", "german", "russian", "mandarin", "cantonese", "egyptian"]

print("Topic choices:")
print("  1.Nations")
print("  2.World Languages\n")
print("Make your choice below\n")
topicpick = input(" ===Number :")
if topicpick == "1":
  word = random.choice(countries)
elif topicpick == "2":
  word = random.choice(languages)
else:
  print("Invalid Option. Program Exiting.")
  exit()

os.system('clear')
print("Pick an Index and Guess the letters, type '?' for help or type '0' to guess full word\n")
length = len(word)
charlist = []
for i in range(length):
  charlist.append(word[i])
blanklist = []
chars = []
for i in range(length):
  blanklist.append('*')
charsall = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(length):
  chars.append(charsall[i])
gameover = False
msg="Nothing"
while not gameover:
  for i in range(length):
    sys.stdout.write(blanklist[i])
  print()
  for i in range(length):
    sys.stdout.write(chars[i])
  print("\n")
  choice = input(' ===Choose one :').upper()
  choice2 = input(' ===What is it :')
  msg="Not " + choice2
  if choice == "0":
    if choice2 == word:
      msg="You guessed " + choice2
      blanklist = charlist
  elif choice == "?":
    blanklist[chars.index(choice2.upper())] = charlist[chars.index(choice2.upper())]
    msg="You revealed " + charlist[chars.index(choice2.upper())]
  else:
    if charlist[chars.index(choice)] == choice2:
      msg="Good " + charlist[chars.index(choice)]
      blanklist[chars.index(choice)] = charlist[chars.index(choice)]
  os.system('clear')
  print("" + msg + "\n")
  if blanklist == charlist:
    print("\n     =======[ You Win ]======\n")
    print("The word is " + word)
    exit()
