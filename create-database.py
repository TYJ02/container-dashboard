import sqlite3

con = sqlite3.connect('database-demo.db')
cur = con.cursor()


def create_table():
# when writing in python sqlite3, we omit semicolon
    cur.execute("CREATE TABLE Containers ( container_id VARCHAR(50) PRIMARY KEY, iso TEXT NOT NULL );")
    cur.execute("CREATE TABLE Damages ( damage_id INTEGER PRIMARY KEY AUTOINCREMENT, container_id VARCHAR(50), timestamp TEXT NOT NULL, damage_type VARCHAR(100), location TEXT NOT NULL, FOREIGN KEY (container_id) REFERENCES Containers(container_id));")
    cur.execute("CREATE TABLE Inspection ( inspect_id INTEGER PRIMARY KEY AUTOINCREMENT, container_id VARCHAR(50), timestamp TEXT NOT NULL, img_path TEXT NOT NULL, FOREIGN KEY (container_id) REFERENCES Containers(container_id));")
    con.commit()
'''
CREATE TABLE Inspection ( inspect_id INTEGER PRIMARY KEY AUTOINCREMENT, container_id VARCHAR(50), timestamp TEXT NOT NULL, img_path TEXT NOT NULL, FOREIGN KEY (container_id) REFERENCES Containers(container_id));
CREATE TABLE DamageSummary(
container_id VARCHAR(50) PRIMARY KEY,
total_damages DECIMAL(10,2),
total_damage_count INTEGER,
FOREIGN KEY (container_id) REFERENCES Containers(container_id)
);
'''

def add_id_demo(data):
    cur.executemany("INSERT INTO Containers (container_id, iso) VALUES (?,?)", data)
    con.commit()

def add_id():
    cur.execute("INSERT INTO Containers (container_id) VALUES ('IAAU1718635'),('AXEU6000191'),('BHCU5000265'),('NLLU4223960'),('OOCU7342259'),('TCNU6215064'),('TGBU7713246');")
    con.commit()


def add_damage(data):
    cur.executemany("INSERT INTO Damages (container_id, timestamp, damage_type, location) VALUES (?,?,?,?)", data)
    con.commit()

def add_inspect(data):
    cur.executemany("INSERT INTO Inspection (container_id, timestamp, img_path) VALUES (?,?,?)", data)
    con.commit()

if __name__ == "__main__":
    data = [("TCNU6215064", "45G1"), ("TCNU2558065", "45G1")]
    #create_table()
    add_id_demo(data)
