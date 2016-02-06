import subprocess
#remove sudo from cmd -> line 4

def get_used_iplist(interface='unspecified', netaddress='unspecified'):

    #Building the bash command to scan used IP's
    cmd = ['arp-scan']
    if interface != 'unspecified':
        cmd = cmd + str("-I "+interface).split()

    if netaddress != 'unspecified':
        cmd.append(netaddress)
    else:
        cmd.append('-l')


    used_iplist = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output = used_iplist.communicate()[0]
    return output
