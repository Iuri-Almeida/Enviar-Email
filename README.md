# Enviar Email

Programa que faz o envio de um email automaticamente.

# Descrição

Esse programa foi escrito na linguagem Python e usou a biblioteca <a href="https://docs.python.org/3/library/smtplib.html">SMTPLib</a> como base. Ele faz o envio de um email para o destinatário escolhido, passando o assunto e a mensagem desejada. 

# Como funciona?

O programa recebe como parâmetros o email do remetente, a senha do remetente (para poder fazer a autenticação no servidor), email do destinatário, assunto (opcional) e mensagem. A partir disso ele envia a mensagem de e para o email escolhido.

<b>Obs.:</b> As variáveis responsáveis por passar os emails, senha, assunto e mensagem estão no final do código, dentro da função main(), que é a função que chama a o programa.

<b>Obs.:</b> Caso vc queria usar diferentes servidores de emails, você consegue encontrar alguns dos principais servidores de email <a href="https://support.office.com/pt-br/article/configura%C3%A7%C3%B5es-de-email-pop-e-imap-para-o-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353">aqui</a>.

# Instalação

É preciso ter o Python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). A única biblioteca usada nesse projeto já vem instalada no Python, então só é preciso ter o Python instalado e importar pelo código (já está feito).

# Uso

Após as instalações, para começar a usar basta clonar esse repositório e digitar o comando <b>python envia-email.py</b> no terminal ou rodar pelo <a href="https://www.jetbrains.com/pt-br/pycharm/download/#section=mac">PyCharm</a>.

<b>Obs.:</b> Para usar esse programa é interessante que vc crie uma nova conta de email para poder usá-la aqui, porque para esse programa ter a autonomia de fazer o envio do email é preciso que vc habilite a função "Acesso a app menos seguro" no Gmail. Para acessar essa função vc precisa: <b>entrar na sua conta de email > clicar no seu ícone de perfil > clicar em Gerenciar sua Conta do Google > clicar na área de busca e digitar "Acesso a app menos seguro" > e então é só ativar essa função</b>. Você precisa ativar essa função porque o código terá que fazer o login na sua conta para enviar o email e como esse código não tem nenhuma credencial para fazer isso, é preciso que você permita esse login remoto que ele fará. :)