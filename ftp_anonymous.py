import ftplib

def testAnonymousLogin(hostname):
        try:
                ftp = ftplib.FTP(hostname)
                ftp.login('anonymous', 'test@test.com')
                print('\n[*] ' + str(hostname) + 'Anonymous Login Success. ')
                ftp.quit()
                return True
        except Exception, e:
                print ('\n[-] ' + str(hostname) + 'Anonymous Login Failed. ')
                return False

host = print('Enter a hostname')
testAnonymousLogin(host)
