# ifmoradas

Desenvolvimento de um website com **Django (Python)** com o intuito de oferecer opções de moradias para estudantes do IFSC. Através do sistema é possível criar e procurar imóveis que estão disponíveis e entrar em contato caso tenham interesse. O sistema possui **autenticação**, **CRUD de imóveis** e foi desenvolvido como principal trabalho da disciplina de **Tópicos Especiais em Programação** para o curso de **Sistemas de Informação** do IFSC Caçador. Visite o projeto em [https://ifmoradas.anthonycruz.com.br](https://ifmoradas.anthonycruz.com.br)

![ifmoradas](https://i.imgur.com/ueunRCw.png)

# Instalação

O primeiro passo para a instalação é clonar o repositório. Para usar esse comando, você precisa especificar a URL do repositório remoto que deseja clonar. Uma vez que você execute este comando, o Git baixará todos os arquivos e histórico de commits do repositório remoto e criará uma cópia em sua máquina local.

``` git clone <URL> ```

Em seguida, você precisa instalar as bibliotecas. Quando você executa este comando, o pip (que é o instalador de pacotes para Python) lerá o arquivo "requirements.txt" e baixará e instalará todos os pacotes listados nele, juntamente com quaisquer dependências que esses pacotes possam ter.

``` pip install -r requirements.txt ```

As migrações devem ser realizadas para configurar o banco de dados. O comando "migrate" usa um histórico de migração para acompanhar as alterações feitas no esquema do banco de dados. Cada migração corresponde a uma alteração específica nos modelos e contém um conjunto de declarações SQL que implementam a alteração.

``` python manage.py migrate ```

Por fim, o projeto pode ser executado com o runserver. O comando "runserver" inicia um servidor web leve que aguarda solicitações em uma porta e endereço IP especificados. Por padrão, o servidor é executado na porta 8000 e escuta todas as interfaces de rede disponíveis. O servidor usa as configurações da aplicação Django para configurar o servidor.

``` python manage.py runserver ```

Assim que o servidor de desenvolvimento estiver em execução, você pode usar um navegador da web para acessar a aplicação no endereço e porta especificados. Quaisquer alterações feitas no código da aplicação ou nos modelos serão automaticamente recarregadas pelo servidor, facilitando o teste e a depuração da aplicação.