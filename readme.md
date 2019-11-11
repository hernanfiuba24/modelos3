# SuperRoute

## Configuration
### Python version
2.7.12
### Install flask
```
pip install Flask
```
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
### Run test
All test are in test package
```
python test/testDijkstra.py
python test/testGrasp.py
```
### Run superMarket
first param : Hallways names
second param : Hallways graph relationes
```
python src/supermarket.py $PWD/files/hallways.json $PWD/files/hallwaysGraph.json 3 supermarket 
```
### Run superMarket from API
* Run API
```
python src/main.py
```
* Request
Get image of hallwaysSuper
```
http://localhost:5000/hallwaysSuper/hallways
```
Get superRoute
    - target : points to visit (separate by colon ',')
    - name : image name
```
http://localhost:5000/superRoute?target=3,4&superName=hallways
http://localhost:5000/superRoute?target=19,20,21&superName=hallwaysSuperX
```


In **output** path will be the image with the best path