print ("welcome to my computer quiz!")

playing = input("Are you ready? Y/N: ")
if playing != "Y" :
    quit()
print ("START")
score=0;
answer = input("1. What nut is used to make marzipan? ")
if answer == "Almonds" or "almonds" or "ALMONDS":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("2. What's the name of the river that runs through Egypt? ")
if answer == "Nile" or "nile" or " NILE" or " The Nile" or "the nile" or "THE NILE" :
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("3. What is Sweden's capital city? ")
if answer == "Stockholm" or "stockholm" or "STOCKHOLM":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("4. What's the highest mountain in the world? ")
if answer == "Mount everest" or "Mount Everest" or "mount everest" or "Everest" or "everest" :
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("5. What is the capital of Argentina? ")
if answer.lower() == "Buenos Aires" or "Buenos aires" or "buenos aires" or "BUENOS AIRES":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("6. What is the currency of poland? ")
if answer == "Zloty" or "zloty" or "ZLOTY":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("7. Which english city is known as the steel city? ")
if answer == "Sheffield" or "SHEFFIELD" or "sheffield" :
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("8. The logo of Porsche car features which animal? ")
if answer == "Horse" or "horse" or "HORSE":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("9. From which grain is the Japanese spirit sake made? ")
if answer == "Rice" or "rice" or "RICE" :
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

    
answer = input("10. Which is the smallest planet in the solar system? ")
if answer == "Mercury" or "mercury" or "MERCURY":
    print ("Correct")
    score+=1;
else:
    print ("Incorrect")

print ("Score: " + str(score))
