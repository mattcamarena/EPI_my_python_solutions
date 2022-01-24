def h_index(citations: List[int]) -> int:
    nums = {}
    cKeys = []
    for citation in citations:
        if citation in nums:
            nums[citation] += 1
        else:
            nums[citation] = 1

    for key in nums.keys():
        cKeys.append(key)

    cKeys.sort(reverse=True)
    runningSum = 0
    for key in cKeys:
        if key <= nums[key] + runningSum:
            if(runningSum > key):
                return runningSum
            else:
                return key
        else:
            runningSum += nums[key]
    
    print(runningSum)
    if runningSum <= len(citations)+1:
        return runningSum
    else:
        return len(citations)+1


    return 0
