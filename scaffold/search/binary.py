from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low < high:
        # Since we opt to take the floor here (left mid)
        mid = low + (high - low) // 2
        # We must check if the target is greater,
        # because if there are only two elements left
        # only `low = mid + 1` will actualy result
        # in shrinking to a single element.
        if nums[mid] < target:
            # Since the target is larger than the midpoint
            # The midpoint is not part of the solution range,
            # So we can bring our low cursor past the midpoint
            low = mid + 1
        else:
            high = mid
    return low if nums[low] == target else -1


if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5], 3))
