#               KEYWORD ARGUMENT & DEFAULT ARGUMENT
def function(name="guest"):
    print("name=",name)

function()
function("omkar")


#               PASSING A FUNCTION TO ANOTHER FUNCTION

def hello():
    print("sunbeam infotech private limited")

def function(nxt):
   nxt()

function(hello)