class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int l= nums.size();  
        for(int i=0;i<=l-1;i+=1){
            int s=nums[i];
            for(int j=i+1;j<=l-1;j+=1){
                if(s==nums[j]){
                    return true;
                }  
            }
        }
        return false;
    }
};