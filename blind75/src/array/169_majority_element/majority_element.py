def majorityElement(self, nums):
    count = 0
    m_element = 0

    for n in nums:
        if count == 0:
            m_element = n
            count += 1
        elif m_element == n:
            count += 1
        else:
            count -= 1

    return m_element
