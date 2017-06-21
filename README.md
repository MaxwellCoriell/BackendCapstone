## BackendCapstone

# DjangoTaskManager

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A task manager application that allows users to create and assign tasks for themselves or other users. As well as being able to delete, and edit, and mark as complete each task.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)   
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## About
Hey, y'all, this Single Page Django Application is a cumulation of the things I've learned in the Backend Portion of my times at [Nashville Software School](https://github.com/nashville-software-school). It is not neccessarily the best representation of my skills, but I am the cause of my own bugs in my code of life.

There is another project that I started, but I made it more complicated than it needed to be, and I am paying the price for it.



### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django:
```
pip install django
```


## Installation


```
git clone https://github.com/MaxwellCoriell/BackendCapstone.git
cd DjangoTaskManager/DjangoTaskManager
```
Setting up the database:

```
chmod +x ./migrate_Django.sh 
```
(^after running this the first time, there is no need to run it again^)
```
./migrate_Django.sh
```
Run project in browser:

```
python manage.py runserver
```



## Usage
[UNDER CONSTRUCTION]


## Contribute

If you want to add to it, go ahead. It's a fairly simple application, but could be expanded more.

1. Fork it!
2. Create your feature branch:
```git checkout -b <YourInititals-WhatNewFeatureDoes>```
3. Commit your changes:
```git commit -m 'Add some feature, or whatever'```
4. Push to the branch:
```git push origin <YourInititals-WhatNewFeatureDoes>```
5. Submit a pull request :D

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits
Project Managers:
  * [Steve Brownlee](https://github.com/stevebrownlee)- BackEnd Instructor
  * [Brenda Long](https://github.com/brendalong)- FrontEnd Instructor
  * [Meg Ducharme](https://github.com/megducharme)- Teacher's Assitant
  * [Gilbert Diaz](https://github.com/gilbertdiaz)- Teacher's Assistant

Thank you all for your invaluable knowledge, your patience, and your care for your students. Without the four of you, I know that I, and my classmates at NSS, wouldn't be anywhere close to the developers we are now.


Build Contributors:
  * [Max Baldridge](https://github.com/MaxwellCoriell)

## License
[MIT © 2017 Max Baldridge](./LICENSE)
