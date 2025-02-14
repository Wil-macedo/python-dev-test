import asyncio
import time

# Função que simula uma chamada de rede com asyncio.sleep
async def networkCall(name, delay):
    print(f"Iniciando {name}...")
    await asyncio.sleep(delay)
    print(f"Finalizando {name} após {delay} segundos.")
    return delay

# Função assíncrona principal
async def main():
    start_time = time.time()  # Marca o tempo de início

    # Cria uma lista de tarefas assíncronas
    tasks = [
        networkCall("Chamada 1", 2),  # Simula 2 segundos de espera
        networkCall("Chamada 2", 3),  # Simula 3 segundos de espera
        networkCall("Chamada 3", 1),  # Simula 1 segundo de espera
    ]

    # Executa todas as chamadas de rede simultaneamente
    await asyncio.gather(*tasks)

    end_time = time.time()  # Marca o tempo de término
    total_time = end_time - start_time  # Calcula o tempo total
    print(f"\nTempo total de execução: {total_time:.2f} segundos")

# Executando o evento principal
if __name__ == "__main__":
    asyncio.run(main())
