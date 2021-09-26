# Author: SMR (AMDG) 09/26/21
free_throw=int(input("How many free throws were made?"))
regular_shot=int(input("How many regular shots were made?"))
three_point=int(input("How many three pointers were made?"))
an1=free_throw
an2=(regular_shot*2)
an3=(three_point*3)
final=an1+an2+an3
print("The player scored",final,"points in the game.")
