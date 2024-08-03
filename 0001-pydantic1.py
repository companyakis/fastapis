from pydantic import BaseModel 
from typing import List 

class Director(BaseModel):
    name: str
    id: int
    divisions: List[str]
    
director_mustafa = Director(
    name = "Mustafa Büyükdereli",
    id = 101,
    divisions = ["FinTech", "Finance", "Accounting"]
)

print(director_mustafa) # name='Mustafa Büyükdereli' id=101 divisions=['FinTech', 'Finance', 'Accounting']
print(director_mustafa.name) # Mustafa Büyükdereli
print(director_mustafa.divisions[0]) # FinTech
