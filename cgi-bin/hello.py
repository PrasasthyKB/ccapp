#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
agent_id = form.getvalue('agent_id')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello from CGI Program</title>"
print "</head>"
print "<body><br><br>"
print "<p>Printing data for agent ID <b>%s<b></p>" % (agent_id)
print "</body>"
print "</html>"
