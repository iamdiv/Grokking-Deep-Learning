def w_sum(input,weight):
    assert(len(input) == len(weight))
    output = 0
    for i in range(len(input)):
        output += input[i]*weight[i]
    return output
def neural_network(input,weight):
    prediction = w_sum(input,weight)
    return prediction
def main():
    weight = [0.1,0.2,0]
    toes = [8.5,9.5,9.9,9.0]
    wlrec = [0.65,0.8,0.8,0.9]
    nfans = [1.2,1.3,0.5,1.0]
    input = [toes[0],wlrec[0],nfans[0]]
    pred = neural_network(input,weight)
    print(pred)
if __name__ == "__main__":
    main()

