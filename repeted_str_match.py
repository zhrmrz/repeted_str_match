class Sol:
    def repeted_str_match(self,str1,str2):
        if str1 not in str2:
            return -1
        i=1
        while(True):
            if str2 in str1*i:
                return i
            i+=1

if __name__ == '__main__':
    p=Sol()
    print(p.repeted_str_match('abcd','cdabcdab'))
