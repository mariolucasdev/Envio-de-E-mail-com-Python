import mainEmail

email    = 'meu email'
senha    = 'minha senha'
emailTo  = 'email do destinatário'
mensagem = 'mensagem'
server   = 'servidor smtp'

mainEmail.sendEmail(email, emailTo, senha, mensagem, server)
