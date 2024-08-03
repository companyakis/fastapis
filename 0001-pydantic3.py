from pydantic import BaseModel 
from typing import List 

class Director(BaseModel):
    name: str
    id: int
    divisions: List[str]
    
# director_mustafa = Director(
#     name = "Mustafa Büyükdereli",
#     id = 101,
#     divisions = ["FinTech", "Finance", "Accounting"]
# )

director_mustafa = {
    "name" : "Mustafa Büyükdereli",
    "id": 101,
    "divisions": ["FinTech", "Finance", "Accounting"],
    "birth_year": 1917 # add a new field => !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}

director1 = Director(**director_mustafa)

print(director1) #name='Mustafa Büyükdereli' id=101 divisions=['FinTech', 'Finance', 'Accounting']

