def HotColdlearning(input,weight,goal_prediction,lr):
    for iter in range(1101):
        pred = input*weight
        error = (pred - goal_prediction)**2

        print("Error:-"+str(error)+"------Prediction :-"+str(pred))

        up_pred = input * (weight+lr)
        up_error = (up_pred - goal_prediction)**2
        down_pred = input * (weight-lr)
        down_error = (down_pred - goal_prediction)**2
        if up_error < down_error:
            weight = weight + lr
        if down_error < up_error:
            weight = weight - lr
    return weight,pred
def main():
    weight = 0.5
    input = 0.5
    goal_prediction = 0.8
    lr = 0.001
    weight,prediction = HotColdlearning(weight,input,goal_prediction,lr)
    print(weight,prediction)
if __name__ == "__main__":
    main()

