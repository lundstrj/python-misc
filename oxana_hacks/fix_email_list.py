import sys


f = open('emails.txt', 'r')
q = open('emails_out.txt', 'w')
cont = f.read().split('\n')
keep = []
for row in cont:
  if row == "":
    pass
  elif ';' in row:
    # handle it
    emails = row.split(';')
    for email in emails:
      q.write(email+'\n')
      keep.append(email)
  else:
    q.write(row+'\n')
    keep.append(row)
f.close()
q.close()
