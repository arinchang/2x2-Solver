# 2x2 Rubik's Cube Solver 
## Usage
Run the following command, replacing the string with scramble of your choice. Note: double moves such as "U2" must be input as "U U". If you're not familiar with cube notation, visit here: https://ruwix.com/the-rubiks-cube/notation/

Note that the solver takes a while to run for scrambles longer than 5 moves long. I May change the state representation to be something hashable like integers in the future and possibly re-implement with C++. 
```none
$ python3 solver.py "R U F U' L"
```
Make sure to keep your cube in the same orientation as you scrambled it when performing the algorithm returned by the solver. If you do not own a physical 2x2 but own a 3x3 cube, you can use your 3x3 and you should see that the corners are solved in some orientation. 

## Dependencies
- Python 3+
- numpy 

Install python, then run the following commands:
```none
$ pip install numpy
```