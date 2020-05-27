# Projeto Envia Email - Python
# Autor: Iuri Lopes Almeida
# Data: 27/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou a biblioteca
# 			 SMTPLib como base. Ele faz o envio de um email para o destinatário
# 			 escolhido, passando o assunto e a mensagem desejada.
# Forma de uso: python envia-email.py


# Importação necessária.
import smtplib


# Função responsável por fazer o envio do email.
# remetente -> email de quem está enviando o email.
# senhaRemetente -> senha de quem está enviando o email.
# destinatario -> email de quem está recebendo o email.
# assunto -> assunto do email.
# msg -> mensagem do email.
def sendEmail(remetente, senhaRemetente, destinatario, assunto, msg):

    # Tente fazer o envio do email.
    try:

        # Estabelecendo uma conexão com o servidor do Google.
        # Obs.: Outros servidores:
        #           . Yahoo -> smtp.mail.yahoo.com:465 ou 587
        #           . iCloud -> smtp.mail.me.com:587
        #           . Outlook, Hotmail -> smtp.office365.com:587
        # Link: https://support.office.com/pt-br/article/configura%C3%A7%C3%B5es-de-email-pop-e-imap-para-o-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353
        # Obs.: É insteressante dar uma olhada nesse link, pois
        #       nele também mostra os diferentes tipos de criptografia
        #       usadas em alguns dos servidores listados.
        servidor = smtplib.SMTP('smtp.gmail.com:587')

        # Fazer sua identificação para o servidor de email.
        servidor.ehlo()

        # Colocar essa conexão em modo TLS (Transfer Security Layer).
        # Obs.: TLS é um protocolo de segurança que faz a criptografia
        #       dos dados que estão sendo enviados do cliente (esse "código")
        #       para o servidor (servidor do Google).
        servidor.starttls()

        # Fazer o login no servidor com a conta que irá enviar o email.
        servidor.login(remetente, senhaRemetente)

        # Onde será montado do assunto e o corpo da mensagem que será enviada.
        # Obs.: O "Subject" está no texto para identificar qual será o assunto
        #       do email. Se caso vc decidir tirá-lo, seu email será enviado
        #       sem assunto.
        mensagem = 'Subject: {}\n\n{}'.format(assunto, msg)

        # Envie (de, para, essa mensagem).
        servidor.sendmail(remetente, destinatario, mensagem)

        # Saia do servidor.
        servidor.quit()

        # Imprima que tudo ocorreu bem.
        print("Email enviado!")

    # Se caso houve algum erro no envio, faça:
    except:

        # Imprima que ocorreu um erro.
        print("Erro ao enviar o email!")


# Função principal responsável por chamar as outras funções.
def main():

    # Passando os parâmetros necessários para fazer o envio do email.
    remetente = ""
    senhaRemetente = ""
    destinatario = ""
    assunto = "Testando o assunto."
    msg = "Testando a mensagem."

    # Chamando a função para fazer o envio do email.
    sendEmail(remetente, senhaRemetente, destinatario, assunto, msg)

    # Obs.: Para usar esse programa é interessante que vc crie uma nova conta
    #       de email para poder usá-la aqui, porque para esse programa ter a
    #       autonomia de fazer o envio do email é preciso que vc habilite a
    #       função "Acesso a app menos seguro" no Gmail. Para acessar essa
    #       função vc precisa entrar na sua conta de email > clicar no seu
    #       ícone de perfil > clicar em Gerenciar sua Conta do Google > clicar
    #       na área de busca e digitar "Acesso a app menos seguro" > e então
    #       é só ativar essa função. Você precisa ativar essa função porque
    #       o código terá que fazer o login na sua conta para enviar o email
    #       e como esse código não tem nenhuma credencial para fazer isso, é
    #       preciso que vc libere esse login remoto que ele fará. :)


if __name__ == "__main__":
    main()