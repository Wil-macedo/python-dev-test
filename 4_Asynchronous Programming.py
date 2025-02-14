import asyncio
from datetime import datetime
from time import sleep
# https://www.hashtagtreinamentos.com/programacao-assincrona-em-python?gad_source=1&gclid=CjwKCAiAzba9BhBhEiwA7glbao3vuTMd-NxhqnIXV7GnfsH0NO1dk-OLz0RZZxaqB3sw3qXAlaYg9BoCoAgQAvD_BwE


async def netCall(name:str, time:int):
    print(f"START: {name}")
    await asyncio.sleep(time)
    print(f"END: {name}")


async def main():

    start = datetime.now()
    
    # Agenda tarefa .
    tarefa1 = asyncio.create_task(netCall("tarefa_1", 8))
    tarefa2 = asyncio.create_task(netCall("tarefa_2", 4))
    tarefa3 = asyncio.create_task(netCall("tarefa_3", 2))
    tarefa4 = asyncio.create_task(netCall("tarefa_4", 1))

    print("END MAIN")

    await tarefa1  # Espera para encerrar.
    await tarefa2
    await tarefa3
    await tarefa4
    
    totalMs = (datetime.now() - start).total_seconds()
    print(f"TEMPO TOTAL ASSÍNCRONO: {totalMs}seg")

asyncio.run(main())


###########################################################################################################################


def syncNetCall(name:str, time:int):
    print(f"START: {name}")
    sleep(time)
    print(f"END: {name}")


def syncMain():

    start = datetime.now()
    
    syncNetCall("tarefa_1", 8)
    syncNetCall("tarefa_2", 4)
    syncNetCall("tarefa_3", 2)
    syncNetCall("tarefa_4", 1)

    print("END MAIN")
    
    totalMs = (datetime.now() - start).total_seconds()
    print(f"TEMPO TOTAL SÍNCRONO: {totalMs}seg")

syncMain()

# TEMPO TOTAL ASSÍNCRONO: 8.004379seg
# TEMPO TOTAL SÍNCRONO: 15.037259seg

# Da para notar o granho de performance é alto usando funções assíncronas.