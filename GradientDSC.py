import numpy as np 

def w_sum(inp,wt):
    assert(len(inp) == len(wt))
    output = 0
    for i in range(len(inp)):
        output += inp[i]*wt[i]
    return output


def vect_mat_mul(input,weights):
    assert(len(input) == len(weights))
    output = [0,0,0]
    for i in range(len(input)):
        output[i] = w_sum(input,weights[i])
    return output

def neural_network(input,weights):
    pred = vect_mat_mul(input,weights)

    return pred 

def outer_prod(vec_a,vec_b):
    out = np.zeros((len(vec_a),len(vec_b)))

    for i in range(len(vec_a)):
        for j in range(len(vec_b)):
            out[i][j] = vec_a[i]*vec_b[j]
    return out


def GradientDSC():
    weights = [[0.1,0.1,-0.3],
              [0.1,0.2,0.0],
              [0.0,1.3,0.1]]
    toes = [8.5,9.5,9.9,9.0]
    wlrec = [0.65,0.8,0.8,0.9]
    nfans = [1.2,1.3,0.5,1.0]

    hurt = [0.1,0.0,0.0,0.1]
    win = [1,1,0,1]
    sad = [0.1,0.0,0.1,0.2]

    alpha = 0.01

    input = [toes[0],wlrec[0],nfans[0]]
    tr = [hurt[0],win[0],sad[0]]
    pred = neural_network(input,weights)
    error = [0,0,0]
    delta = [0,0,0]

    for i in range(len(tr)):
        error[i] = (pred[i]-tr[i]) **2
        delta[i] = pred[i]-tr[i] 

    wt_deltas = outer_prod(error,delta)

    for i in range(len(weights)):
        for j in range(len(weights[0])):
            weights[i][j] -= alpha*wt_deltas[i][j]
    print("Updated weights",weights)

if __name__ == '__main__':
    GradientDSC()