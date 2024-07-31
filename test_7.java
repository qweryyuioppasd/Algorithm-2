package 项目;
import java.util.Scanner;
import java.util.HashMap;
/*
 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
 */
public class test_7 {
	public static void main(String[] args) {
		// TODO 自动生成的方法存根
	   int nums1[]=new int[] {1,2,3,4,5,6,7};
	   int nums2[]=new int[] {1,2,1,3,4,5};
	   int nums3[]=new int[0];
	   Solution_7 s1=new Solution_7();
	   System.out.println(s1.containsDuplicate(nums1));
	   System.out.println(s1.containsDuplicate(nums2));
	   System.out.println(s1.containsDuplicate(nums3));
	}

}

class Solution_7{
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer>h1=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++) {
        	if(h1.containsKey(nums[i])) {
        		return true;
        	}
        	h1.put(nums[i],i);
        }
        return false;
    }
}