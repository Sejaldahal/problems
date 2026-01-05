class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)   
        low, high = 0, m

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (m + n + 1) // 2 - mid1

            left1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            left2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]

            right1 = float('inf') if mid1 == m else nums1[mid1]
            right2 = float('inf') if mid2 == n else nums2[mid2]     

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)

            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1



if __name__ == "__main__":
    solution = Solution()

    # Test cases
    tests = [
        ([1, 3,5,7], [2]),
        ([1, 2,6], [3, 4,5]),
        ([0, 1], [1, 2]),
        ([], [1]),
        ([2], [])
    ]

    for nums1, nums2 in tests:
        median = solution.findMedianSortedArrays(nums1, nums2)
        print(f"nums1 = {nums1}, nums2 = {nums2} → median = {median}")
''' In this code we define a class Solution with a method findMedianSortedArrays that takes two sorted arrays as input.
initally we compare length of array and then perform binary search on the smaller array (hence placing smaller length in nums1).

Binary search works on sorted arrays by dividing the elements in half and then checks the condition whether equal, or less than or greater than the target value.

initally we set two pointers low and high to the start and end of the smaller array.

we then enter a while loop that continues until low is less than or equal to high.
mid1 and mid2 which represent the partition indices for nums1 and nums2 .
Both nums1 and nums2 are considered as a single sorted array and then partitioned into left and right halves.

we partition both arrays such that the left partition contains elements less than or equal to those in the right partition.
-inf and +inf are used to handle edge cases where the partition is at the start or end of an array.
left is equal to -inf when the partition index is 0 (no elements on the left side) and right is equal to +inf when the partition index is at the end of the array (no elements on the right side).
meaning that if no elements are present on one side of the partition, it won't affect the comparison.

if left1 <= right2 and left2 <= right1:
then we have found the correct partition. and we calculate the median based on whether the total number of elements is even or odd.
if odd we return the maximum of the left elements.(left1,left2)
if even we return the average of the maximum of the left elements and the minimum of the right elements.
else    
if left1 > right2:
then we are too far on the right side for nums1 and we need to move left by adjusting high pointer.
else
we are too far on the left side for nums1 and we need to move right by adjusting low pointer.



'''