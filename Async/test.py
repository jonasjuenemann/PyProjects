import asyncio
import time

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    # time.sleep(2) -> hierauf würde das komplette Programm warten!
    print("done")
    return {"data": 1}


async def print_numbers():
    for i in range(15):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data()) # task -> a Future -> ähnlich wie Promise in JS
    task2 = asyncio.create_task(print_numbers())  # Man könnte die Funktion auch ohne dies callen, das würde aber den Sinn verfehlen, da diese dann wieder nacheinander ausgeführt werden würden
    # await print_numbers() # würde auch gehen

    value = await task1  # ohne await:main() finished direkt, die erwarteten task werden gar nicht gemacht. value ist lediglich ein pending objekt
    # sehr ähnlich promises in javascript
    print(value)
    await task2  # so wird task2 auch nach task1 zu Ende ausgeführt


# main() kann man nicht einfach so laufen lassen

asyncio.run(main())
