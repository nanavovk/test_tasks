import argparse
import statistics

parser = argparse.ArgumentParser(description='Steps')
parser.add_argument('nums_path', type=str, help='path to nums')
args = parser.parse_args()

with open(args.nums_path, 'r') as file:
    nums = [line.strip() for line in file.readlines()]
nums1 = list(map(int, nums))

mid = statistics.median(nums1)
cnt = 0

for i in nums1:
    cnt += abs(mid - i)

print(int(cnt))
