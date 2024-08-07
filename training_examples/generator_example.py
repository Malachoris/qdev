import time
from typing import Generator


# TODO: ADD generators

def process(x: list[int]) -> list[str]:
    out: list[str] = []
    for ind, elem in enumerate(x):
        new_elem = f"{ind}. {elem}"
        out.append(new_elem)
    return out


def process_gen(x: list[int]) -> Generator[str, None, None]:
    for ind, elem in enumerate(x):
        new_elem = f"{ind}. {elem}"
        yield new_elem


a = list(range(100000))
print(a[-10:])  # cant index generator
start = time.time()

# result = process(a)
result = process_gen(a)
end = time.time() - start
firs_value = next(result)
print(firs_value)
firs_value = next(result)
print(firs_value)
firs_value = next(result)
print(firs_value)

print(end)
print(result)
print("-" * 20)

for elem in result:
    print(elem)

# for elem in result:
#     print((elem))

# TODO: Generator is (when called next(result) goes in hits yield PAUSED
#  got value returned it
# TODO: you can make for loop and dont create a list
