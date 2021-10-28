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
   