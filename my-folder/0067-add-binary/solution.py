class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = 0
        result = ""
        carry = 0        
        while a or b:
            a_res, b_res = "", ""
            if not a:
                a_res = "0"
            elif not b:
                b_res = "0"

            if not a_res:
                a_res = a[-1]
                a = a[:-1]
            
            if not b_res:
                b_res = b[-1]
                b = b[:-1]


            if a_res == "1" and b_res == "1":
                if carry >= 1:
                    f_res = "1"
                else:
                    carry += 1
                    f_res = "0"
            elif a_res == "0" and b_res == "0":
                if carry >= 1:
                    f_res = "1"
                    carry -= 1
                else:
                    f_res = "0"
            else:
                if carry >= 1:
                    f_res = "0"
                else:
                    f_res = "1"
            result = f_res + result

        while carry > 0:
            result = "1" + result
            carry -= 1
    

        return result
