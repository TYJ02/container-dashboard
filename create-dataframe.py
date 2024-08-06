import pandas as pd

# list = [image, id, damage count, type 1, type 2, rating]

item1 = [["image.png", 10101, 2, 1, 1, 84]]

column_names = ['image', 'id', 'count', 'axis', 'concave', 'rating']

data = pd.DataFrame(data=item1, columns = column_names)

data.to_csv("container.csv")
            
print(data)
