# NFA_2_DFA (NFA_to_DFA)
## A simple python script that turns NFA to DFA

we know that every DFA/NFA, can be described using these 5 properties:

  1-The alphabet
  
  2-State set
  
  3-Initial state
  
  4-Accept state(s)
  
  5-Transition function
  
  
in this algorithm, we assume that our alphabet is {a,b}.

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

in second line, we get the accept state(s) (in ascending order).

in each of the next lines, one section of transition fucntion is written in the form below:
```
    <from state>:<symbol>:<to state1>,<to state2>,...
    <from state>:<symbol>:<to state1>,<to state2>,...
    ...
```


at the end of input, for better understanding of the algorithm, type "end".

### output
in the first line of output, we get the number of states in the corresponding DFA, in the second line, the start state and in third one, Accept state(s) in an ascending order.

in the lines after that, transfer function with a lexicographic sort gets printed:
```
<from state>:<symbol>:<to state>
<from state>:<symbol>:<to state>
...
```

### example
#### input
this NFA's language is a<sup>__*__</sup>.
```
1
0
0:a:0
end
```

#### output
```
2
1
1
0:a:0
0:b:0
1:a:1
1:b:0
```
