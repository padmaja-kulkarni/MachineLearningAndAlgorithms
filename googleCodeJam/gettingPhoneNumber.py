# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:16:39 2016
@author: kulkarni
"""
import numpy as np
from collections import Counter
import random

class getPhoneNumber():     
    
    def __init__(self):
       self.numbers = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
       self.prefered_num_seq = ['ZERO','TWO', 'FOUR', 'SIX','EIGHT']
       self.secondary_seq =  np.array(['ONE', 'THREE','FIVE','SEVEN', 'NINE']) 

    def count_accurances(self, strng, letter):    
        counter = Counter(strng)
        return(counter[letter])
        

    def check_all_letter_occurance(self, strng, substrng):
        substrng_letrs = list(substrng)
        str_ltrs = list(strng)
        count_arr = True
        for i in range(len(substrng_letrs)):
            if self.count_accurances(strng, substrng_letrs[i])>0:
                str_ltrs.remove(substrng_letrs[i])
                strng = "".join(str_ltrs)
                continue
            if self.count_accurances(strng, substrng_letrs[i]) ==0:
                count_arr = False
        return count_arr

    def delete_substring(self, strng, substrng):
        substrng_letrs = list(substrng)
        str_ltrs = list(strng)
        for i in range(len(substrng_letrs)):
            if self.count_accurances(strng, substrng_letrs[i])>0:
                str_ltrs.remove(substrng_letrs[i])
                strng = "".join(str_ltrs)
        return strng
        
    def getTheNumber(self, inpt):
        ph_nums = []
        itr = int(len(inpt)/3)
        for i in range(itr):
            for j in range(len(self.prefered_num_seq)):
                if(self.check_all_letter_occurance(inpt, self.prefered_num_seq[j])):
                    inpt = self.delete_substring(inpt, self.prefered_num_seq[j])
                    ph_nums.append(self.prefered_num_seq[j])            
        itr = int(len(inpt)/3)        
        for i in range(itr):       
            nums = []
            random.shuffle(self.secondary_seq) 
            temp_input = inpt
            for k in range(itr):
                for j in range(len(self.secondary_seq)):
                    if(self.check_all_letter_occurance(temp_input, self.secondary_seq[j])):
                        temp_input = self.delete_substring(temp_input, self.secondary_seq[j])
                        nums.append(self.secondary_seq[j]) 
                if len(temp_input) == 0:
                    for p in range(len(nums)):
                        ph_nums.append(nums[p])
                    break
            if len(temp_input) == 0:
                break
        idx = np.array([],dtype =int)     
        for i in range(len(ph_nums)):
            idx = np.append(idx, self.numbers.index(ph_nums[i]))   
        idx = np.sort(idx).astype(str)
        idx = "".join(idx)
        return idx
        
if __name__ == '__main__':
    getNum = getPhoneNumber()
    data = np.genfromtxt("A-large-practice.in",dtype='str')  
    data = data[1:]
    myfile = open('output_large.txt', 'w')
    for i in range(len(data)):
        if i ==0:
            myfile.writelines("Case #%d:  %-*s" % (i+1,10,  getNum.getTheNumber(data[i])))
        else:
             myfile.writelines("\nCase #%d:  %-*s" % (i+1,10,  getNum.getTheNumber(data[i])))       
        #print ("Case #%d:  %-*s" % (i+1,10,  getNum.getTheNumber(data[i])))
    myfile.close()
   