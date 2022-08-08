d1 = {}
print(type(d1))
d2 = {"Name": "Feroz",
      "Department": "CSE",
      "ID": "256",
      "Mohan": {"B": "Food", "L": "Drinks", "D": "JunkFood"}}
d2["Saiteja"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2["Mohan"])
d3 = d2.copy()
d2.update({"ID": 255})
print(d2.keys())
print(d2.items())
