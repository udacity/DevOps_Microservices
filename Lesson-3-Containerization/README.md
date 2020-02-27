# Data Engineering API Example

An example project that shows how to create a Data Engineering API around Flask and Pandas:

Data teams often need to build libraries and services to make it easier to work with data on the platform.  In this example there is a need to create a Proof of Concept aggregation of csv data.  A REST API that accepts a csv, a column to group on, and a column to aggregate and returns the result.

Note,this project is a Chapter in the book Pragmatic AI, the entire projects source can be found [here](https://github.com/noahgift/pragmaticai)

## Using the default web app.
The Swagger API has some pretty powerful tools built in.

* To list the plugins that are loaded:

![Plugins](https://user-images.githubusercontent.com/58792/37561928-cf57944a-2a18-11e8-8f97-3d1e1cda4041.png)

* To apply one of those functions:

![Swagger API](https://user-images.githubusercontent.com/58792/37561897-019be4fc-2a18-11e8-8351-53d8d7f527b9.png)

## Sample Input

```
first_name,last_name,count
chuck,norris,10
kristen,norris,17
john,lee,3
sam,mcgregor,15
john,mcgregor,19
```
## Sample Output

```
norris,27
lee,3
mcgregor,34
```

## How to run example and setup environment:

To create environment (tested on OS X 10.12.5), run `make setup`, which does the following commands below:

```
mkdir -p ~/.pai-aws && python3 -m venv ~/.pai-aws
```

Then source the virtualenv.  Typically I do it this way, I add an alias to my .zshrc:

```
alias ntop="cd ~/src/pai-aws && source ~/.pai-aws/bin/activate"
```

I can then type in:  `ntop` and I cd into my checkout and source a virtualenv.  Next, I then make sure I have the latest packages and that linting and tests pass by running make all:

```make all```


I also like to verify that pylint and pytest and python are exactly the versions I expect, so I added a make command env to conveniently check for these:

```make env

(.pai-aws) ➜  pai-aws git:(master) ✗ make env
#Show information about environment
which python3
/Users/noahgift/.pai-aws/bin/python3
python3 --version
Python 3.6.1
which pytest
/Users/noahgift/.pai-aws/bin/pytest
which pylint
/Users/noahgift/.pai-aws/bin/pylint
```

## How to interact with Commandline tool (Click Framework):


Check Version:

```
(.pai-aws) ➜  pai-aws git:(master) ✗ ./csvutil.py --version
csvutil.py, version 0.1
```

Check Help:

```
(.pai-aws) ➜  pai-aws git:(master) ✗ ./csvutil.py --help   
Usage: csvutil.py [OPTIONS] COMMAND [ARGS]...

  CSV Operations Tool



Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

Aggregate CSV

```
(.pai-aws) ➜  pai-aws git:(master) ✗ ./csvcli.py cvsagg --file ext/input.csv --column last_name
Processing csvfile: ext/input.csv and column name: last_name
{"count":{"mcgregor":34,"lee":3,"norris":27}}
```

Testing a bigger file than the assignment:

```
(.pai-aws) ➜  pai-aws git:(master) ✗ ./csvcli.py cvsagg --file ext/large_input.csv --column last_name 
Processing csvfile: ext/large_input.csv and column name: last_name
{"count":{"mcgregor":34,"lee":3,"norris":27},"random_column":{"mcgregor":57,"lee":61,"norris":100}}
```


## How to run webapp (primary question) and use API

To run the flask api (if you have followed instructions above), you should be able to run the make command `make start-api`.  The output should look like this:

```
(.pai-aws) ➜  pai-aws git:(master) ✗ make start-api
#sets PYTHONPATH to directory above, would do differently in production
cd flask_app && PYTHONPATH=".." python web.py
2017-06-17 16:34:15,049 - __main__ - INFO - START Flask
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
 * Restarting with stat
2017-06-17 16:34:15,473 - __main__ - INFO - START Flask
 * Debugger is active!
 * Debugger PIN: 122-568-160
2017-06-17 16:34:43,736 - __main__ - INFO - {'/api/help': 'Print available api routes', '/favicon.ico': 'The Favicon', '/': 'Home Page'}
127.0.0.1 - - [17/Jun/2017 16:34:43] "GET / HTTP/1.1" 200 -
```

## Test Client with Swagger UI

Next, open a web browser to view Swagger API documentation (formatted as HTML):

  http://0.0.0.0:5001/apidocs/#/

For example to see swagger docs/UI for cvs aggregate endpoint go here:

  http://0.0.0.0:5001/apidocs/#!/default/put_api_aggregate

## Interactively Test application in IPython

Using the requests library you can query the api as follows in IPython:

```

In [1]: import requests, base64
In [2]: url = "http://0.0.0.0:5001/api/npsum"
In [3]: payload = {'column':'count', 'group_by':"last_name"}
In [3]: headers = {'Content-Type': 'application/json'}
In [3]: with open("ext/input.csv", "rb") as f:
    ...:     data = base64.b64encode(f.read())

In [4]: r = requests.put(url, data=data, params=payload, headers=headers)

In [5]: r.content
Out[5]: b'{"count":{"mcgregor":34,"lee":3,"norris":27}}'

```

## How to simulate Client:
  run the client_simulation script
```
(.pai-aws) ➜  tests git:(inperson-interview) ✗ python client_simulation.py 
status code:  400
response body:  {'column': 'count', 'error_msg': 'Query Parameter column or group_by not set', 'group_by': None}
status code:  200
response body:  {'first_name': {'3': 'john', '10': 'chuck', '15': 'sam', '17': 'kristen', '19': 'john'}, 'last_name': {'3': 'lee', '10': 'norris', '15': 'mcgregor', '17': 'norris', '19': 'mcgregor'}}
```

## How to interact with python library (nlib):

  Typically I use commandline IPython to test libraries that I create.  Here is how to ensure the library is working (should be able to get version number):

```
In [1]: from nlib import csvops

In [2]: df = csvops.ingest_csv("ext/input.csv")
2017-06-17 17:00:33,973 - nlib.csvops - INFO - CSV to DF conversion with CSV File Path ext/input.csv

In [3]: df.head()
Out[3]: 
  first_name last_name  count
0      chuck     norris     10
1    kristen     norris     17
2       john       lee      3
3        sam     mcgregor     15
4       john     mcgregor     19

```




## Benchmark web Service

Finally, the simplest way to test everything is to use the Makefile to start the web service and then benchmark it (which uploads base64 encoded csv):

```

(.pai-aws) ➜  pai-aws git:(master) ✗ make start-api

```

Then run the apache benchmark via Makefile.  The output should look something like this:

```

(.pai-aws) ➜  pai-aws git:(inperson-interview) ✗ make benchmark-web
#very simple benchmark of api
ab -n 1000 -c 100 -T 'application/json' -u ext/input_base64.txt http://0.0.0.0:5001/api/aggregate\?column=count\&group_by=last_name
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.12.2
Server Hostname:        0.0.0.0
Server Port:            5001

Document Path:          /api/aggregate?column=count&group_by=last_name
Document Length:        154 bytes

Concurrency Level:      100
Time taken for tests:   7.657 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      309000 bytes
Total body sent:        308000
HTML transferred:       154000 bytes
Requests per second:    130.60 [#/sec] (mean)
Time per request:       765.716 [ms] (mean)
Time per request:       7.657 [ms] (mean, across all concurrent requests)
Transfer rate:          39.41 [Kbytes/sec] received
                        39.28 kb/s sent
                        78.69 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       6
Processing:    18  730 142.4    757     865
Waiting:       18  730 142.4    756     865
Total:         23  731 141.3    757     865

Percentage of the requests served within a certain time (ms)
  50%    757
  66%    777
  75%    787
  80%    794
  90%    830
  95%    850
  98%    860
  99%    862
 100%    865 (longest request)



```

### Viewing Juypter Notebooks

They can be found here:
https://github.com/noahgift/pai-aws/blob/inperson-interview/notebooks/api.ipynb

### Circle CI Configuration

Circle CI is used to build the project.  The configuration file looks like follows:

```
machine:
  python:
    version: 3.6.1

dependencies:
  pre:
    - make install

test:
  pre:
    - make lint-circleci
    - make test-circleci
```

Those make commands being called are below.  They write artifacts to the Circle CI Artifacts Directory:


```
lint-circleci:                                                              
  pylint --output-format=parseable --load-plugins pylint_flask --disable=R,C flask_app/*.py nlib csvcli > $$CIRCLE_ARTIFACTS/pylint.html  

test-circleci:
  @cd tests; pytest -vv --cov-report html:$$CIRCLE_ARTIFACTS --cov=web --cov=nlib test_*.py  
```

The URL for the project build is here:  https://circleci.com/gh/noahgift/pai-aws.  To see artificats pylint output and/or test coverage output, you can go to the artificats directory here (for build 24):  

https://circleci.com/gh/noahgift/pai-aws/24#artifacts/containers/0















