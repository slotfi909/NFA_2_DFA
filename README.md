# NFA_to_DFA
## A simple python script that turns NFA to DFA

we know that every DFA/NFA, can be described using these 5 properties:
  1-The alphabet
  2-State set
  3-Initial state
  4-Accept state(s)
  5-Transition function
  
in this algorithm, we assume that our alphabet consist of {a,b}.

we also label our states starting from 0(in NFA, we consider start state the zero state), and we show epsilon transitions using " ' ". 

so for example, if we have an NFA with 3 states, its state set will be {0,1,2} and for its respective DFA, our state set will be {0,1,2,3,4,5,6,7}, which will correspond to NFA states as below:

|DFA state|coressponding NFA states|
|---------|------------------------|
|0|{}|
|1|{0}|
|2|{1}|
|3|{2}|
|4|{0,1}|
|5|{0,2}|
|6|{1,2}|
|7|{0,1,2}|


### input
in the first line of input, we get the number of NFA's states.

in second line, we get the accept state(s) (in aceending order).

in each of the next lines, one section of transition fucntion is written in the form below:
    '''
    <from state>:<symbol>:<to state1>,<to state2>,...
    <from state>:<symbol>:<to state1>,<to state2>,...
    ...
    '''


in 
