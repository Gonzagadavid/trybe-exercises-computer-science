import requests
import time

# Rate Limit

# # À partir da décima requisição somos bloqueados de acessar o recurso
# # Código de status 429: Too Many Requests
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)
# Neste exemplo, após a décima requisição, o servidor começa a nos retornar respostas com o código de status 429 , "Too Many Requests". 
# Isto significa que estamos utilizando uma taxa de solicitação maior que a suportada. Ele permanecerá assim por algum tempo (1 minuto).

# Uma boa prática é sempre colocarmos um uma pausa entre as requisições, ou lote delas, mesmo que o website, onde a informação está,
# não faça o bloqueio, assim evitamos tirar o site do ar.
# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response)
    time.sleep(6)


# Timeout

# Por 10 segundos não temos certeza se a requisição irá retornar
response = requests.get("https://httpbin.org/delay/10")
print(response)



try:
    # recurso demora muito a responder
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.ReadTimeout:
    # vamos fazer uma nova requisição
    response = requests.get("http://httpbin.org/delay/1", timeout=2)
finally:
    print(response.status_code)