# save the model

joblib.dump(model, "simple_reg_model")

# load the model

simple_reg = joblib.load("simple_reg_model")

print(simple_reg.coef_)

print(simple_reg.predict([[10]]))

"""
[0.02602589]

[4.72968879]
"""
