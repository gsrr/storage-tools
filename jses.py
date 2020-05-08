import sys

CMD_MAP = {
        0x0e : {"key" : "download_microcode", "desc" : "Download Microcode"},
}

def display_output(order, output):
    print 
    print "-" * 30
    for key in order:
        print "%s : %s"%(key, output[key])




def compile_download_microcode(cmd, arr):
    order = ["command"]
    output = {
        "command" : cmd["desc"]
    }
    display_output(order, output)
    
def compile():
    msg = sys.argv[2]
    arr = [int(x, 16) for x in msg.split(",")]
    cmd = arr[0]
    subf = getattr(sys.modules[__name__], "compile_" + CMD_MAP[cmd]["key"])
    subf(CMD_MAP[cmd], arr)

def resort():
    msg = sys.argv[2]
    arr = msg.split(",")
    for i in xrange(len(arr)):
        if i % 16 == 0:
            print
        elif i % 8 == 0:
            print " ",
        print arr[i],



def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()

if __name__ == "__main__":
    main()
