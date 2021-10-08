#TP1_YEO TIEDJO NADEGE_ATTOUMBRE KOUADIO JUVENAL
#Partie 2.2 
liste = [
    (i, j)
    for i in range(5)
    for j in 'pays'
]
print(liste)
dictionnaire= {}
for key, value in liste:
    if key in dictionnaire:
        dictionnaire[key]=dictionnaire[key]+value
    else:
     dictionnaire[key] = value
print(dictionnaire)
print('ou une seconde maniere de faire')
dictionnaire= {}
val=[]
for key, value in liste:
    if key in dictionnaire:
        val.append(dictionnaire[key])
        val.append(value)
        dictionnaire[key] = val
        val=[]
    else:
     dictionnaire[key] = value
print(dictionnaire)


#dicts = {}
#keys = [1,2,1,4]
#values = ["Hi", "I", "am", "John"]
#j=0
#val=[]
#for i in keys:
 #   if i in dicts:
  #      val.append(values[j])
   #     j+=1
    #else:
     #   dicts[i]=values[j]
      #  j+=1

#print(dicts)
#print(val)