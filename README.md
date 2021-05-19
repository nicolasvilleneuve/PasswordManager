## PasswordManager
A GUI with the ability to generate passwords for you and store them in a file for you.

## Description
The following app is very straight forward. 
You simply run the code, which will in turn, launch a GUI.

There are several fields for you to fill in:
Firstly, Website (Fig1), which is meant to make it so the website for which you are storing information is stored as such, 
but also to make that data accessible if you want to search for it (Fig 2) (which you can do by only filling in the website in the Website text box and pressing search, which will make
the credentials for that website pop up in a prompt window). 

<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure1.png" alt="Figure 1">
Figure 1. Website entry field boxed in red. 
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure2.png" alt="Figure 2">
Figure 2. Search button boxed in red. 
<br />
Secondly, you fill in your desired username in the Email/Username box (exemplified by Fig 3, below). 
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure3.png" alt="Figure 3">
Figure 3. The username/email text box boxed in red. 
<br />
Then, you fill in your desired password (Fig 4, below), OR, if you would like a STRONG password generated for you, you can press the "Generate Password" button (exemplified by Fig. 5, below). 
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure4.png" alt="Figure 4">
Figure 4. Password text box boxed in red. 
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure5.png" alt="Figure 5">
Figure 5. Generate password button boxed in red. 
<br />
After you have filled in all the necessary text fields, you can press add (exemplified by Figure 6) to store that information to a database (which will be named 'passwords.txt').
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure6.png" alt="Figure 6">
Figure 6. The add button boxed in red. 
<br />
In this way, your passwords will be securely stored, so long as you dont have a hacker actively controlling you computer or having access to your files. 
<br />
If you did not fill in all of the text fields, however, you will get an error prompt window, telling you that you need to fill in all of the fields in order to successfully save your data. Such a case may be denoted by Figure 7, below. 
<br />
<img src="https://github.com/nicolasvilleneuve/PasswordManager/blob/main/figures/Figure7.png" alt="Figure 7">
Figure 7. Prompt in the case of all the fields not being filled in. 
<br />
## Usage
You can freely access this app so long as you have a version of python 3 (this was made in python 3.9.1), the tkinter module, the random module, the json module, and the images from the images folder of the presenr repository. With those, you should simply be able to run the code and have a visually-appeasing timer to hold you accountable for/encourage your productivity. 

## Contributing / Support
If you would like to create a PULL request, please feel free. Whether the intent be to pilfer from the code as you like some elements of the app, or to suggest improvements, you are most welcome to. If the changes are to be major, however, please open an issue first so we can discuss if/what you would like to change. Should you have a problem in doing so, please feel free to let me know (my email is on my website so please find it there in case it has changed since writing this).

##License
MIT License

Copyright (c) 2021 Nicolas Villeneuve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




