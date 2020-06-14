# Projeto Envia Email - Python e SMTPLib
# Autor: Iuri Lopes Almeida
# Data: 27/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou a biblioteca
#            SMTPLib como base. Ele faz o envio de um email para o destinatário
#            escolhido, passando o assunto e a mensagem desejada. Podendo também
#            fazer o envio de arquivos em anexo, como: pdf, imagens...
# Forma de uso: python envia-email.py


# Importação necessária.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


# Função responsável por fazer o envio do email com anexo.
# remetente -> email de quem está enviando o email.
# senhaRemetente -> senha de quem está enviando o email.
# destinatario -> email de quem está recebendo o email.
# titulo -> título do email.
# corpoMensagem -> assunto do email.
# nomeArquivo -> nome do arquivo que deseja enviar em anexo.
def sendEmailComAnexo(remetente, senhaRemetente, destinatario, titulo, corpoMensagem, nomeArquivo):

    # Tente fazer o envio do email.
    try:

        # Montando uma variável para receber todas as partes de uma mensagem em um email.
        msg = MIMEMultipart()

        # Passando o email do remetente, do destinatário e o título do email.
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = titulo

        # Juntando e organizando todas as partes informadas da mensagem com o corpo da
        # da mensagem passada.
        msg.attach(MIMEText(corpoMensagem, 'plain'))

        # Abrindo o arquivo onde terá as informações monitoradas pelo keylogger.
        # Obs.: O 'rt' significa que pode ser lido ('r') e que tem o valor de um
        #       texto ('t'), ou seja, que só contém texto dentro.
        # Obs.: Caso você deseja usar para enviar uma imagem/vídeo é interessante usar
        #       a extensão de binário ('b').
        anexo = open(nomeArquivo, 'rb')

        # Montando uma variável para receber as informações para fazer a codificação do anexo.
        anexoCod = MIMEBase('application', 'octet-stream')

        # Fazendo a leitura do anexo.
        anexoCod.set_payload((anexo).read())

        # Fazendo a codificação do anexo em base64.
        encoders.encode_base64(anexoCod)

        # Dizendo qual é o título do arquivo.
        anexoCod.add_header('Content-Disposition', "attachment; filename= " + nomeArquivo)

        # Juntando o anexo com a mensagem depois da codificação.
        msg.attach(anexoCod)

        # Fechando o arquivo.
        anexo.close()

        # Transformando tudo que tem em uma forma que a gente consiga ler.
        mensagem = msg.as_string()

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


# Função responsável por fazer o envio do email sem anexo.
# remetente -> email de quem está enviando o email.
# senhaRemetente -> senha de quem está enviando o email.
# destinatario -> email de quem está recebendo o email.
# assunto -> assunto do email.
# msg -> mensagem do email.
def sendEmailSemAnexo(remetente, senhaRemetente, destinatario, assunto, msg):

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
    # Obs.: Se caso vc queira fazer o envio para mais de uma pessoa, basta
    #       colocar o destinatário como um array de emails.
    #       Ex.: destinatario = ["teste01@gmail.com", "teste02@gmail.com", "teste03@gmail.com"]
    remetente = ""
    senhaRemetente = ""
    destinatario = ""
    assunto = "Testando o assunto."
    msg = "Testando a mensagem."

    # Chamando a função para fazer o envio do email sem anexo.
    # sendEmailSemAnexo(remetente, senhaRemetente, destinatario, assunto, msg)

    # Alguns outros parâmetros que serão usados na função sendEmailComAnexo().
    titulo = "Testando novo envio."
    corpoMensagem = "Esse é um teste do novo envio."
    nomeArquivo = "imagens/paisagem.jpg"

    # Chamando a função para fazer o envio do email sem anexo.
    # Obs.: Nessa função só é permetido fazer o envio para um destinatário, caso tente fazer
    #       com mais de um como na sendEmailSemAnexo(), seu email provavelmente não será enviado.
    sendEmailComAnexo(remetente, senhaRemetente, destinatario, titulo, corpoMensagem, nomeArquivo)

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