

class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        m , n  = len(A), len(B)
        if m > n :
            m , n , A , B = n , m , B , A 
        n_min , n_max , half = 0, m , (m+n +1)//2 
        while n_min <= n_max:
            i = (n_min+n_max)//2
            j = half - i 
            if i >0 and A[i-1] > B[j]:
                n_max = i-1
            elif i < m and A[i] < B[j-1]:
                n_min = i+1
            else:

                if i == 0 : max_l = B[j-1]
                elif j == 0 :max_l = A[j-1]
                else: max_l = max(A[i-1],B[j-1])

                if (m+n)%2 == 1:
                    return max_l
                if i == m : min_r = B[j]
                elif j ==n : min_r = A[i]
                else: min_r = min(A[i],B[j])

                return (min_r+max_l) /2

if __name__ == "__main__":
    s  = Solution()
    A = [1,2,3]
    B = [2,3,4]
    res = s.findMedianSortedArrays(A,B)
    print(res)
