# Media-Files-to-printable
Convert your images or pictures into printable character sho that you  can print your pictures in terminal just by using defaulf print function



##How to use
1) Download or clone the repo to your machine
2) create a virtual environmaet or not it's your choice
`
python -m venv environment_name
`
2.1)activate the environment if you have created one
`source ./environment_name/bin/activate ` for linux and macs
` ./environment_name/Scripts/activate.bat ` for windows

3) now install the requirements files
` pip install -r requirenments.txt`
4)run the code as
` python main.py -i input.jpg

example:
        python main.py -i input.jpg -r 100x100 -bw #convert the image to black and white and resize it to 100x100
        python main.py -i input.jpg  #convert the image to rgb and uses default 50x50 size
        python main.py -i input.mp4 -vid -bw #create a video from the images and convert the image to black and white
        python main.py -i input.mp4 -vid  #create a video from the images and convert the image to rgb
        python main.py -i input.mp4 -vid -r 100x100 -bw #create a video from the images and convert the image to black and white and resize it to 100x100
        python main.py -i input.mp4 -vid -o file.txt #creats a dump of strings separated by new line to file.txt

`
5) like other's you don't have to worry about the position of arguments and the texts for example
`
python main.py -i input.jpg #convert the image to rgb and uses default 50x50 size -o file.txt
python main.py -i input.jpg  -o file.txt
`
both the above code will execute 
6)now you can use it in your code for prinitng pictures in your terminal

# Want's to change the image to any other images
Easy! just change the input.jpg from above codes to your files path or name
# Note the image name must be .jpeg/.png/ .wepb/ .bmp and video must be .mp4 yes it supports other video formats also but I have reomved that 
function to prevent any errors

# sample of executed code in pycharm you can use any other interpreater
[![Visit youtube for more](https://i9.ytimg.com/vi/fhQ3AGA-e-E/mq2.jpg?sqp=CJiYsJIG&rs=AOn4CLAIBompMgTg87k8ywQ1-8SPyD5_Og)](https://www.youtube.com/watch?v=fhQ3AGA-e-E "asciirender")




