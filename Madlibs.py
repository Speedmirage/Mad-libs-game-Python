import time

"""
This programs takes the form of a Mad Libs game. You will have to enter several words to bring a pre-set story line to life in your own way. Have fun & Enjoy
"""
print "***The Mab Libs game by Addiel A. has been initialized..."

time.sleep(1)

mainchar =  raw_input("Please name our main character ")

print "***Now you'll be asked to enter three different adjetives to descrive our main character"

adjetive1 =  raw_input("Please input the first adjective ")
adjetive2 =  raw_input("Please input the second adjetive ")
adjetive3 =  raw_input("Please input the third and final adjetive ")

print "***Now, please kindly input three verbs"

verb1 = raw_input("Please input the first verb ")
verb2 = raw_input("Please input the second verb ")
verb3 = raw_input("please input the final verb ")

print "***Now, please enter four nouns"

noun1 = raw_input("Please input the first noun ")
noun2 = raw_input("Please input the second noun ")
noun3 = raw_input("please input the third noun ")
noun4 = raw_input("Please input the final noun ")

print "***Now, please answer a couple of weird, but fun statements"
animal = raw_input("Please input an animal ")
food =  raw_input("Please input a type of food ")
fruit =  raw_input("Please input a type of fruit ")
number = raw_input("Please input a random number ")
superhero =  raw_input("Please input the name of a superhero ")
country = raw_input("Please input the name of a random nation state ")
dessert = raw_input("Please enter a random dessert ")
year =  raw_input("Please enter a year ")

#BackBone of your story
STORY = """"This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. 
On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym 
of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s 
quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep 
and woke up in the year %s, in a world where %ss ruled the world."""
print " "
print STORY % (adjetive1, mainchar,verb1,adjetive2,noun1,noun2,animal,food,verb2,noun3,fruit,adjetive3,mainchar,
verb3,number,mainchar,superhero,superhero,mainchar,country,mainchar,dessert,mainchar,year,noun4)

