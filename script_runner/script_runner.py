
import os
import time

def script_runner(script,thereshold,interval):


        
        for _ in range(thereshold):
         
            script_result = openFile(script)
            if script_result==0:
                return 0
            else :
                if _==thereshold-2:
                    break
                else:
                    time.sleep(interval)
                
        return 1
   

        


def openFile(script):
    return os.system(script)