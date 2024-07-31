package 项目;
import java.util.Scanner;
import java.util.HashMap;

/*
 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false
 */

public class test_6 {
	public static void main(String[] args) {
		// TODO 自动生成的方法存根
			Scanner sc=new Scanner(System.in);
			int k=sc.nextInt();
			sc.close();
			int array[]=new int[] {1,2,3,2,-1,0,100};
			Solution_6 s1=new Solution_6();
			System.out.println(s1.containsNearbyDuplicate(array, k));
	}

}

class Solution_6{
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer>h1=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++) {
        	if(h1.containsKey(nums[i])) {
        		if(Math.abs(i-h1.get(nums[i]))<k) {
        			return true;
        		}
        	}
        	h1.put(nums[i],i);
        }
        return false;
    }
}