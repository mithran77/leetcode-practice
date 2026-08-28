class Solution {
private:
    vector<int> memo;
    vector<bool> computed;

    // Returns the maximum subarray sum that MUST end at index i
    int dp(int i, const vector<int>& nums) {

        // Base case
        if (i == 0) {
            return nums[0];
        }

        // Already solved?
        if (computed[i]) {
            return memo[i];
        }

        /*
            Two choices:

            1. Start new subarray at i
               nums[i]

            2. Extend best subarray ending at i-1
               nums[i] + dp(i-1)
        */

        memo[i] = max(
            nums[i],
            nums[i] + dp(i - 1, nums)
        );

        computed[i] = true;

        return memo[i];
    }

public:
    int maxSubArray(vector<int>& nums) {

        int n = nums.size();

        memo.resize(n);
        computed.resize(n, false);

        int answer = nums[0];

        // Compute dp(i) for every position
        for (int i = 0; i < n; i++) {

            /*
                dp(i) = best subarray ending at i

                Example:
                [-2,1,-3,4,-1,2,1,-5,4]

                dp(0) = -2
                dp(1) = 1
                dp(2) = -2
                dp(3) = 4
                dp(4) = 3
                dp(5) = 5
                dp(6) = 6
                dp(7) = 1
                dp(8) = 5
            */
            answer = max(answer, dp(i, nums));
        }

        return answer;
    }
};
