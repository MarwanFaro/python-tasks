# task1
steps=input("enter the steps by spateted  :")
steps=steps.split()
step_list=list(map(int,steps))

highest_step=max(step_list)
lowest_step=min(step_list)
avg=sum(step_list)/len(step_list)
sorted_list=sorted(step_list,reverse=True)


print("the high step is : ",highest_step)
print("the low step is : ",lowest_step)
print("the average step is : ",avg)
print("the sorted list is : ",sorted_list)






