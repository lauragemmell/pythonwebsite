import mandrill
 
mandrill_client = mandrill.Mandrill('9FdJjzfupPJojkDcNiv4jA')
 
mandrill_client.messages.send(
    message={
        'html': '<p>Hello from Mandrill!</p>',
        'from_email': 'laura-gemmell@hotmail.com',
        'to': [{'email': 'andynwalker@hotmail.com', 'name': 'Example', 'type': 'to'}]
    }
)