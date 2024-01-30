from random import randint

user_input = lambda x: [int(input()) for _ in range(x)]
median = lambda x: (x[len(x)//2-1]+x[len(x)//2])/2 if len(x)%2==0 else x[len(x)//2]

if __name__ == '__main__':
    print(median(user_input(input())))