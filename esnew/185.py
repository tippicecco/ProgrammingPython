#[print(x) for x in "This is my string" if (x != 's' and x != ' ')]
[x for x in "This is my string"]

nums = [i for i in range(1,1001)]
string ="Stringa per l'esercizio pratico di list comprehension."
#print((len(string)))
#div_8 = [item for item in nums if item % 8 == 0]
#print(div_8)
#list_6 = [item for item in nums if item % 10 == 6]
#print(list_6)

#nspazi = [item for item in string if item == " " ]
#print(str(len(nspazi)) + " spazi")
#vocali = "aeiou"
#string = [item for item in string if item not in vocali ]
#deli=""
#string = deli.join(string)

#for x in range(len(vocali)):
   # string = string.replace(vocali[x],"")
string = string.split(" ")
parole5 = [item for item in string if len(item) < 5]
print(parole5)

num1 = [ item for item in nums for i in range(2,10)  if item % i if i != 10  ]
print(num1)

#for item in nums:
 # divisore = False
  #for i in range(2,9):
   # if item % i == 0 :
    #  divisore = True
  #if divisore:
   # print(item)

