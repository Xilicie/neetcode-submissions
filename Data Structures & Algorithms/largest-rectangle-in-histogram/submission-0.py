class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areasToR = heights[:]
        for i in range(len(heights) - 1):
            h = heights[i]
            area = h
            j = i + 1
            while j < len(heights) and h <= heights[j]:
                area += h
                j += 1
            areasToR[i] = area
            
        areasToL = heights[:]
        for i in range(len(heights) - 1, 0, -1):
            h = heights[i]
            area = h
            j = i - 1
            while j >= 0 and h <= heights[j]:
                area += h
                j -= 1
            areasToL[i] = area

        maxA = 0
        for i in range(len(heights)):
            area = areasToR[i] + areasToL[i] - heights[i]
            maxA = max(area, maxA)
        
        return maxA
