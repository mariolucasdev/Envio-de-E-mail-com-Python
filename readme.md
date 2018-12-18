# Envio de E-mail autenticado com Python

Enivo de e-mail autenticado simples com python.

## Dependências

Sem dependências

## Detalhes
Envio básico com validação apenas de envio ou falha

## Configurações

É necessário importar o arquivo mainEmail.py que contém a função de envio
```py
    import mainEmail
```

main.py
```py
    email    = 'meu email'
    senha    = 'minha senha'
    emailTo  = 'email do destinatário'
    mensagem = 'mensagem'
    server   = 'servidor smtp'
```

## Função de Envio
```py
    mainEmail.sendEmail(email, emailTo, senha, mensagem, server)
```

## Retorno da Função

Caso funcione tudo certo a função irá retornar ```True``` caso exista alguma falha a função ira retornar ```False```

