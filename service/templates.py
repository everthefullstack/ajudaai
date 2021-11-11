def template_recuperacao_senha_1():
    return """
        <!DOCTYPE html>
        <html lang="PT-BR">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Recuperação de senha</title>
        </head>
        <body>
            <div>
                <p>Clique no link abaixo para receber uma nova senha por email:</p>
                <p><a href="@url/trocar_senha/@token">Receber minha senha</a></p>
            </div>
        </body>
        </html>
    """

def template_recuperacao_senha_2():
    return """
        <!DOCTYPE html>
        <html lang="PT-BR">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Recuperação de senha</title>
        </head>
        <body>
            <div>
                <p>sua nova senha é: @senha</p>
        </body>
        </html>
    """

def template_edicao_evento():
    return """
        <!DOCTYPE html>
        <html lang="PT-BR">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Evento alterado!</title>
        </head>
        <body>
            <div>
                <p>O evento @nomeevento que você está participando sofreu mudanças.</p>
                <p>Visite nossa plataforma para saber mais sobre.</p>
            </div>
        </body>
        </html>
    """

def template_excluir_evento():
    return """
        <!DOCTYPE html>
        <html lang="PT-BR">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Evento cancelado!</title>
        </head>
        <body>
            <div>
                <p>O evento @nomeevento que você estava participando foi cancelado.</p>
                <p>Caso necessário, entre em contato com o criador do evento para saber mais.</p>
                <p>Contatos do criador:</p>
                <div>
                    Nome: @nomecriador <br>
                    Email: @telefonecriador <br>
                    Telefone: @emailcriador
                </div>
            </div>
        </body>
        </html>
    """