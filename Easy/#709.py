class Solution:
    def toLowerCase(self, str: str) -> str:

        capitalDict = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'}
        
        newStr = ""
        for i in range(len(str)):
            if str[i] in capitalDict:
                newStr += capitalDict[str[i]]
            else:
                newStr += str[i]
        return newStr