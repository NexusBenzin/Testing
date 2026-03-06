import Functions

# Variables and Data Types
float = 0.1
integer = 1
string = "Hello World"
boolean = True

list = [1,2,3,4,5]   # ideally should not have miss-matched data types

dictionary = {"a": 1,
              "b": True,
              "c": 0.1,
              "d": "Hello World",
}

# Conditions
y = "bbb"
x = "aaa"

if x == "aaa":
    print("x equals aaa")
else:
    print("x does not equal aaa")


if x == "aaa" and y == "bbb":
    print("x equals aaa and y  equals bbb")
else:
    print("either x does not equal aaa or y does not equal bbb")



# Cycles

books = [{"Name": "Benzin"},
         {"Name": "Diesel is BLEUGH"}
]

#for book in books:


for i in range(10):
    print(i)

#time.sleep(5)
#while True:
#    print("While True: cycle")


# Functions


Functions.sum(1, 2)