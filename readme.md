# Mining large graphs

This is a small application which uses estimatations and approximations to find the nearest neighbours for the provided data and create graph out of it. The graph is then used to find optimal path between the two data points

## Installation

Once the zip is extracted, the dependencies should be installed using the following command (it is recommended that a new virtual environment be created and application is run in that environment)

```
bin/python -m pip install -r requirements.txt
```

The csv file to injest should be copied to the application directory and the name of the file should be set in the *config.py* file adjacent to `csvFileToLoad`. This is help application identify the file name and load it for processing.

Next step is to start the application. This could be done by the following command

```
bin/python3 -m flask --app web run
```

## Usage
The package contains the following files

1. neatestNeighbours.py 
2. graph.py
3. extraction.py
4. web.py
5. requirements.txt
6. config.py

The package contains a simple web application created in flask which has 2 endpoints

```
/GET 
/nearest?id=<datapoint>
```

```
/GET 
/path?id1=<startpoint>&id2=<endpoint>
```