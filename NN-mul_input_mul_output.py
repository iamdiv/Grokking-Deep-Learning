def w_sum(input,weight):
    assert(len(input) == len(weight))
    output = 0
    for i in range(len(input)):
        output += input[i]*weight[i]
    return output
def vect_mat_mul(input,weight):
    assert(len(input) == len(weight))
    output = [0,0,0]
    for i in range(len(input)):
        output[i] = w_sum(input,weight[i])
    return output

def neural_network(input,weight):
    h_input = vect_mat_mul(input,weight[0])
    prediction = vect_mat_mul(h_input,weight[1])
    return prediction
def main():
    ih_wt = [[0.1,0.2,-0.1],
                [-0.1,0.1,0.9],
                [0.1,0.4,0.1]]
    hp_wt = [[0.3,1.1,-0.3],
             [0.1,0.2,0.0],
             [0.0,1.3,0.1]]
    weight = [ih_wt,hp_wt]
    toes = [8.5,9.5,9.9,9.0]
    wlrec = [0.65,0.8,0.8,0.9]
    nfans = [1.2,1.3,0.5,1.0]
    input = [toes[0],wlrec[0],nfans[0]]
    pred = neural_network(input,weight)
    print(pred)
if __name__ == "__main__":
    main()

 