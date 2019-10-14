# oracle
# 14/10/2019
# Tanwir Ali [ali.tanwir@yahoo.co.uk]


# 1. Python script that converts a non-negative integer to it's English words equivalent

instructions
------------

* clone git
> git clone https://github.com/desertsystems/oracle.git
> cd oracle
> python3 number.py

**relevant files**
**number.py**



# 2. A service using Docker for Python web servic

instructions
------------

* clone git (if not already done for first part)
> git clone https://github.com/desertsystems/oracle.git


* build
> cd oracle
> docker build -t oracle .


* check local image
> docker images


* run
> docker run -d -p 5000:5000 oracle:latest


* test
> curl http://127.0.0.1:5000/
*response: {'oracle': 'python'}*


* kill
*get container_id from*
> docker ps
*then execute*
> docker kill [container_id]


* delete local images
> docker system prune -a

**relevant file**
**app.py**
**Dockerfile**




# 0. Buzzfizz

`for a range of numbers 1 to 100, output all but subtitute all divisible by 3 with 'fizz' and substitute all divisible by 5 with 'buzz'. Substitube those number that are both divisabe by 3 and 5 with 'fizzbuzz'.`

instructions
------------

# clone git (if not already done for first &/ second part)
> git clone https://github.com/desertsystems/oracle.git
> cd oracle
> python3 buzzfizz.py

**relevant files**
**buzzfizz.py**