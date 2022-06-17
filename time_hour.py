def convert(s):
    
    if(s[8:10]=='AM'):
         if(s[:2] == '12'):
            return '00'+s[2:]
         else:
            return s[:8]
    if(int(s[:2])<12 ):
        return (str(12+int(s[:2]))+s[2:8])
    else:
        return s[:8]

    
        
    
s=input()
print(convert(s))
