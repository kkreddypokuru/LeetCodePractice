# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
import logging

logging.getLogger().setLevel(logging.INFO)


def remove_duplicate(nums):
    """
    removed duplicates from sorted list
    :param nums:
    :return:
    """
    insert_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[insert_index] = nums[i]
            insert_index = insert_index + 1
    return insert_index


if __name__ == "__main__":
    data = [1, 1, 2, 2, 3, 3, 3, ]
    distinct_count, distinct_data = remove_duplicate(data)
    logging.info(f"distinct_data: {distinct_data}".format(distinct_data=distinct_data))
    logging.info("distinct_count: {distinct_count}".format(distinct_count=distinct_count))
