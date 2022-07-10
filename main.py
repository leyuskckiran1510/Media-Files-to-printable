import sys
import subprocess as sp
import bin
import os
import shutil



def photo(file,size,bw,out):
    w, h = size.split('x')
    a = bin.Run(file,int(w),int(h))
    if out=='Console':
        if bw:
            print(a.BW())
        else:
            print(a.RGB())
    else:
        output = open(f"{out}", "a")
        if bw:
            output.write(a.BW())
        else:
            output.write(a.RGB())
        print("Now you can print the media files in the folder 'seq'")
        print("Conversion completed successfully!\n" * 2)
        print("Or you can print the media files in the folder 'seq-{file.split('.')[0]}'")


def video(file,fps,size,bw,out):
    dir=''
    print(str(os.listdir()))
    if "seq" in os.listdir():
        os.mkdir(f"seq-{file.split('.')[0]}")
        dir=f"seq-{file.split('.')[0]}"
    elif "seq" not in os.listdir():
        os.mkdir("seq")
        dir="seq"
    cmd=f'ffmpeg -i {file} -vf fps={fps} ./{dir}/img%03d.png'
    try:
        a = sp.check_output(cmd,shell=True,stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        a = e.output.decode("utf-8").strip().split("\n")[-1]
        print('Error: ffmpeg failed to convert video to images \nError ===> ',a)
        if "not found" in a:
            print("If you haven't installed ffmpeg, please install it from https://www.ffmpeg.org/download.html")
            print("and try again.")
        if "No such file or directory" in a:
            print("The video file you specified does not exist. please check again or is it a valid video file/path?")
    print("Video converted to images successfully!\n"*2)
    print("Now Media Files to printable media files conversion is in progress...")
    if out=='Console':
        w, h = size.split('x')
        for i in range(1,len(os.listdir(dir))+1):
            a = bin.Run(f"{dir}/img{i:03d}.png",int(w),int(h))
            if bw:
                #Ansi code for clear screen and move cursor to the top of the screen
                print(f"\x1b[2J\x1b[1;1H",end='\r')
                # printing actual image 
                print(a.BW(),end='\r')
            else:
                #Ansi code for clear screen and move cursor to the top of the screen
                print(f"\x1b[2J\x1b[1;1H",end='\r')
                #printing actual image
                print(a.RGB(),end="\r")

    else:
        w, h = size.split('x')
        for i in range(1, len(os.listdir(dir)) + 1):
            a = bin.Run(f"{dir}/img{i:03d}.png", int(w),int(h))
            output = open(f"{out}", "a")
            if bw:
                output.write(a.BW())
            else:
                output.write(a.RGB())
        print("Now you can print the media files in the folder 'seq'")
        print("Conversion completed successfully!\n"*2)
        print("Or you can print the media files in the folder 'seq-{file.split('.')[0]}'")

    #os.rmdir(f"{dir}")
    shutil.rmtree(f"{dir}")


    #a = sp.call(cmd,shell=True)

if __name__ == '__main__':
    argvs = sys.argv[1:]
    bw = False
    vid = False
    size='50x50'
    out='Console'
    fps=30
    if("-h") in argvs:
        print("""
        -h : showss the help message and usage with some examples 
        -v : shows the version of the program and exits
        -i : input file
        -r : resize the image to given size (default: 50x50)
        -vid : create a video from the images
        -bw: convert the image to black and white
        -rgb : convert the image to rgb
        -o : output string to file no printing to screen
        -fps : frames per second of the video use with -vid
        
        example:
        python main.py -i input.jpg -r 100x100 -bw #convert the image to black and white and resize it to 100x100
        python main.py -i input.jpg -rgb #convert the image to rgb and uses default 50x50 size
        python main.py -i input.mp4 -vid -bw #create a video from the images and convert the image to black and white
        python main.py -i input.mp4 -vid -rgb #create a video from the images and convert the image to rgb
        python main.py -i input.mp4 -vid -r 100x100 -bw #create a video from the images and convert the image to black and white and resize it to 100x100
        python main.py -i input.mp4 -vid -rgb -o file.txt #creats a dump of strings separated by new line to file.txt
        """)
    elif ("-v") in argvs:
        print("""
        Media files to printable version 0.1
        """)
    elif ("-i") not in argvs:
        print("Please provide an input file using '-i filenam' or use -h for help!")
    else:
        b = argvs.index("-i")
        try:
            file = argvs[b+1]
        except:
            print("Please provide an input file or use -h for help!")
        if file.split(".")[-1] in ["jpg","jpeg","png","gif","bmp","tiff","tif","webp","mp4"]:
            if ("-r") in argvs:
                size = argvs[argvs.index("-r")+1]
            if ("-bw") in argvs:
                bw = True
            if ("-rgb") in argvs:
                bw = False
            if ("-vid") in argvs:
                vid = True
                if file.split(".")[-1] != "mp4":
                    print("Please provide a video file! (mp4)\n -h for help\n Exiting...")
                if ("-fps") in argvs:
                    fps = argvs[argvs.index("-fps")+1]
                else:
                    fps = "30"
            if ("-o") in argvs:
                try:
                    out = argvs[argvs.index("-o")+1]
                except:
                    print("Please provide an output file! or remove -o to print on console/terminal\n -h for help\n Exiting...")
            print("file:-", file, " Ouput_Size:-", size, "   Is_BW:-", bw, "  Is_Video:-", vid, "   Print_To:-", out)
        else:
            print("Please provide a valid file! like jpg/png/mp4 ... \n -h for help\n Exiting...")


    if vid:
        video(file,fps,size,bw,out)
    else:
        photo(file,size,bw,out)

