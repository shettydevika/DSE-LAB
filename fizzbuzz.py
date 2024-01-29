import random
import numpy as np 
from typing import List
import tqdm
import math

def squared_distance(predictions,targets):
    return np.sum(np.array(predictions)-np.array(targets) **2)

def fizzbuzzencode(x) -> List[int]:
    if x%15 == 0:
        return[0,0,0,1]
    elif x%5 ==0:
        return [0,0,1,0]
    elif x%3 ==0:
        return [0,1,0,0]
    else:
        return [1,0,0,0]

def feed_forward(network,input_vector):
    outputs=[]

    #process one layer at a time 
    for layer in network :
        input_with_bias=input_vector+[1]  #add a bias input
        output=[neuron_output(neuron,input_with_bias) for neuron in layer]
        outputs.append(output) #remember the output

        #input to the next layer is the output of this one
        input_vector=output

    return outputs

def sigmoid(t):
    return 1/(1+math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(np.dot(weights,inputs))

def binaryencode(x:int) -> List[int]:
    binary=[]
    for i in range(10) :
        binary.append(x%2)
        x=x//2
    return binary

def sqerror_gradients(network,x,y):
    hidden_outputs=feed_forward(network[:1],x)[0]
    output_predctions=feed_forward(network,x)[-1]
    output_gradients=[2*(output_predctions[i]-y[i])*output_predctions[i]* (1- output_predctions[i]) for i in range (len(y))]

    hidden_gradients=[hidden_outputs[j]*(1-hidden_outputs[j]) * np.dot([network[1][i][j] * output_gradients[i] for i in range(len(output_gradients))], output_gradients) for j in range(len(hidden_outputs))]
    
    return [hidden_gradients,output_gradients]

def gradient_step(neuron,grad,learning_rate):
    if isinstance(grad,np.ndarray):
        grad=grad.item()
    return [weight-learning_rate*grad for weight in neuron]

xs=[binaryencode(n) for n in range(101, 1024)]
ys=[fizzbuzzencode(n) for n in range(101, 1024)]

HIDDEN=25
network=[
    [[random.random() for _ in range(11)] for _ in range(HIDDEN)],
    [[random.random() for _ in range(HIDDEN+1)] for _ in range(4)]
]

learning_rate= 1.0 
with tqdm.trange(500) as t:
    for epoch in t:
        epoch_loss=0.0
        for x,y in zip(xs,ys):
            predicted=feed_forward(network,x)[-1]
            epoch_loss+= squared_distance(np.array(predicted),np.array(y))
            gradients=sqerror_gradients(network,x,y)

            network=[
                [
                    gradient_step(neuron,grad, -learning_rate)
                    for neuron,grad in zip(layer,layer_grad)
                ]
                for layer,layer_grad in zip(network,gradients)
            ]
        t.set_description(f"Fizz Buzz(loss:{epoch_loss:.2f})")

def argmax(xs:List)  -> int:
    return max(range (len(xs)), key=lambda i:xs[i])

num_correct=0

for n in range(1,101):
    x=binaryencode(n)
    predicted=argmax(feed_forward(network,x)[-1])
    actual=argmax(fizzbuzzencode(n))
    labels=[str(n),"fizz", "buzz","fizzbuzz"]
    print(n,labels[predicted],labels[actual])
    if predicted == actual:
        num_correct+=1

print(num_correct,"/",100)

