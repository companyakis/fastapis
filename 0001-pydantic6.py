from pydantic import BaseModel, field_validator, ConfigDict
from typing import List 

class Director(BaseModel):
    name: str
    id: int
    divisions: List[str]
    
    # add assignment control 
    model_config = ConfigDict(validate_assignment = True)
    
    @field_validator("divisions")
    @classmethod
    def validate_divisions(cls, control_list: List[str]):
        if len(control_list) > 5 or len(control_list) < 3:
            raise ValueError("Number of divisions must be between 3 and 5 (3 or 4 or 5)!")
        return control_list    
    
director_mustafa = {
    "name" : "Mustafa Büyükdereli",
    "id": 101,
    "divisions": ["FinTech", "Finance", "Accounting"],
}

director1 = Director(**director_mustafa)

director1.name = 2024

print(director1) # Input should be a valid string [type=string_type, input_value=2024, input_type=int]
