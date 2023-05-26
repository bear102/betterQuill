from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput import keyboard
import pyperclip
import requests
import json
import re
from threading import Thread



# ------------------------------------------------------ change these values ------------------------------------------------------

chrome_driver_path = r"path\to\chromedriver.exe"

url = "https://www.quill.org/proofreader/#/play/pf?activities=18&student=gqmn_MExofjROonIvgmyGw&uid=afbb2b83-fa5d-414c-9c5c-a633fb2f012f"

# ------------------------------------------------------ change these values ------------------------------------------------------


start_index = url.find("quill.org/") + len("quill.org/")
end_index = url.find("/", start_index)

if start_index != -1 and end_index != -1:
    section = url[start_index:end_index]
    assignmentType = section
else:
    print("Section not found in URL")



service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)
html = """
<style>
    #instructions,
    #answer {
        background-color: lightblue;
        display: flex;
        justify-content: center;
        width: fit-content;
        border: 3px solid black;
        border-radius: 5px;
        padding: 40px;
        display: flex;
        flex-direction: column;
    }

    #myDiv {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
    }
    .correctHighlight{
        background-color: orange;
    }
</style>

    <div id="answer" style="padding: 20px; font-weight: bolder">    <label for="answer">Check Your Answer:</label>
</div>

<div id="instructions" style="margin-bottom: 50px; margin-top: 30px"></div>
"""

htmlE = """
<style>
    #instructions,
    #answer {
        background-color: lightblue;
        display: flex;
        justify-content: center;
        width: fit-content;
        border: 3px solid black;
        border-radius: 5px;
        padding: 40px;
        display: flex;
        flex-direction: column;
    }

    #myDiv {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
    }
</style>

    <div id="answer" style="padding: 20px; font-weight: bolder">    <label for="answer">Check Your Answer:</label>
</div>
"""


htmlP = """
<style>
    #instructions,
    #answer {
        background-color: lightblue;
        display: flex;
        justify-content: center;
        width: fit-content;
        border: 3px solid black;
        border-radius: 5px;
        padding: 40px;
        display: flex;
        flex-direction: column;
    }

    #myDiv {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin-top: 30px;
    }
    .correctHighlight{
        background-color: orange;
    }
</style>

    <div id="answer" style="padding: 20px; font-weight: bolder">    <label for="answer">Check Your Answer:</label>
</div>

<div id="instructions" style="margin-bottom: 50px; margin-top: 30px" ><strong>Hover over the Orange phrases for an explanation<br></strong></div>
"""









# ++++++++++++++++++++++++++++++++ Grammar Section ++++++++++++++++++++++++++++++++


# ////////////////////////// answersGrammar \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def getAnswersG(correctNum):
    answersURL = 'https://www.quill.org/api/v1/active_activity_sessions/'+student_value+'.json'
    response = requests.get(answersURL)
    if response.status_code == 200:
        answers = response.text
        ans = json.loads(answers)
        ans = ans['questionSet']
        answerText = ans[correctNum]['answers'][0]['text']
        return answerText

    else:
        print(f"Error: {response.status_code}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ answersGrammar ////////////////////////////



# ////////////////////////// directionsGrammar \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def getDirectionsG(uid_value):
    directionsURL = 'https://www.quill.org/api/v1/lessons/'+uid_value+'.json'
    response = requests.get(directionsURL)
    if response.status_code == 200:
        directionsPrev = response.text
        directions = json.loads(directionsPrev)

        htmlDir = directions['landingPageHtml']
    else:
        print(f"Error: {response.status_code}")
        htmlDir = "not avaiable instructions"
    return htmlDir

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ directionsGrammar ////////////////////////////


if assignmentType == 'grammar':
    start_index = url.index('student=')
    end_index = url.index('&uid', start_index)

    student_value = url[start_index + len('student='):end_index]

    uid_start_index = url.index('&uid=') + len('&uid=')
    uid_value = url[uid_start_index:]

    print("Student Value:", student_value)
    print("UID Value:", uid_value)
    directions = getDirectionsG(uid_value)



# ++++++++++++++++++++++++++++++++ Grammar Section ++++++++++++++++++++++++++++++++


















# ++++++++++++++++++++++++++++++++ Connect Section ++++++++++++++++++++++++++++++++


# ////////////////////////// answerID \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def getQuestionIdC(correctNum):

    answersURL = 'https://www.quill.org/api/v1/lessons/'+lesson_id+'.json'
    response = requests.get(answersURL)
    if response.status_code == 200:
        answers = response.text
        ans = json.loads(answers)
        ans = ans['questions']
        answerText = ans[correctNum]['key']
        return answerText

    else:
        print(f"Error: {response.status_code}")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ answerID ////////////////////////////





# ////////////////////////// answerConnect \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def getAnswerC(iden):
    answerURL = 'https://cms.quill.org/questions/' + iden + '/multiple_choice_options'
    response = requests.get(answerURL)
    if response.status_code == 200:
        answersAll = response.text
        answersAll = json.loads(answersAll)
        correctAnswer = answersAll[0]['text']
        return correctAnswer
    else:
        print(f"Error: {response.status_code}")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ answerConnect ////////////////////////////



if assignmentType == 'connect':

    start_index = url.find('lesson') + len('lesson') + 1
    end_index = url.find('activities')

    if start_index != -1 and end_index != -1:
        lesson_id = url[start_index:end_index]
    else:
        print('Lesson ID not found in the URL.')



# ////////////////////////// direcitonsConnect \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    directionsURL = 'https://www.quill.org/api/v1/lessons/'+lesson_id+'.json'
    response = requests.get(directionsURL)
    if response.status_code == 200:
        directionsPrev = response.text
        directions = json.loads(directionsPrev)

        htmlDir = directions['landingPageHtml']
    else:
        print(f"Error: {response.status_code}")
        htmlDir = "not avaiable instructions"

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ direcitonsConnect ////////////////////////////




# ++++++++++++++++++++++++++++++++ Connect Section ++++++++++++++++++++++++++++++++











# ++++++++++++++++++++++++++++++++ evidence Section ++++++++++++++++++++++++++++++++



# ////////////////////////// answerEvidence \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def getAnswerE(conj, uid):
    answersURL = 'https://www.quill.org/api/v1/evidence/activities/' + str(uid)
    request = requests.get(answersURL)

    respText = request.text
    respText = json.loads(respText)
    for i in range (len(respText['prompts'])):
        if respText['prompts'][i]['conjunction'] == conj:
            return respText['prompts'][i]['text'] + " " + respText['prompts'][i]['first_strong_example']
    else:
        return 'Answer Not Found :('
    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ answerEvidence ////////////////////////////



if assignmentType == 'evidence':
    start_index = url.find("uid=")

    if start_index != -1:
        # Extract the substring starting from the "uid=" parameter
        uid_substring = url[start_index + 4:]

        # Find the end index of the uid value
        end_index = uid_substring.find("&")
        if end_index != -1:
            # Extract the uid value
            uid = uid_substring[:end_index]
        else:
            # If no '&' character is found, consider the uid value until the end of the URL or fragment identifier
            fragment_index = uid_substring.find("#")
            if fragment_index != -1:
                uid = uid_substring[:fragment_index]
            else:
                uid = uid_substring
        uid = int(uid)
    else:
        uid = None
    


# ++++++++++++++++++++++++++++++++ evidence Section ++++++++++++++++++++++++++++++++

    












# ++++++++++++++++++++++++++++++++ proofreader Section ++++++++++++++++++++++++++++++++


if assignmentType == 'proofreader':
    start_index_student = url.find("student=")
    if start_index_student != -1:
        student_substring = url[start_index_student + 8:]

        end_index_student = student_substring.find("&")
        if end_index_student != -1:
            student = student_substring[:end_index_student]
        else:
            student = student_substring
    else:
        student = None

    start_index_uid = url.find("uid=")
    if start_index_uid != -1:
        uid_substring = url[start_index_uid + 4:]

        end_index_uid = uid_substring.find("&")
        if end_index_uid != -1:
            uid = uid_substring[:end_index_uid]
        else:
            uid = uid_substring
    else:
        uid = None

    print("Student:", student)
    print("UID:", uid)

# ////////////////////////// OGPassageProofreader \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    url = 'https://www.quill.org/api/v1/lessons/' + uid + '.json'
    request = requests.get(url)
    response = request.text
    response = json.loads(response)
    completeCorrectText = ''
    conceptIDList = []

    passageOG = response['passage']

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ OGPassageProofreader ////////////////////////////



# ////////////////////////// getCorrectPassageProofreader \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    url = 'https://www.quill.org/api/v1/active_activity_sessions/' + student + '.json'
    request = requests.get(url)
    response = request.text
    response = json.loads(response)
    replaceWordList = []
    counter = 0
    psg = response['passage']
    for i in range(len(psg)):
        for b in range(len(psg[i])):
            if 'conceptUID' in psg[i][b]:
                conceptIDList.append(psg[i][b]['conceptUID'])
                replaceWordList.append(f"<span class='correctHighlight' data-index = '{conceptIDList[counter]}'>" + psg[i][b]['correctText'] + "</span>")
                counter +=1


    pattern = r"(\{[^}]+\})"
    def replace(match):
        global replaceWordList
        return replaceWordList.pop(0)
    

    newPassage = re.sub(pattern, replace, passageOG)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ getCorrectPassageProofreader ////////////////////////////



# ++++++++++++++++++++++++++++++++ proofreader Section ++++++++++++++++++++++++++++++++

    
















def exeScript():

# ////////////////////////// Grammar \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'grammar':
        questionNum = driver.find_element(By.XPATH, "//div[@class='progress-bar-container']//p")
        text = questionNum.text
        number = text.split(" ")[0]  
        correctNum = int(number)-1
        print(correctNum)  
        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(html)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';



        var qSec = document.querySelector('div.question-section');
        qSec.style.display = 'flex';
        qSec.style.flexDirection = 'column';
        qSec.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""
        var newDiv = document.createElement('div');
        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = `{directions}`;

        var parentElement = document.getElementById('instructions'); 
        parentElement.appendChild(newDiv);

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{getAnswersG(correctNum)}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
    """)
    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ Grammar ////////////////////////////






# ////////////////////////// connect \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


    if assignmentType == 'connect':
        questionNum = driver.find_element(By.XPATH, "//div[@class='progress-bar-container']//p")
        text = questionNum.text
        number = text.split(" ")[0]  
        correctNum = int(number)-1
        print(correctNum)  
        qID = getQuestionIdC(correctNum)
        correct = getAnswerC(qID)

        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(html)};

        var parentElement = document.getElementById('main-content'); 

        var buttonGroupElement = document.querySelector('div.question-button-group.button-group');
        buttonGroupElement.style.display = 'flex';
        buttonGroupElement.style.flexDirection = 'column';
        buttonGroupElement.appendChild(newDiv);

        """
                            
        );
        driver.execute_script(f"""
        var newDiv = document.createElement('div');
        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = `{htmlDir}`;

        var parentElement = document.getElementById('instructions'); 
        parentElement.appendChild(newDiv);

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{correct}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
    """)
        

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ connect ////////////////////////////




# ////////////////////////// evidence \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'evidence':
        element = driver.find_element(By.XPATH,'//div[@class="editor"]/p/u')
        print(element.text)

        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(htmlE)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';

        var appendTo = document.querySelector('div.attempts-and-button-container');
        appendTo.style.display = 'flex';
        appendTo.style.flexDirection = 'column';
        appendTo.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{getAnswerE(element.text,uid)}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
    """)
        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ evidence ////////////////////////////





# ////////////////////////// proofreader \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'proofreader':


        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(htmlP)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';

        var appendTo = document.querySelector('div#button-container');
        appendTo.style.display = 'flex';
        appendTo.style.flexDirection = 'column';
        appendTo.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.innerHTML = `{newPassage}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
        """)

        driver.execute_script(f"""
 function getConceptP(concID) {{
    var url = 'https://www.quill.org/api/v1/concepts.json';
    var request = new XMLHttpRequest();
    request.open('GET', url, false);
    request.send(null);

    if (request.status === 200) {{
        var requestText = request.responseText;
        var requestJSON = JSON.parse(requestText);

        for (var i = 0; i < requestJSON.concepts.length; i++) {{
            if (requestJSON.concepts[i].uid === concID) {{
                return requestJSON.concepts[i].explanation;
            }}
        }}
    }}

    return 'invalid concept id';
}}

            const indexSpans = document.querySelectorAll('.correctHighlight');
            indexSpans.forEach(span => {{
            span.addEventListener('mouseover', function() {{
                var existingDiv = document.getElementById('mdVI');
                if (existingDiv) {{
                    existingDiv.remove();
                }}
                const concID = this.getAttribute('data-index');
                console.log('concID:', concID);
                
                var mdVI = document.createElement('div');
                mdVI.id = 'mdVI';
                mdVI.className = 'myClass';
                mdVI.innerHTML = 'Explanation:<br>' + getConceptP(concID);

                var parentElement = document.getElementById('instructions'); 
                parentElement.appendChild(mdVI);
                
            }});
            }});
        """)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ proofreader ////////////////////////////

    print('Executed execScript()')
    return "exec script done"






def exeScriptA():

# ////////////////////////// Grammar \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'grammar':
        questionNum = driver.find_element(By.XPATH, "//div[@class='progress-bar-container']//p")
        text = questionNum.text
        number = text.split(" ")[0]  
        correctNum = int(number)-1
        print(correctNum)  
        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(html)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';



        var qSec = document.querySelector('div.question-section');
        qSec.style.display = 'flex';
        qSec.style.flexDirection = 'column';
        qSec.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""
        var newDiv = document.createElement('div');
        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = `{directions}`;

        var parentElement = document.getElementById('instructions'); 
        parentElement.appendChild(newDiv);

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{getAnswersG(correctNum)}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);



    """)
        input_selector = '[placeholder="Type your answer here."]'
        text_box = driver.find_element(By.CSS_SELECTOR, input_selector)
        text_box.send_keys(getAnswersG(correctNum))
    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ Grammar ////////////////////////////






# ////////////////////////// connect \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


    if assignmentType == 'connect':
        questionNum = driver.find_element(By.XPATH, "//div[@class='progress-bar-container']//p")
        text = questionNum.text
        number = text.split(" ")[0]  
        correctNum = int(number)-1
        print(correctNum)  
        qID = getQuestionIdC(correctNum)
        correct = getAnswerC(qID)

        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(html)};

        var parentElement = document.getElementById('main-content'); 

        var buttonGroupElement = document.querySelector('div.question-button-group.button-group');
        buttonGroupElement.style.display = 'flex';
        buttonGroupElement.style.flexDirection = 'column';
        buttonGroupElement.appendChild(newDiv);

        """
                            
        );
        driver.execute_script(f"""
        var newDiv = document.createElement('div');
        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = `{htmlDir}`;

        var parentElement = document.getElementById('instructions'); 
        parentElement.appendChild(newDiv);

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{correct}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);


    """)
        input_selector = '[placeholder="Type your answer here."]'
        text_box = driver.find_element(By.CSS_SELECTOR, input_selector)
        text_box.send_keys(correct)
        

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ connect ////////////////////////////




# ////////////////////////// evidence \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'evidence':            
        element = driver.find_element(By.XPATH,'//div[@class="editor"]/p/u')
        answer = getAnswerE(element.text,uid)
        print(element.text)

        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(htmlE)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';

        var appendTo = document.querySelector('div.attempts-and-button-container');
        appendTo.style.display = 'flex';
        appendTo.style.flexDirection = 'column';
        appendTo.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.textContent = `{answer}`;
        console.log(`{answer}`)

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
        """)

        original_text = driver.execute_script("""
        var editorElement = document.querySelector('.editor');
        var paragraphElement = editorElement.querySelector('p');
        var originalText = paragraphElement.textContent.trim();
        return originalText;
        """)
        added_text = answer[len(original_text):].strip()

        text_box = driver.find_element(By.CSS_SELECTOR, '.editor')
        text_box.send_keys(added_text)



        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ evidence ////////////////////////////





# ////////////////////////// proofreader \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    if assignmentType == 'proofreader':


        driver.execute_script(f"""
        var existingDiv = document.getElementById('myDiv');
        if (existingDiv) {{
            existingDiv.remove();
        }}
        var newDiv = document.createElement('div');

        newDiv.id = 'myDiv';
        newDiv.className = 'myClass';
        newDiv.innerHTML = {json.dumps(htmlP)};
        newDiv.style.display = 'flex';
        newDiv.style.flexDirection = 'column';
        newDiv.style.alignItems = 'center';

        var appendTo = document.querySelector('div#button-container');
        appendTo.style.display = 'flex';
        appendTo.style.flexDirection = 'column';
        appendTo.appendChild(newDiv);
        """
                            
        );
        driver.execute_script(f"""

        var newDiv2 = document.createElement('div');
        newDiv2.id = 'myDiv2';
        newDiv2.className = 'myClass';
        newDiv2.innerHTML = `{newPassage}`;

        var parentElement2 = document.getElementById('answer'); 
        parentElement2.appendChild(newDiv2);
        """)

        driver.execute_script(f"""
 function getConceptP(concID) {{
    var url = 'https://www.quill.org/api/v1/concepts.json';
    var request = new XMLHttpRequest();
    request.open('GET', url, false);
    request.send(null);

    if (request.status === 200) {{
        var requestText = request.responseText;
        var requestJSON = JSON.parse(requestText);

        for (var i = 0; i < requestJSON.concepts.length; i++) {{
            if (requestJSON.concepts[i].uid === concID) {{
                return requestJSON.concepts[i].explanation;
            }}
        }}
    }}

    return 'invalid concept id';
}}

            const indexSpans = document.querySelectorAll('.correctHighlight');
            indexSpans.forEach(span => {{
            span.addEventListener('mouseover', function() {{
                var existingDiv = document.getElementById('mdVI');
                if (existingDiv) {{
                    existingDiv.remove();
                }}
                const concID = this.getAttribute('data-index');
                console.log('concID:', concID);
                
                var mdVI = document.createElement('div');
                mdVI.id = 'mdVI';
                mdVI.className = 'myClass';
                mdVI.innerHTML = 'Explanation:<br>' + getConceptP(concID);

                var parentElement = document.getElementById('instructions'); 
                parentElement.appendChild(mdVI);
                
            }});
            }});
        """)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ proofreader ////////////////////////////

    print('Executed execScriptA()')
    return "exec script done"






# ////////////////////////// copy origional question text into box \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def find_paragraph_input():
    paragraph_selectors = [".draft-js.sentence-fragments", ".prompt"]
    input_selector = '[placeholder="Type your answer here."]'

    for selector in paragraph_selectors:
        paragraph_tags = driver.find_elements(By.CSS_SELECTOR, selector)
        if len(paragraph_tags) > 0:
            ptext = ''
            for paragraph in paragraph_tags:
                paragraph_text = paragraph.text
                ptext += paragraph_text

            ptext = ptext.replace('\n',' ')

            text_box = driver.find_element(By.CSS_SELECTOR, input_selector)
            return text_box, ptext

    raise Exception("Paragraph not found")



def copyFromText():
    try:
        text_box, ptext = find_paragraph_input()
        text_box.send_keys(ptext)
    except Exception as e:
        print(str(e)) 


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\ copy origional question text into box ////////////////////////////




def enter():
    try:
        btn = driver.find_element(By.CSS_SELECTOR, "button.quill-button.large.primary.contained.focus-on-light")
        btn.click()
    except:
        try:
            btn = driver.find_element(By.CSS_SELECTOR, "button.quill-button.focus-on-light")
            btn.click()
        except:
            pass 

def execScr():
    exeScript()

def execScrA():
    exeScriptA()

def paste():
    clipboard_content = pyperclip.paste()
    active_element = driver.switch_to.active_element
    active_element.send_keys(clipboard_content)


 



with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': copyFromText, # change these hotkeys if you want. This one takes the answer text and puts it into the input box. Allows for you to easily edit and saves time.
        '<ctrl>+<alt>+u': execScr, # change these hotkeys if you want. This one gets the answer and the directions (if available)
        '<ctrl>+<alt>+m': execScrA, # change these hotkeys if you want. This one gets the answer and the directions and copies it to the input box(if available)
        '<ctrl>+v': paste, # change these hotkeys if you want. This one allows you to paste
        '`':enter
        }) as h:
    h.join()


