## Program name: scan_github.py

### Description

   Imaging we are interested to know the popularity of technology stack like 'django', 'react' ...
   This small web crawler program will search the keywords in github and display the sorted results.

### How to run

- Setup: The python program uses two python modules: requests and beautifulsoup(bs4)
  To install these two packages:  
	~~~~
	pip install requests
	pip install beautifulsoup4
	~~~~

- Review and modify the content of the list 'keywords' as needed
	~~~~
	keywords = ['angular', 'flask', 'django', 'react', 'node.js', 'mysql', 'sqlite', 'mongodb']
	~~~~

- To run the program:
	~~~~
	python scan_github.py
	~~~~

### Sample output

	~~~~
	Retriving term 'angular' : 625,475
	Retriving term 'flask' : 146,484
	Retriving term 'django' : 286,692
	Retriving term 'react' : 1,286,091
	Retriving term 'node.js' : 245,097
	Retriving term 'mysql' : 172,295
	Retriving term 'sqlite' : 45,387
	Retriving term 'mongodb' : 131,499

	Sorted result:
	react   : 1286091
	angular :  625475
	django  :  286692
	node.js :  245097
	mysql   :  172295
	flask   :  146484
	mongodb :  131499
	sqlite  :   45387
	~~~~
  
   