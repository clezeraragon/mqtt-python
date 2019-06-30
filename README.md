## Projeto inicial para conexão de dispositivos IOT

#### Este projeto visa realizar os dois metodos para comunicação com os dispositivos:

### Publish

``` command python publish.py ```

### Subscribe

``` command python subscribe.py ```

#### Para efeito de otimização e ambientização segue algumas etapas do projeto:

#### Precisamos instalar o mosquitto:

``` sudo apt-get install mosquitto ```

#### Precisamos instalar a biblioteca python paho-mqtt. Você precisa do 'pip3' para instalar este módulo, então se você ainda não fez isso, você precisará instalar pip3:

``` sudo apt-get install python3-pip ```

## Agora você pode instalar o paho-mqtt:

``` sudo pip3 install paho-mqtt ```

#### Você pode verificar a versão do seu python instalado dando o camando:

``` python -v ```

#### Na proxima etapa do projeto vou integra-lo com o django para realizar as presistências e iniciar as conexões



