@REM Ambiente Virtual

@REM comando para criação deste ambiente isolado, deve ser executado na raiz do projeto.
python3 -m venv .venv 

@REM Caso o venv não esteja instalado, utilize o comando 
sudo apt install python3-venv

@REM Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, 
@REM pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.
source .venv/bin/activate

@REM Você pode conferir se o comando de ativação do ambiente virtual deu certo com o seguinte comando:
which python3

@REM O resultado será o caminho para a pasta onde você criou seu ambiente virtual ( pwd ), 
@REM acrescido de .venv/bin/python3 .

