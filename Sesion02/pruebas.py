from logging import raiseExceptions


data =[ {
    "dni" : "40085122",
    "nombre" : "JULIO",
},
{
    "dni" : "40085123",
    "nombre" : "MARCOS",
},
{
    "dni" : "40085124",
    "nombre" : "MARIA",
    }
]


z = 0
for x in data:
 
    print(x["dni"])
    z = z + 1  
    if  x["dni"] == "40085123":
     
      #print ("hallado", z-1 )
      print(data[z-1])  
      break

    
