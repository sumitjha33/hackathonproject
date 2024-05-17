def productExceptSelf(self, nums, n):
        #code here
        prod=1
        flag=0
        
        for i in range(n):
            if nums[i]==0:
                flag+=1
            else:
                prod*=nums[i]
        
        for i in range(n):
            if flag>1:
                nums[i]=0
            elif flag==0:
                nums[i]=prod//nums[i]
            elif flag==1 and nums[i]!=0:
                nums[i]=0
            else:
                nums[i]=prod
                
        return nums