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
