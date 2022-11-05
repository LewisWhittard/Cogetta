Cogger is a substitution cipher written in Python 3 and has been released 
under the MIT license. This works by allowing you to define a custom amount 
of set of IDs (wheel keys).

Here is an example of how a 2 wheeled-key would work:

Original Key: 1-0-2-3+3-2-1-0    
Character set: 0:A-S-D-F    
Message: ASDFA

Start Encryption:
Key state  1-0-2-3+3-2-1-0    
A(0) becomes S (1) which becomes D(2)
key state 2-1-3-0+3-2-1-0
S(1) becomes S(1) which becomes D(2)
Key state 3-2-0-1+3-2-1-0
D(2) becomes A(0) which becomes F(3)
Key  state 0-3-1-2+3-2-1-0
F(3) becomes D(2) which becomes S(1)
Key state 1-0-2-3+0-3-2-1
A(0) becomes S(1) which becomes F(3)
Your final encrypted message DDFSF
