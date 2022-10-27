import numpy as np


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        max_overlap = 0
        img1 = np.array(img1)
        img2 = np.array(img2)
        lens = len(img1)
        img1_padded = np.pad(img1, lens-1, mode='constant', constant_values=(0, 0))
        for i in range(lens * 2 - 1):
            for j in range(lens * 2 - 1):
                max_overlap = max(max_overlap, np.sum(img1_padded[i:i+lens, j:j+lens] * img2))
        return max_overlap
