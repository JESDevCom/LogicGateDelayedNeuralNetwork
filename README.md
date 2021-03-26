# LogicGateDelayedNeuralNetwork
Neural Network Research using logic gates to solve boolean input problems.

**What is it?**

Imagine you have a room full of 9 news reporters (the nodes) and 1 king (output layer & last node). The 9 reporters are divided into 3 groups of 3 people each because the King only has 3 time slots available. So, the King has 3 morning reporters, 3 afternoon reporters, and 3 evening reporters. The first reporting group recieves the news first (input data). The next group receives the news from the previous group.

The order of the groups never changes, but each group member gets to decide when they get to report their take on the news to the next group. 

The reporters train on when their co-workers are most receptive. Should reporter 1 of group 2 go before, after, or at the same time as reporter 3 of group 2 when presenting the news to the next group? Likewise, the king learns when to say he's had enough news for the day; thereby, producing his final decision(s) (output data). He might never hear the last reporter in group 2 and 3 before making his descision. 

*TIMING MATTERS!* Thus, the delay of deciding when to present plays a big role in the neural network. Hence why this project is called "Logic Gate Delayed Neural Networks."

**What about deep neural networks?**

The reporters and their king is like a building block. You can stack them deep. So a king provides news to another set of reporters deeper in the network that have their own king. When the network begins to taper down and end, you can have layers of kings that all independently decide when to make a decision once they have received a previous decision. 

This means that through training: some kings will not have their decision heard and some kings will never make a decision in time. This emulates a bunch of brain cells deciding when to fire.

# Projects Examples

LGDNNv1: input [2 nodes], (1) hidden layer  [3 nodes each], output [1 node]
 * Solved: XNOR, NOR, OR, NAND, XOR.
 * Failed: AND
 
LGDNNv2: input [2 nodes], (2) hidden layers [3 nodes each], output [1 node]
 * Solved: XNOR, NOR, OR, NAND, XOR, AND.
 * Failed: None
 
 LGDNNv3: input [2 nodes], (2) hiddenlayers [3 nodes each], output [2 nodes]
 * Solved: mux_not, mux_or, mux_and
 * Failed: None
 
 
