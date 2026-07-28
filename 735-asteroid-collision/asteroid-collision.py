class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack=[]
        n=len(arr)

        for i in range(n):
            if stack:
                if stack[-1]>0 and arr[i]>0:
                    stack.append(arr[i])
                
                elif stack[-1]>0 and arr[i]<0:
                    while stack and stack[-1] > 0 and abs(arr[i]) > abs(stack[-1]):
                        stack.pop()
                    
                    if not stack or stack[-1] < 0:
                        stack.append(arr[i])
                    
                    elif abs(stack[-1])==abs(arr[i]):
                        stack.pop()
                    
                else:
                    stack.append(arr[i])
                        
            else:
                stack.append(arr[i])
        return stack

                    
