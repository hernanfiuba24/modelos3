# SuperRoute

## Configuration
### Python version
2.7.12
### Install pandas
```
pip install pandas
```
### Install pygraphviz
```
1. sudo apt-get install graphviz libgraphviz-dev pkg-config
2. Create and activate virtualenv if needed. The commands looks something like sudo apt-get install python-pip python-virtualenv
3. Run pip install pygraphviz
4. Run terminal and check by importing and see if it works
```
If is necesarry
```
sudo apt-get install python-dev
```
## Run test
All test are in test package
```
python test/testDijkstra.py
python test/testGrasp.py
```
## Run superMarket
first param : Hallways names
second param : Hallways graph relationes
```
python src/supermarket.py $PWD/files/hallways.json $PWD/files/hallwaysGraph.json 3 supermarket 
```
In **output** path will be the image with the best path