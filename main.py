from data_structs.min_heap import MinHeap
from input_helpers import ask_for_n_and_k, ask_user_to_fill_array


def d_run_solution_with_prints(func):
    def inner(arr: [int], k: int):
        print(f"\n--------------------- {func.__name__} ---------------------\n")
        solution, counter = func(arr, k)
        print(f"The solution is {solution}\n\nIt took {counter} comparisons.\n")

    return inner


@d_run_solution_with_prints
def first_solution(arr: [int], k: int) -> ([int], int):
    print(f"The entire array: {arr}\n")
    min_heap = MinHeap(arr)
    k_sorted = [min_heap.heap_extract_min() for _ in range(k)]
    return k_sorted, min_heap.counter


@d_run_solution_with_prints
def second_solution(arr: [int], k: int) -> ([int], int):
    print(f"The entire array: {arr}\n")
    min_heap = MinHeap(arr)
    k_sorted = [min_heap.heap_extract_min() for _ in range(k)]
    return k_sorted, min_heap.counter


def main():
    n, k = ask_for_n_and_k()
    arr = ask_user_to_fill_array(n)

    first_solution(arr, k)
    second_solution(arr, k)


if __name__ == "__main__":
    main()
