# 0x00. AirBnB clone - The console

## Introduction

This is a team project to make a clone of [AirBnb](https://fr.airbnb.com/)'s console
<br>
We want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources

- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

## General

### Installation

```bash
git clone https://github.com/s-maarouf/AirBnB_clone.git
```

### Execution

**In interactive mode**

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

**In non-interactive mode**

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Commands usage

- **help**: list available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

<br>

- **help \<command\>**: prints command documentation

```bash
(hbnb) help <command>
```

> example

```bash
(hbnb) help destroy
Deletes an instance
(hbnb)
```

<br>

- **create**: to create a new instance:

```bash
(hbnb) create <class_name>
```

> example

```bash
(hbnb) create BaseModel
73fea987-e376-4de8-9964-1f17c59737ca
(hbnb)
```

<br>

- **show**: to show an instance informations:

```bash
(hbnb) show <class_name> <class_id>
```

> example

```bash
(hbnb) show BaseModel 73fea987-e376-4de8-9964-1f17c59737ca
[BaseModel] (73fea987-e376-4de8-9964-1f17c59737ca) {'id': '73fea987-e376-4de8-9964-1f17c59737ca', 'created_at': datetime.datetime(2023, 7, 16, 22, 23, 37, 618037), 'updated_at': datetime.datetime(2023, 7, 16, 22, 23, 37, 618037)}
(hbnb)
```

<br>

- **destroy**: to destroy an instance:

```bash
(hbnb) destroy <class_name> <class_id>
```

> example

```bash
(hbnb) destroy BaseModel 73fea987-e376-4de8-9964-1f17c59737ca
(hbnb)
```

<br>

- **all**: to show all instances based or not on the class name

```bash
(hbnb) all
```

> example

```bash
(hbnb) all
[]
(hbnb) create BaseModel
f9f6c985-14d1-4d4f-be9e-c2c80594c33f
(hbnb) all
["[BaseModel] (f9f6c985-14d1-4d4f-be9e-c2c80594c33f) {'id': 'f9f6c985-14d1-4d4f-be9e-c2c80594c33f', 'created_at': datetime.datetime(2023, 7, 16, 22, 30, 25, 505852), 'updated_at': datetime.datetime(2023, 7, 16, 22, 30, 25, 505852)}"]
(hbnb) create User
97763dfd-9521-46fb-bd2a-af570cfaf29b
(hbnb) all
["[BaseModel] (f9f6c985-14d1-4d4f-be9e-c2c80594c33f) {'id': 'f9f6c985-14d1-4d4f-be9e-c2c80594c33f', 'created_at': datetime.datetime(2023, 7, 16, 22, 30, 25, 505852), 'updated_at': datetime.datetime(2023, 7, 16, 22, 30, 25, 505852)}", "[User] (97763dfd-9521-46fb-bd2a-af570cfaf29b) {'id': '97763dfd-9521-46fb-bd2a-af570cfaf29b', 'created_at': datetime.datetime(2023, 7, 16, 22, 30, 30, 855188), 'updated_at': datetime.datetime(2023, 7, 16, 22, 30, 30, 855188)}"]
(hbnb)
```

<br>

- **update**: to update an instance  by adding or updating attribute

```bash
(hbnb) update <class_name> <class_id> <attribute name> "<attribute value>"
```

> example

```bash
(hbnb) update User 97763dfd-9521-46fb-bd2a-af570cfaf29b first_name "SMAAROUF"
(hbnb) show User 97763dfd-9521-46fb-bd2a-af570cfaf29b
[User] (97763dfd-9521-46fb-bd2a-af570cfaf29b) {'id': '97763dfd-9521-46fb-bd2a-af570cfaf29b', 'created_at': datetime.datetime(2023, 7, 16, 22, 30, 30, 855188), 'updated_at': datetime.datetime(2023, 7, 16, 22, 30, 30, 855188), 'first_name': '"SMAAROUF"'}
(hbnb)
```

<br>

- **count**: to count the number of instances of a class

```bash
(hbnb) count <class_name>
```

> example

```bash
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```

<br>

- **quit**: to quit the console:

```bash
(hbnb) quit
$
```

<br>

- **EOF**: exit the program using EOF

```bash
(hbnb) EOF

$
```

## Author's notes:

This project was made by [@s-maarouf](https://github.com/s-maarouf) and [@ABDE-LKADER](https://github.com/ABDE-LKADER)
