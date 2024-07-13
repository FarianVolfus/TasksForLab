import sys

def find_moves(nums): # ищем минимальные шаги
    nums.sort()
    median = nums[round(len(nums) / 2)] #считаем медиану
    result_moves = sum(abs(num - median) for num in nums)
    # print(result_moves) чек
    return result_moves


if __name__ == "__main__":
    nums_data = sys.argv[1]
    with open(nums_data, 'r') as file:
        nums = [int(line) for line in file]
    # print(nums) чек
    moves = find_moves(nums)
    print(moves)


