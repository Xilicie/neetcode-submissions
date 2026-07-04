class Solution {
public:
    int jump(vector<int>& nums) {
        int L = 0, R = 0;
        int jumps = 0;

        while (R < nums.size() - 1) {
            int farthest = L;
            for (int i = L; i < R + 1; i++) {
                farthest = max(farthest, nums[i] + i);
            }

            L = R + 1;
            R = farthest;

            jumps++;
        }


        return jumps;
    }
};
