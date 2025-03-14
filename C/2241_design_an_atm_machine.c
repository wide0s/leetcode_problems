#define BANKNOTES (5)

typedef struct {
    int funds[BANKNOTES];
} ATM;

static const int banknotes[] = {20, 50, 100, 200, 500};

ATM* aTMCreate() {
    return calloc(1, sizeof(ATM));
}

void aTMDeposit(ATM* obj, int* banknotesCount, int banknotesCountSize) {
    if (!obj || !banknotesCount || !banknotesCountSize)
        return;

    for (int i = 0; i < banknotesCountSize; i++)
        obj->funds[i] += banknotesCount[i];
}

static inline int min(int a, int b) {
    return a > b ? b : a;
}

int* aTMWithdraw(ATM* obj, int amount, int* retSize) {
    int *transaction, q;

    if (!obj || !retSize) {
	if (retSize)
	    *retSize = 0;
        return NULL;
    }

    transaction = calloc(BANKNOTES, sizeof(int));
    if (!transaction) {
        *retSize = 0;
        return NULL;
    }

    for (int i = BANKNOTES - 1; i >= 0; i--) {
        q = min(amount / banknotes[i], obj->funds[i]);
        if (obj->funds[i] >= q) {
            obj->funds[i] -= q;
            amount -= q * banknotes[i];
            transaction[i] = q;
        }
    }

    if (amount) {
        aTMDeposit(obj, transaction, BANKNOTES);
        transaction[0] = -1;
        *retSize = 1;
        return transaction;
    }

    *retSize = BANKNOTES;
    return transaction;
}

void aTMFree(ATM* obj) {
    free(obj);
}

/**
 * Your ATM struct will be instantiated and called as such:
 * ATM* obj = aTMCreate();
 * aTMDeposit(obj, banknotesCount, banknotesCountSize);
 
 * int* param_2 = aTMWithdraw(obj, amount, retSize);
 
 * aTMFree(obj);
*/
