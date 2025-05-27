class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:


        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m,n = n,m

        left = 0
        right = m


        while left <= right:
            i = (left + right)//2
            j = (m + n + 1)//2 - i
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA
            maxleftA = float('-inf') if i == 0 else nums1[i-1]
            maxleftB = float('-inf') if j == 0 else nums2[j-1]

            minrightA = float('inf') if i == m else nums1[i]
            minrightB = float('inf') if j == n else nums2[j]

            if maxleftA <= minrightB and maxleftB <= minrightA:
                if (m+n) % 2 == 0:
                    return (max(maxleftA, maxleftB) + min(minrightA, minrightB)) / 2
                else:
                    return max(maxleftA, maxleftB)
            elif maxleftA > minrightB:
                right = i - 1
            else:
                left = i + 1


        # m = len(nums1)
        # n = len(nums2)

        # if (m+n)%2 != 0:
        #     median_idx = [(m+n)//2]
        # else:
        #     median_idx = [(m+n)//2, ((m+n)//2)-1]

        # p1 = 0
        # p2 = 0

        # prev1 = 0
        # prev2 = 0
        # while (p1 + p2) <= median_idx[0]:
        #     if not p1<m and p2<n:
        #         prev2 = prev1
        #         prev1 = nums2[p2]
        #         # res.append(nums2[p2])
        #         p2 += 1
        #     elif not p2<n and p1<m:
        #         prev2 = prev1
        #         prev1 = nums1[p1]
        #         # res.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] <= nums2[p2]:
        #         prev2 = prev1
        #         prev1 = nums1[p1]
        #         # res.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         prev2 = prev1
        #         prev1 = nums2[p2]
        #         # res.append(nums2[p2])
        #         p2 += 1

        # if (m+n)%2 != 0:
        #     return prev1
        # return (prev1+prev2)/2
