# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    time = [0]*n
    
    for i in range(m):
        thread = time.index(min(time))
        start = time[thread]
        time[thread] += data[i]
        output.append((thread, start))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = map(int, input().split())
    m = map(int, input().split())
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, start in result:
        print(thread, start)



if __name__ == "__main__":
    main()
