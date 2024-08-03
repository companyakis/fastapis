from pydantic import BaseModel, field_validator 
from typing import List 

class Director(BaseModel):
    name: str
    id: int
    divisions: List[str]
    
    # field validation
    # let's create a rule
    # let' restrict number of the divisions managed by each director
    
    @field_validator("divisions")
    @classmethod
    def validate_divisions(cls, control_list: List[str]):
        if len(control_list) > 5 or len(control_list) < 3:
            raise ValueError("Number of divisions must be between 3 and 5 (3 or 4 or 5)!")
        return control_list    
    
# director_mustafa = Director(
#     name = "Mustafa Büyükdereli",
#     id = 101,
#     divisions = ["FinTech", "Finance", "Accounting"]
# )

director_mustafa = {
    "name" : "Mustafa Büyükdereli",
    "id": 101,
    "divisions": ["FinTech", "Finance"],
}

director1 = Director(**director_mustafa)

print(director1) # Value error, Number of divisions must be between 3 and 5 (3 or 4 or 5)!

