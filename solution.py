def solution(number):
    num_list=[x for x in range(number) if x%3==0 or x%5==0]
    return sum(num_list)

if __name__ == '__main__':
    assert solution(10)==23
    assert solution(0)==0
    solution(15)==45