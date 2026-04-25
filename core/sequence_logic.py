def get_sequences(nums):
    if not nums:
        return []

    nums = sorted(set(nums))
    sequences = []
    current = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current.append(nums[i])
        else:
            if len(current) >= 2:   # 🔥 FILTER
                sequences.append(current)
            current = [nums[i]]

    if len(current) >= 2:
        sequences.append(current)

    return sequences