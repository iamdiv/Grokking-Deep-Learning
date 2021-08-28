def el_mul(input,weight):
    output = [0,0,0]
    assert(len(output) == len(weight))
    
    for i in range(len(weight)):
        output[i] = input*weight[i]
    return output
def neural_network(input,weight):
    prediction = el_mul(input,weight)
    return prediction
def main():
    weight = [0.3,0.2,0.9]
    wlrec = [0.65,0.8,0.8,0.9]
    input = wlrec[0]
    pred = neural_network(input,weight)
    print(pred)
if __name__ == "__main__":
    main()

