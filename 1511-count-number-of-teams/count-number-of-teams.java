class Solution {
    public int numTeams(int[] rating) {
        int n = rating.length;
        int count = 0;

        for (int k = 0; k < n; k++) {
            for (int j = k + 1; j < n; j++) {
                for (int i = j + 1; i < n; i++) {

                    if ((rating[i] < rating[j] && rating[j] < rating[k]) ||
                        (rating[i] > rating[j] && rating[j] > rating[k])) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}