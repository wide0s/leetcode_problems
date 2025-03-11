#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int minCostToMoveChips(int* position, int positionSize) {
    int i, even_chips, odd_chips;
    if (!position || positionSize < 2)
        return 0;
    for (i = 0, even_chips = 0; i < positionSize; i++)
        if (position[i] % 2 == 0)
            even_chips++;
    odd_chips = positionSize - even_chips;
    return odd_chips < even_chips ? odd_chips : even_chips;
}

int main(int argc, char **argv) {
    int positions1[] = {2, 2, 2, 3, 3};
    int positions2[] = {1, 2, 3};
    int positions3[] = {1, 1000000000};
    assert(minCostToMoveChips(positions1, 5) == 2);
    assert(minCostToMoveChips(positions2, 3) == 1);
    assert(minCostToMoveChips(positions3, 2) == 1);
    return 0;
}
