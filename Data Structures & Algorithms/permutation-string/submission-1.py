class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1>len_s2:
            return False
        
        def check_freq(sub_str:str):
            feq = {}
            for i in sub_str:
                feq[i]=feq.get(i,0)+1
            return feq
        j=0

        s1_feq = check_freq(s1)
        while j<len_s2:
            s2_sub_feq = check_freq(s2[j:j+len_s1])
            if s1_feq==s2_sub_feq:
                return True
            
            j+=1
        return False


        