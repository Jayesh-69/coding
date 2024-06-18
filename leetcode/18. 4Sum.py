class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        a.sort()
        res=[]
        for i in range(len(a)-2):
            for j in range(len(a)-1,i+2,-1):
                k=i+1
                l=j-1
                while k<l:
                    s=a[i]+a[j]+a[k]+a[l]
                    if [a[i],a[k],a[l],a[j]] not in res and s==target:
                        res.append([a[i],a[k],a[l],a[j]])
                        k+=1
                        l-=1
                    elif s>target:
                        l-=1
                    else:
                        k+=1
        return res