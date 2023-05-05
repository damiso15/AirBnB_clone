# AIR BNB CLONE - THE CONSOLE #

![The AirBnB Company Logo](./img/png-transparent-airbnb-logo-san-francisco-travel-hotel-airbnb-logo-text-trademark-logo-thumbnail.png "AirBnB")


## 0x00. AirBnB clone - The console ##

![Cloning Process](./img/cloning.png "Cloning")

This repository hosts the preliminary phase of a project aimed at replicating the AirBnB website. At this stage, a backend console is developed to manage application data. The console enables users to create, modify, and delete objects, in addition to managing file storage. Employing JSON serialization/deserialization, the storage remains consistent across sessions.

### console ###
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file) The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored. This abstraction will also allow you to change the type of storage easily without updating all of your codebase. The console will be a tool to validate this storage engine

### interpreter ###
The command interpreter looks like a mini shell and allows the management of objects of this project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


### Directories ###
* Models folder: This folder contains the classes used for this project. BaseModel is the parent Class. The other classes inherit from BaseModel and specify others attributes for itself.
* Tests folder: This folder conatins the unittests to run comprehensive tests of this project
* Img folder: This folder contains all the images needed for the README
* AUTHORS: Information about the authors
* console.py: Eceutable file of the console
* file.json: JSON file with all information of instances

---


## Table of Contents ###
* [Installation](#installation)
* [Documentation](#documentation)
* [Examples and Usage](#examplesandusage)
* [Contact](#contact)
* [License](#license)

---

### Installation ###
* You clone this [repository]()
* Move to the directory named AirBnB_clone 
* locate and execute the file console.py

---

### Documentation ###
* cmd module
* packages
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

---

### Examples and Usage ###
#### Execution ####

~~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
~~~~

#### create ####
Creat an instance and show us the id number

~~~~
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
e37cf8df-351a-4df6-9d15-fd9331a5bfb2
(hbnb) 
~~~~

#### Show ####
Show the Class, object if the id is especified and its attributes

~~~~
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) 
~~~~

#### all ####
shows all the instances

~~~~
(hbnb) all BaseModel
["[BaseModel] (5c8ebd08-a708-4823-b9a2-29d58b87c063) {'id': '5c8ebd08-a708-4823-b9a2-29d58b87c063', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 926171), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 926179)}", "[BaseModel] (e576e179-8bb6-4229-a8be-90585b0c1d01) {'id': 'e576e179-8bb6-4229-a8be-90585b0c1d01', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 896687), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 896706)}", "[BaseModel] (0763761f-4534-4a02-8097-79a4ab935ecb) {'id': '0763761f-4534-4a02-8097-79a4ab935ecb', 'created_at': datetime.datetime(2020, 7, 1, 4, 8, 48, 451468), 'updated_at': datetime.datetime(2020, 7, 1, 4, 8, 48, 451881)}", "[BaseModel] (f794d1ba-6688-42b8-ae08-0b307125643a) {'id': 'f794d1ba-6688-42b8-ae08-0b307125643a', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 922410), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 923071)}", "[BaseModel] (ef9b217c-b58c-4d5f-b797-0dbbed80dedd) {'id': 'ef9b217c-b58c-4d5f-b797-0dbbed80dedd', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 930489), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 930504)}", "[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}", "[BaseModel] (82f3d1a2-c28d-4327-be5f-0bceb29b0eb9) {'id': '82f3d1a2-c28d-4327-be5f-0bceb29b0eb9', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 888932), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 889340)}", "[BaseModel] (e029daa8-9083-4097-b2bd-a66fe4895532) {'id': 'e029daa8-9083-4097-b2bd-a66fe4895532', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 892554), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 892561)}"
(hbnb) 
~~~~

#### update ####
update an instance

~~~~
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) update BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2 first_name "CharlieMeco"
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'first_name': '"CharlieMeco"', 'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) 
~~~~

#### Destroy ####
Delete an instance

~~~~
(hbnb) destroy BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
** no instance found **
(hbnb) 
~~~~

---

### Contact ###
* Oluwadamilola SONAIKE -  [github](https://github.com/damiso15) || [LinkedIn](https://www.linkedin.com/in/oluwadamilola-sonaike/)

---

### License ###
MIT License
