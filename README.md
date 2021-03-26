# LogicGateDelayedNeuralNetwork
Neural Network Research using logic gates to solve boolean input problems.

**What is it?**

Imagine you have a room full of 9 news reporters (the nodes) and 1 king (last layer & last node). The 9 reporters are divided into 3 groups of 3 people because the King only has 3 appointment slots open. hence, you have the 3 morning reporters, the 3 afternoon reporters, and the 3 evening reporters. All reporters have the same news story (input data) from that morning.

The order of the groups never changes, but each group member gets to decide when they get to report their take on the news to the King. 

The reporters train on when the king is most receptive. Should reporter 1 of group 2 go before, after, or at the same time as reporter 3 of group 2 when presenting the news to the King? Likewise, the king learns when to say he's had enough news for the day; thereby, producing his final decision(s) (output data). He might never find the last reporter in group 3 to be worthy and will make his descion before hearing him. 

*THE TIME OF DAY MATTERS!* Thus, the delay plays a big role in the neural network. Hence why this project is called "Logic Gate Delayed Neural Networks."

**What about deep neural networks?**

The reporters and their king is like a building block. You can stack them deep. So a king provides news to another set of reporters deeper in the network that have their own king. When the network begins to taper down and end, you can have layers of kings that all independtly decide when to make a decision once they have received a previous decision. 

This means that through training: some kings will not have their decision heard and some kings will never make a decision in time. 

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
 
 
