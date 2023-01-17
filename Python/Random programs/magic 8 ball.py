import random
import time

Answer_list = ['Go for it', 'No way', 'come again', 'some bull crap about fear', 'Its up to u man', 'Dont ask me, IDK', 'no dont do it', 'only you can save him', "I don't care", 'yes do it', "It is certain", "It is decidedly so", "I can't answer that"]
password=2345
AnswerPrev=1
x='225221'
while x!=password:

    q = input("WHAT IS YOUR QUESTION")

    time.sleep(0.3)
    Nextanswer=random.choice(Answer_list)
    
    if AnswerPrev!=Nextanswer:
        print("  -", Nextanswer)
        AnswerPrev=Nextanswer

    else:
        print("  -", random.choice(Answer_list))



    
  
