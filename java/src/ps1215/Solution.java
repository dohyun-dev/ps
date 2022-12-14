package com.example.cicd.controller;

import java.util.*;

class Solution {
    Map<String, Integer> map;
    int ptr = 0;
    int answer = 0;
    public int solution(String[] want, int[] number, String[] discount) {
        map = new HashMap();

        for(int i = 0; i < 10; i++) {
            map.put(discount[i], map.getOrDefault(discount[i], 0) + 1);
        }

        while(9 + ptr < discount.length) {
            if (check(want, number))
                answer++;
            slide(discount);
        }
        return answer;
    }

    public boolean check(String[] want, int[] number) {
        for(int i = 0; i < want.length; i++) {
            if(!map.containsKey(want[i]) || map.get(want[i]) - number[i] > 0)
                return false;
        }
        return true;
    }

    public void slide(String[] discount) {
        map.put(discount[ptr], map.get(discount[ptr]) - 1 > 0 ? map.get(discount[ptr]) - 1 : 0);
        if(9 + ++ptr < discount.length)
            map.put(discount[9 + ptr], map.getOrDefault(discount[9 + ptr], 0) + 1);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.solution(new String[]{"apple"}, new int[] {10}, new String[] {"banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"});
    }
}