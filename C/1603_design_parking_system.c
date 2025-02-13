typedef struct {
    int space[3];
} ParkingSystem;

ParkingSystem* parkingSystemCreate(int big, int medium, int small) {
    ParkingSystem *p;

    p = malloc(sizeof(ParkingSystem));
    if (p) {
        p->space[0] = big;
        p->space[1] = medium;
        p->space[2] = small;
    }
    return p;
}

bool parkingSystemAddCar(ParkingSystem* obj, int carType) {
    ParkingSystem *p = obj;
    int i = carType - 1;

    if (p && i >= 0 && i < sizeof(p->space) / sizeof(p->space[0]) && p->space[i]) {
        p->space[i]--;
        return true;
    }
    return false;
}

void parkingSystemFree(ParkingSystem* obj) {
    free(obj);
}

/**
 * Your ParkingSystem struct will be instantiated and called as such:
 * ParkingSystem* obj = parkingSystemCreate(big, medium, small);
 * bool param_1 = parkingSystemAddCar(obj, carType);
 
 * parkingSystemFree(obj);
*/
