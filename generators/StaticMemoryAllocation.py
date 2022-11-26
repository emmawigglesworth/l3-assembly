class StaticMemoryAllocation():

    def __init__(self, global_vars: dict()) -> None:
        self.__global_vars = global_vars

    def generate(self):
        print('; Allocating Global (static) memory')
        for n in self.__global_vars:
            if self.__global_vars[n] is not None:
                # reserving memory
                print(f'{str(n+":"):<9}\t.WORD {str(self.__global_vars[n])}')
            else:
                print(f'{str(n+":"):<9}\t.BLOCK 2')  # reserving memory
