#Step1
def getFile():
  file = input('Please enter the file name with the extension : ')
  with open(file,'r') as f:
    text = f.read()
    lines = text.split('\n')
    return lines


#Step2
def findDomains(lines):
  i = 1
  domains = list()
  for email in lines:
    domain = email.split('@')
    print('Email',i,' : ',email)
    i+=1
    if not domain[1] in domains:
      domains.append(domain[1])
  return domains


#Step3
def domainsDic(emails,domains):
  dic = dict()
  for domain in domains:
    print('Domain selected : ',domain)
    lst = list()
    for email in emails:
      e = email.split('@')
      if e[1] == domain:
        lst.append(email)
        
    #delete the added emails
    for email in lst:
      emails.remove(email)
      print('Submitted --> ',email)
    
    dic[domain] = lst
  return dic



#Step4
def saveToFile(dic):
  
  for domain,emails in dic.items():
    with open(domain,'w') as f:
      for email in emails:
        print(f"Added to {domain} file --> {email}")
        f.write(email+'\n') 
  return 'Successfully done, check your directory...'





#ProgramPrincipal
emails = getFile()
domains = findDomains(emails)
dic = domainsDic(emails,domains)
print(saveToFile(dic))



