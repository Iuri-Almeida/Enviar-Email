# Enviar Email

Programa que faz o envio de um email automaticamente.

# Descrição

Esse programa foi escrito na linguagem Python e usou a biblioteca <a href="https://docs.python.org/3/library/smtplib.html">SMTPLib</a> como base. Ele faz o envio de um email para o destinatário escolhido, passando o assunto e a mensagem desejada. Podendo também fazer o envio de arquivos em anexo, como: pdf, imagem...

<b>Obs.:</b> Caso queira fazer o envio de algum arquivo pdf ou imagem, por exemplo, é necessário fazer a alteração de <b>'rt'</b> para <b>'rb'</b> na <b>linha 48</b> do código.

# Como funciona?

O programa é dividio em duas funções: <b>sendEmailSemAnexo()</b> e <b>sendEmailComAnexo()</b>. A função <b>sendEmailSemAnexo()</b> faz o envio do email sem anexo e recebe como parâmetros o email do remetente, a senha do remetente (para poder fazer a autenticação no servidor), email do destinatário, assunto (opcional) e mensagem. Já a função <b>sendEmailComAnexo()</b> faz o envio do email com anexo e recebe como parâmetros o email do remetente, a senha do remetente (para poder fazer a autenticação no servidor), email do destinatário, titulo do email, a mensagem e o nome do arquivo que deseja enviar em anexo. A partir disso o programa envia o email do remetente para o destinatário escolhido.

<b>Obs.:</b> Todas as variáveis que as funções estão recebendo estão no final do código, dentro da função main(), que é a função que chama todas as outras funções.

<b>Obs.:</b> Caso vc queria usar diferentes servidores de emails, você consegue encontrar alguns dos principais servidores de email <a href="https://support.office.com/pt-br/article/configura%C3%A7%C3%B5es-de-email-pop-e-imap-para-o-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353">aqui</a>.

# Instalação

É preciso ter o Python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). As bibliotecas usadas nesse projeto já vem instaladas no Python, então só é preciso ter o Python instalado e importar pelo código (já está feito).

# Uso

Após a instalação, para começar a usar basta clonar esse repositório e digitar o comando <b>python envia-email.py</b> no terminal ou rodar pelo <a href="https://www.jetbrains.com/pt-br/pycharm/download/#section=mac">PyCharm</a>.

<b>Obs.:</b> Para usar esse programa é interessante que vc crie uma nova conta de email para poder usá-la aqui, porque para esse programa ter a autonomia de fazer o envio do email é preciso que vc habilite a função "Acesso a app menos seguro" no Gmail. Para acessar essa função vc precisa: <b>entrar na sua conta de email > clicar no seu ícone de perfil > clicar em Gerenciar sua Conta do Google > clicar na área de busca e digitar "Acesso a app menos seguro" > e então é só ativar essa função</b>. Você precisa ativar essa função porque o código terá que fazer o login na sua conta para enviar o email e como esse código não tem nenhuma credencial para fazer isso, é preciso que você permita esse login remoto que ele fará. :)