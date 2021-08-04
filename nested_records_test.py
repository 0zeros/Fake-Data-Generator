from data_generator import *
from view import *


# first name
# full name -> fname mname lname
# card holder -> full name, card Number, CVC, date


# set parameters to generate list of First name
format = "fname"
element = ["fname"]
constraints = {"fname": {"record": "no", "type": "string", "choose": "fname list"}}

data_sets = {
    "fname list": ["JAMES","JOHN","ROBERT",'MICHAEL','WILLIAM','DAVID','RICHARD','CHARLES','JOSEPH','THOMAS','CHRISTOPHER','DANIEL','PAUL','MARK','DONALD','GEORGE','KENNETH','STEVEN','EDWARD','BRIAN','RONALD','ANTHONY','KEVIN','JASON','MATTHEW','GARY','TIMOTHY','JOSE','LARRY','JEFFREY','FRANK','SCOTT','ERIC','STEPHEN','ANDREW','RAYMOND','GREGORY','JOSHUA','JERRY','DENNIS']
}

# call generator function
data_generator("first name", 10, format, element, constraints, data_sets)


# set parameters to generate list of full name ids
format = "fname mname lname"

element = ["fname","mname","lname"]

constraints = {"fname": {"record": "yes", "name": "first name"},
               "mname": {"record": "no", "type": "string", "choose": "mname list"},
               "lname": {"record": "no", "type": "string", "choose": "lname list"}
               }

data_sets = {
    "mname list": ['WALTER','PATRICK','PETER','HAROLD','DOUGLAS','HENRY','CARL','ARTHUR','RYAN','ROGER','JOE','JUAN','JACK','ALBERT','JONATHAN','JUSTIN','TERRY','GERALD','KEITH','SAMUEL','WILLIE','RALPH','LAWRENCE','NICHOLAS','ROY','BENJAMIN','BRUCE','BRANDON','ADAM','HARRY','FRED','WAYNE','BILLY','STEVE','LOUIS','JEREMY','AARON','RANDY','HOWARD','EUGENE','CARLOS','RUSSELL','BOBBY','VICTOR','MARTIN','ERNEST','PHILLIP','TODD','JESSE','CRAIG','ALAN'],
    "lname list": ['SMITH','JOHNSON','WILLIAMS','JONES','BROWN','DAVIS','MILLER','WILSON','MOORE','TAYLOR','ANDERSON','THOMAS','JACKSON','WHITE','HARRIS','MARTIN','THOMPSON','GARCIA','MARTINEZ','ROBINSON','CLARK','RODRIGUEZ','LEWIS','LEE','WALKER','HALL','ALLEN','YOUNG','HERNANDEZ','KING','WRIGHT','LOPEZ','HILL','SCOTT','GREEN','ADAMS','BAKER','GONZALEZ','NELSON','CARTER','MITCHELL','PEREZ','ROBERTS','TURNER','PHILLIPS','CAMPBELL','PARKER','EVANS','EDWARDS','COLLINS','STEWART','SANCHEZ','MORRIS','ROGERS','REED','COOK']
}

# call generator function
data_generator("full name",10, format, element, constraints, data_sets)


# set parameters to generate list of card holder details
format = "full name, xxxxxxxxxxxxxxxx, yyy, DD/MM/YYYY"

element = ["full name", "xxxxxxxxxxxxxxxx", "yyy", "DD", "MM", "YYYY"]

constraints = {"full name": {"record": "yes", "name": "full name"},
               "xxxxxxxxxxxxxxxx": {"record": "no", "type": "integer", "length": "16"},
               "yyy": {"record": "no", "type": "integer", "length": "3"},
               "DD": {"record": "no", "type": "integer", "range": [1, 31]},
               "MM": {"record": "no", "type": "integer", "range": [1, 12]},
               "YYYY": {"record": "no", "type": "integer", "length": "4"},
               }

data_sets = {}

# call generator function and print the list which is returned by generator
data_generator("Card holder", 10, format, element, constraints, data_sets)

# just to print data of output file
view()