# :book: alx-backend-storage.


## :page_with_curl: Topics Covered.
1. MySQL advanced.


## :wrench: Project setup.
```bash
## Install MySQL 5.7 in ubuntu

# Add key to server
sudo apt-key add signature.key

# Add apt repo
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

sudo apt-get update

# Check mysql available versions
sudo apt-cache policy mysql-server

# Install mysql 5.7
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

# Check if installed
mysql --version


# Create project directory and readme.
mkdir ./alx-backend-storage/
touch ./alx-backend-storage/README.md

cd alx-backend-storage

# Create git repository.
git init
git add .
git commit -m 'first commit'
git remote add origin <REMOTE_URL>
git push
```


# :computer: Projects


## [0x00. MySQL advanced](0x00-MySQL_Advanced)


### :wrench: Project setup.
```bash
# Create project directory and readme.
mkdir ./0x00-MySQL_Advanced/
touch ./0x00-MySQL_Advanced/README.md
cd 0x00-MySQL_Advanced
```

> [:point_right: Go to project](0x00-MySQL_Advanced)


## [0. We are all unique!](0-uniq_users.sql)
Write a SQL script that creates a table users following these requirements:

*   With these attributes:
    *    id, integer, never null, auto increment and primary key
    *    email, string (255 characters), never null and unique
    *    name, string (255 characters)
*    If the table already exists, your script should not fail
*    Your script can be executed on any database

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
```
### :wrench: Project setup.
```bash
# Create project directory and readme.
mkdir ./0-uniq_users.sql/
touch ./0-uniq_users.sql/README.md
cd 0-uniq_users.sql
```

> [:point_right: Go to project](0x00-MySQL_Advanced)


![0x02. Python - Async Comprehension](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230110T151042Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0e47e3b3f27e61fe826c4521bb00eb04fb9e07b8bd1c4927e1c8577d1623e539)
## [0x02. Python - Async Comprehension](0x02-python_async_comprehension)
Type Annotation (Strongly Dynamically typed) in python. Reason for implementing type Annotation:
1. Code documentation.
2. Linting and validation.

### :wrench: Project setup.
```bash
# Create project directory and readme.
mkdir ./0x02-python_async_comprehension/
touch ./0x02-python_async_comprehension/README.md
cd 0x02-python_async_comprehension
```

> [:point_right: Go to project](0x02-python_async_comprehension)


# :man: Author and Credits.
This project was done by [SE. Nathaniel Emenike](https://github.com/Githubnath). Feel free to get intouch with me;

:iphone: WhatsApp [+2347035445571](https://wa.me/2347035445571)

:email: Email [emenikenathaniel55@gmail.com](mailto:emenikenathaniel55@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
