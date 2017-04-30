## Function to create XML xs:elements from a list.

# Enter list of element names to convert to proper xs:elements
listNames = ["name1",
"name2","name3"]

def list_to_XML(listNames):
    xml_list =[]
    for nm in listNames:
        print('<xs:element name="'+str(nm)+ '"/>')
        xml_list.append('<xs:element name="'+str(nm)+ '"/>')

list_to_XML(listNames)

#if __name__ == '__main__':
#    list_to_XML(listNames)
