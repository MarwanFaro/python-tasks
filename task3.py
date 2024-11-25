import random

tries = 5
words=["String","double","bool","int","float","char"]
selcted_word= random.choice(words)
scrambld_word= ''.join(random.sample(selcted_word,len(selcted_word)))
while tries>0:
 print(scrambld_word)
 gusse =input("enter the gusse: ")
 if gusse == selcted_word:
  print("congrates you won")
  break
 else:
  tries-=1
  print(f"tries left {tries}")

if tries==0: 
 print ("the correcte answer is : ",selcted_word)


  