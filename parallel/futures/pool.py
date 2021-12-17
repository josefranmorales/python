import logging
import queue
from concurrent.futures import ProcessPoolExecutor


logging.basicConfig(
	level=logging.DEBUG,
	format="%(processName)s %(message)s")


def is_even(number):
    return {'number': number, 'es par?': number % 2 == 0 }


if __name__ == '__main__':

    q = queue.Queue()

    for x in range(1, 15):
        q.put(x)

    with ProcessPoolExecutor(max_workers=2) as executor:
        while True:
            future = executor.submit(is_even, q.get())
            future.add_done_callback(
                lambda future: logging.info(f"Process_1: {future.result()}")
            )

            future = executor.submit(is_even, q.get())
            future.add_done_callback(
                lambda future: logging.info(f"Process_2: {future.result()}")
            )
            q.task_done()
