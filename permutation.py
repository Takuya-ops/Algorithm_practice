from typing import List, Iterator


def all_perms(elements: List[int]) -> Iterator[List[int]]:
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == "__main__":
    for p in all_perms([1, 2, 3]):
        print(p)
