from xml.dom import minidom


def read():
    doc = minidom.parse('student-list.xml')
    root = doc.documentElement
    print(root)
    print(root.tagName)

    student_list = root.getElementsByTagName('student')
    for student in student_list:
        id = student.getAttribute('id')
        name = student.getElementsByTagName('name')[0].childNodes[0].data
        age = student.getElementsByTagName('age')[0].childNodes[0].data
        print('id={} name={} age={}'.format(id, name, age))


def create():
    doc = minidom.getDOMImplementation().createDocument(None, None, None)
    root = doc.createElement('studentList')
    doc.appendChild(root)

    student = doc.createElement('student')
    student.setAttribute('id', '123')

    name = doc.createElement('name')
    name.appendChild(doc.createTextNode('java'))
    student.appendChild(name)

    age = doc.createElement('age')
    age.appendChild(doc.createTextNode('10'))
    student.appendChild(age)

    root.appendChild(student)

    writer = open('student-list-new.xml', 'w', encoding='UTF-8')
    doc.writexml(writer, indent='\n', addindent='  ', encoding='UTF-8')


def update():
    doc = minidom.parse('student-list-new.xml')
    root = doc.documentElement
    print(root)
    print(root.tagName)

    student = doc.createElement('student')
    student.setAttribute('id', '100')

    name = doc.createElement('name')
    name.appendChild(doc.createTextNode('李白'))
    student.appendChild(name)

    age = doc.createElement('age')
    age.appendChild(doc.createTextNode('666'))
    student.appendChild(age)

    root.appendChild(student)

    writer = open('student-list-new.xml', 'w', encoding='UTF-8')
    doc.writexml(writer, indent='\n', addindent='  ', encoding='UTF-8')


# read()
# create()
update()