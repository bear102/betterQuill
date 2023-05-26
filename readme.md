# **betterQuill**

betterQuill is a python script that improves quill.org, a free online ELA learning tool.
<br><br>

## **Main features**
1. get answers
2. concept explanation
3. quality of life tools
<br><br>


## Table of Contents
- [**betterQuill**](#betterquill)
  - [**Main features**](#main-features)
  - [Table of Contents](#table-of-contents)
  - [**Example**](#example)
  - [**Usage**](#usage)


<br><br>

## **Example**

**Ok so lets say I am doing some Quill and learning my english, and then, I get to a problem that I am not sure about. I dont want to get this question wrong because then I would have to do the entire lesson again (very annoying)**

<br><br>

<img src="https://github.com/bear102/betterQuill/blob/main/images/Screenshot%202023-05-26%20133724.png" alt="first">

<br><br>

**Now what I can do is, `ctrl + alt + u` and then boom, you have the answer and a detailed explanation.**

<br><br>

<img src="https://github.com/bear102/betterQuill/blob/main/images/Screenshot%202023-05-26%20134058.png" alt="first"  >
<br><br>

**If you wanted to, you could even do `ctrl + alt + m` to directly have the answer move to the text box, and then submit it.**
**now you can make corrections or just submit and go on to the next question by hitting the \` symbol (top left of keyboard under escape key)**
<br><br>

***
<br><br>

**The `connect`, `grammar`, and `evidence` sections are pretty similar. Lets try a `proofreading` one The proofreading lessons typically give you a passage and ask you to make some changes and improvements.**
<br><br>

<img src="https://github.com/bear102/betterQuill/blob/main/images/Screenshot%202023-05-26%20135000.png" alt="first"  >

<br><br>

**by pressing `ctrl + alt + u` it gives you the correct passage with all the fixes highlighted:**

<br><br>

<img src="https://github.com/bear102/betterQuill/blob/main/images/Screenshot%202023-05-26%20134910.png" alt="first" >

<br><br>

**This allows you to check your work and even gives you a detailed explanation of why this change should be made. Hover over some higlighted text for an explanation.**







<br><br>

***
<br><br>

## **Usage**

1. if you havent installed python yet, install it
   
2. install all the requirements by executing
``` python
pip install -r requirements.txt
```
1. install chromedriver [here](https://chromedriver.chromium.org/downloads). To check which version of chrome you have installed, click the 3 dots at the top right > help > about google chrome
   
2. extract the chromedriver zip file and in the  `main.py` file change the chrome_driver_path to the path to your chromedriver

``` python
chrome_driver_path = r"path\to\chromedriver.exe"
```

5. open up a quill activity and copy the link, here are some examples (notice the type of lesson: grammar, connect, evidence, and proofreader. These are the only ones available right now)
```
https://www.quill.org/grammar/#/play/sw/?activities=30&student=DN39euJiwBtn3O4twU8RNA&uid=u7uHk9U_4Bfc64knFYPrJA

https://www.quill.org/connect/#/play/lesson/2e04ef36-ceea-4544-b7c7-751f89fc2b34?activities=72&student=5Z3rQjpCjqyKVoy7RMM7rQ

https://www.quill.org/evidence/#/play?activities=7&session=mxF8oN-uMke2qUsqGII-_g&uid=186

https://www.quill.org/proofreader/#/play/pf?activities=18&student=OCYZvCF_r_aB7yPSuJas9A&uid=VolwH12xgS732exLTniUDQ
```

6. go back into `main.py` and change the example url to your url
``` python
url = "https://www.quill.org/evidence/#/play?activities=6&session=iNLVUwqXmWJpqDAokZ-SaA&uid=171"
```

7. Run the python script.

8. you can execute a few commands
  - **ctrl + alt + h**: copies the question text into the input box so you dont have to retype the entire thing
  - **ctrl + alt + u**: gets the answer to the question and the explanation (you dont have to answer the question to get the answer. Note: this feature is designed for you to check your work without having to mess up and redo the entire lesson)
  - **ctrl + alt + m**: gets the answer and explanation and then copies the answer into the text box so it can be easily submitted. (note this does not currently work for the 'proofreader' lessons)
  - **ctrl v**: will allow you to paste text into the box (quill disables this by default)
  - **\`**: located at the top right of your keyboard under the escape key. This will allow you to repeatedly hit it to continue on to the next question. (quill disables this by default)


***



