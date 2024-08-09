import pandas as pd

# list = [image, id, damage count, type 1, type 2, rating]

item1 = [["20240806", "10101.jpg", 10101, 2, 1, 1, 84],
         ["20240806","10102.jpg", 10102, 2, 1, 1, 60]
         ]

column_names = ["timestamp", 'image', 'id', 'count', 'axis', 'concave', 'rating']

data = pd.DataFrame(data=item1, columns = column_names)

data.to_csv("container.csv", index= False)
            
print(data)
