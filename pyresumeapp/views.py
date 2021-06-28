from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def renderResume(request):
    fname = request.GET.get('firstname')
    mname = request.GET.get('middlename')
    lname = request.GET.get('lastname')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    githublink = request.GET.get('githublink')
    linkedinlink = request.GET.get('linkedinlink')
    degree = request.GET.get('degree')
    university = request.GET.get('university')
    cgpa = request.GET.get('cgpa')
    classxii = request.GET.get('classxii')
    schoolxii = request.GET.get('schoolxii')
    percentagexii = request.GET.get('percentagexii')
    classx = request.GET.get('classx')
    schoolx = request.GET.get('schoolx')
    percentagex = request.GET.get('percentagex')
    languages = request.GET.get('languages').split(',')
    send_languages = ''
    for i in languages:
        send_languages += i.lstrip().rstrip()
        if languages.index(i) < len(languages)-1:
            send_languages += ', '

    frameworks = request.GET.get('frameworks').split(',')
    send_frameworks = ''
    for i in frameworks:
        send_frameworks += i.lstrip().rstrip()
        if frameworks.index(i) < len(frameworks)-1:
            send_frameworks += ', '

    itconstructs = request.GET.get('itconstructs').split(',')
    send_itconstructs = ''
    for i in itconstructs:
        send_itconstructs += i.lstrip().rstrip()
        if itconstructs.index(i) < len(itconstructs)-1:
            send_itconstructs += ', '

    dblanguage = request.GET.get('dblanguage').split(',')
    send_dblanguage = ''
    for i in dblanguage:
        send_dblanguage += i.lstrip().rstrip()
        if dblanguage.index(i) < len(dblanguage)-1:
            send_dblanguage += ', '

    operatingsystems = request.GET.get('operatingsystems').split(',')
    send_operatingsystems = ''
    for i in operatingsystems:
        send_operatingsystems += i.lstrip().rstrip()
        if operatingsystems.index(i) < len(operatingsystems)-1:
            send_operatingsystems += ', '

    developmenttools = request.GET.get('devlopmenttools').split(',')
    send_developmenttools = ''
    for i in developmenttools:
        send_developmenttools += i.lstrip().rstrip()
        if developmenttools.index(i) < len(developmenttools)-1:
            send_developmenttools += ', '

    familiarwith = request.GET.get('familiarwith').split(',')
    send_familiarwith = ''
    for i in familiarwith:
        send_familiarwith += i.lstrip().rstrip()
        if familiarwith.index(i) < len(familiarwith)-1:
            send_familiarwith += ', '


    # print("-------->>>", request.GET.get('projects'))
    projects = request.GET.get('projects').replace('[bold]', '[bold] ').replace('[/bold]', ' [/bold]').replace('[/link]', ' [/link]').split(',,,')
    
    # all_other_text = []
    # all_urls = []
    send_projects = []

    for project in projects:
        url_text = []
        other_text = []
        for word in project.split():
            if '[link' in word:
                end_link = word.index('"]')
                url_text = word[7:end_link]
                other_text.append('[link]')
                other_text.append(word[end_link+2:])
            else:
                other_text.append(word)

        # Joining link words starts
        cp = [] # connection points
        for word in other_text:
            if word == '[link]' or word == '[/link]':
                cp.append(other_text.index(word))

        # other_text[x[3:6] = [''.join(x[3:6])]]
        other_text[cp[0]+1:cp[1]] = [' '.join(other_text[cp[0]+1:cp[1]])]
        # Joining link words ends
            
        # print('url text : ', url_text)
        # print('other text : ', other_text)

        send_projects.append({'url_data': url_text, 'text_data': other_text})

    

    # Portfolio operations starts here...
    portfoliolinks = request.GET.get('portfoliolinks')
    send_portfoliolinks = []

    portfolio_links = portfoliolinks.replace('[bold]', '[bold] ').replace('[/bold]', ' [/bold]').replace('[/link]', ' [/link]').split(',,,')

    send_portfoliolinks = []

    for portfolio_link in portfolio_links:
        url_text = ''
        other_text = []
        for word in portfolio_link.split():
            if '[link' in word:
                end_link = word.index('"]')
                url_text = word[7:end_link]
                other_text.append('[link]')
                other_text.append(word[end_link+2:])
            else:
                other_text.append(word)


        # Joining link words starts
        cp = [] # connection points
        for word in other_text:
            if word == '[link]' or word == '[/link]':
                cp.append(other_text.index(word))

        other_text[cp[0]+1:cp[1]] = [' '.join(other_text[cp[0]+1:cp[1]])]
        # Joining link words end

        send_portfoliolinks.append({'url_data': url_text, 'text_data': other_text})
    

    otherdetails = request.GET.get('otherdetails')
    send_other_details = []
    for j in otherdetails.replace('[bold]', '[bold] ').replace('[/bold]', ' [/bold]').split(',,,'):
        send_other_details.append(j.split(' '))

    resume_data = {
        'fullname': fname.capitalize()+' '+mname[0].upper()+'. '+lname.capitalize(),
        'email': email,
        'phone': phone,
        'githublink': githublink.lstrip().rstrip(),
        'linkedinlink': linkedinlink.lstrip().rstrip(),
        'degree': degree,
        'university': university,
        'cgpa': cgpa,
        'classxii': classxii,
        'schoolxii': schoolxii,
        'percentagexii': percentagexii,
        'classx': classx,
        'schoolx': schoolx,
        'percentagex': percentagex,
        'languages': send_languages,
        'frameworks': send_frameworks,
        'itconstructs': send_itconstructs,
        'dblanguages': send_dblanguage,
        'operatingsystems': send_operatingsystems,
        'developmenttools': send_developmenttools,
        'familiarwith': send_familiarwith,
        # 'projects': all_other_text, # Project text
        # 'project_urls': all_urls, # Project Urls
        'projects': send_projects,
        'portfoliolinks': send_portfoliolinks,
        'otherdetails': send_other_details,
    }
    return render(request, 'renderresume.html', resume_data)

'''
After Graduation and learning technologies as a part of Self-Learning, I am seeking an opportunity which allows me to continue learning and updating my skills. As the Zen of Python says I will provide my best in writing high-efficient and easily readable codes as a Developer.
Vinay
Davda
vinaydavda7@gmail.com
+919537084223
BCA (2016-2019)
Marwadi University, Rajkot
6.57
Class XII (2016)
Nilkanth Commerce School
64.57
Class X (2014)
Nalanda Vidhyalaya
87.83
Python3,C++,HTML,CSS
OOPS,DBMS
Microsoft Visual Studio, Jupyter Notebook, Pycharm
Django,Flask,Boorstrap4,Kivy
MySQL
Linux,Windows,Mac,Android
Flask,C++,Java,JavaScript,PHP,Kivy,Wordpress,Inkscape





[bold][link="https://github.com/vinaydavda/Text-Utility"]Text Utility app in Django[/link][/bold] for various operations on text like uppercase-lowercase conversion, character count, etc.,,,
Working model of [bold][link="https://github.com/vinaydavda/Hamming-Code"]Hamming Code[/link][/bold] 1 bit Linear Error Correction in Python3,,,
[bold][link="https://github.com/vinaydavda/PyResume-Maker"]Resume Creator app[/link][/bold] using [bold]Django and Bootstrap4[/bold] which renders a Resume from user entered data




[link="https://www.hackerrank.com/vinaydavda7"]HackerRank[/link],,,
[link="https://drive.google.com/drive/folders/1jk0ZcvEGGfyF_amEX8ppHGCkqf9ykmpY?usp=sharing"]Certificates[/link]





Certificate for Completion of Python Training - [bold]IIT Bombay[/bold],,,Learned some basic concepts of [bold]Public-Private keys[/bold] and [bold]End-to-end Encryption[/bold] using Python in College,,,Attended one day workshop on [bold]Python and Machine Learning[/bold] - Smt. K.S.N. Kansagara Mahila College (Rajkot)
'''

'''
http://127.0.0.1:8000/renderresume/?objective=After+Graduation+and+learning+technologies+as+a+part+of+Self-Learning%2C+I+am+seeking+an+opportunity+which+allows+me+to+continue+learning+and+updating+my+skills.+As+the+Zen+of+Python+says+I+will+provide+my+best+in+writing+high-efficient+and+easily+readable+codes+as+a+Developer.&firstname=Vinay&middlename=Ketanbhai&lastname=Davda&email=vinaydavda7%40gmail.com&phone=%2B919537084223&degree=BCA+%282016-2019%29&university=Marwadi+University%2C+Rajkot&cgpa=6.57&classxii=Class+XII+%282016%29&schoolxii=Nilkanth+Commerce+School&percentagexii=64.57&classx=Class+X+%282014%29&schoolx=Nalanda+Vidhyalaya&percentagex=87.83&languages=Python3%2CHTML%2CCSS&frameworks=Django%2CFlask%2CBoorstrap4%2CKivy&itconstructs=OOPS%2CDBMS&dblanguage=MySQL&operatingsystems=Linux%2CWindows%2CMac%2CAndroid&devlopmenttools=Microsoft+Visual+Studio%2C+Jupyter+Notebook%2C+Pycharm&projects=Text+Utility+app+in+%5Bbold%5DDjango%5B%2Fbold%5D+for+various+operations+on+text+like+uppercase-lowercase+conversion%2C+character+count%2C+etc.%2C%2C%2CWorking+model+of+%5Bbold%5DHamming+Code%5B%2Fbold%5D+1+bit+Linear+Error+Correction+in+Python3%2C%2C%2C%5Bbold%5DResume+Creator+app%5B%2Fbold%5D+using+%5Bbold%5DDjango+and+Bootstrap4%5B%2Fbold%5D+which+renders+a+Resume+from+user+entered+data&portfoliolinks=Github%2Chttps%3A%2F%2Fgithub.com%2Fvinaydavda%2C%2C%2CHackerRank%2Chttps%3A%2F%2Fwww.hackerrank.com%2Fvinaydavda7%2C%2C%2CCertificates%2Chttps%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1jk0ZcvEGGfyF_amEX8ppHGCkqf9ykmpY%3Fusp%3Dsharing&otherdetails=Certificate+for+Completion+of+Python+Training+-+%5Bbold%5DIIT+Bombay%5B%2Fbold%5D%2C%2C%2CLearned+some+basic+concepts+of+%5Bbold%5DPublic-Private+keys%5B%2Fbold%5D+and+%5Bbold%5DEnd-to-end+Encryption%5B%2Fbold%5D+using+Python+in+College%2C%2C%2CAttended+one+day+workshop+on+%5Bbold%5DPython+and+Machine+Learning%5B%2Fbold%5D+-+Smt.+K.S.N.+Kansagara+Mahila+College+%28Rajkot%29&hobbies=Programming%2CSports%2CReading%2CVector+Art
'''

'''
Alert
List group
Table
'''

'''
{{ objective }} <br />
  {{ fname }} <br />
  {{ mname }} <br />
  {{ lname }} <br />
  {{ email }} <br />
  {{ phone }} <br />
  {{ degree }} <br />
  {{ university }} <br />
  {{ cgpa }} <br />
  {{ classxii }} <br />
  {{ schoolxii }} <br />
  {{ percentagexii }} <br />
  {{ classx }} <br />
  {{ schoolx }} <br />
  {{ percentagex }} <br />
  {{ languages }} <br />
  {{ frameworks }} <br />
  {{ itconstructs }} <br />
  {{ dblanguage }} <br />
  {{ operatingsystems }} <br />
  {{ devlopmenttools }} <br />
  {{ projects }} <br />
  {{ portfoliolinks }} <br />
  {{ otherdetails }} <br />
  {{ hobbies }}
'''