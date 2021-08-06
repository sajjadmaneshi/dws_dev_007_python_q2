from os import environ

class Config:

    ENV= environ.get('TEST_ENV','production')
    DEBUG=int(environ.get('TEST_DEBUG',"0"))
    COMMAND = environ.get('‫‪DWS_TESTER_COMMAND‬‬',"start text.txt") 
    THERESHOLD = int(environ.get('‫‪DWS_TESTER_THRESHOLD‬‬',"4"))
    INTERVAL=int(environ.get('‫‪DWS_TESTER_INTERVAL','5'))

