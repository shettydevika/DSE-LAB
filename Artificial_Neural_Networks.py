import numpy as np
x=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
x=x/np.amax(x,axis=0)
y=y/100
def sigmoid(x):
    return 1/(1+np.exp(-x))
def derivatives_sigmoid(x):
    return x*(1-x)
epoch=5000
lr=0.1
inputlayer_neuron=2
hiddenlayer_neuron=3
output_neuron=1
wh=np.random.uniform(size=(inputlayer_neuron,hiddenlayer_neuron))
bh=np.random.uniform(size=(1,hiddenlayer_neuron))
wout=np.random.uniform(size=(hiddenlayer_neuron,output_neuron))
bout=np.random.uniform(size=(1,output_neuron))

for i in range(epoch):
    hinpl=np.dot(x,wh)
    hinp=hinpl+bh
    hlayer_out=sigmoid(hinp)
    outinpl=np.dot(hlayer_out,wout)
    outinp=outinpl+bout
    output=sigmoid(outinp)
    
    Eo=y-output
    outgard=derivatives_sigmoid(output)
    d_output=Eo*outgard
    EH=d_output.dot(wout.T)
    
    hiddengard=derivatives_sigmoid(hlayer_out)
    d_hiddenlayer=EH*hiddengard
    
    wout+=hlayer_out.T.dot(d_output)*lr
    wh+=x.T.dot(d_hiddenlayer)*lr
    
    print("Input:\n"+str(x))
    print("Actual output:\n"+str(y))
    print("Prdicted output:\n",output)
    
//output

Input:
[[0.66666667 1.        ]
 [0.33333333 0.55555556]
 [1.         0.66666667]]
Actual output:
[[0.92]
 [0.86]
 [0.89]]
Prdicted output:
 [[0.9163712 ]
 [0.90940344]
 [0.92083078]]
