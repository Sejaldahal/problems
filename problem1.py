# Two Sum Problem
#using simple brute force approach

def twosums(nums,target):
    for i in range (len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = twosums(nums, target)
    print(result) 

''' In this code we define a function twosums which takes a list of numbers and a target sum as input.
firstly in the nums array we iterated through each element using two nested loops.
in the outer loop we select an element and in the inner loop we check for every other element if the sum of the two elements equals the target.
if we find such a pair we return their indices as a list [i,j].

'''