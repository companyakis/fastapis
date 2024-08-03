from pydantic import BaseModel, field_validator 
from typing import List 

class Director(BaseModel):
    name: str
    id: int
    divisions: List[str]
    
    @field_validator("divisions")
    @classmethod
    def validate_divisions(cls, control_list: List[str]):
        if len(control_list) > 5 or len(control_list) < 3:
            raise ValueError("Number of divisions must be between 3 and 5 (3 or 4 or 5)!")
        return control_list    
    
# add assignment control (before) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Look at the final result !!!!!!!!!!!!!!!

director_mustafa = {
    "name" : "Mustafa Büyükdereli",
    "id": 101,
    "divisions": ["FinTech", "Finance", "Accounting"],
    "countries": [
        {"country_name": "Germany", "active": True},
        {"country_name": "Canada", "active": False}
    ]
}

director1 = Director(**director_mustafa)

director1.name = "Mustafa Deleted"

print(director1) # name='Mustafa Deleted' id=101 divisions=['FinTech', 'Finance', 'Accounting']
