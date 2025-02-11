struct Node {
    int val;
    struct Node *next;
    struct Node *prev;
};

typedef struct {
    size_t size;
    struct Node *head;
} MyLinkedList;

MyLinkedList* myLinkedListCreate() {
    MyLinkedList *list;

    list = malloc(sizeof(MyLinkedList));
    if (list) {
        list->size = 0;
        list->head = NULL;
    }
    return list;
}

static struct Node *myLinkedListFindNode(MyLinkedList* obj, int index, int bSafe) {
    MyLinkedList *list = obj;
    struct Node *node;
    int i, upper_limit;

    if (!list)
        return NULL;

    upper_limit = (bSafe) ? list->size : list->size + 1;
    if (list->head && (index >= 0 && index < upper_limit)) {
        node = list->head;
        /* minor list traversal optimization */
        if (index <= (list->size / 2)) {
            for (i = 0; i < index; ++i)
                node = node->next;
        } else {
            for (i = 0; i < list->size - index; ++i)
                node = node->prev;
        }
        return node;
    }
    return NULL;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    MyLinkedList *list = obj;
    struct Node *node;

    if (list) {
        node = myLinkedListFindNode(list, index, 1 /*SAFE*/);
        if (node)
            return node->val;
    }
    return -1;
}

static struct Node *allocNode(int val, struct Node *next, struct Node *prev) {
    struct Node *node;

    node = malloc(sizeof(*node));
    if (node) {
        node->val = val;
        node->next = next;
        node->prev = prev;
    }
    return node;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    MyLinkedList *list = obj;
    struct Node *node;

    if (list) {
        if (!list->head) {
            list->head = allocNode(val, NULL, NULL);
            if (!list->head)
                return;
            list->head->next = list->head;
            list->head->prev = list->head;
        } else {
            node = allocNode(val, list->head, list->head->prev);
            if (!node)
                return;
            list->head->prev->next = node;
            list->head->prev = node;
            list->head = node;
        }
        list->size++;
    }
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    MyLinkedList *list = obj;
    struct Node *node;

    if (list) {
        if (!list->head) {
            myLinkedListAddAtHead(list, val);
        } else {
            node = allocNode(val, list->head, list->head->prev);
            if (!node)
                return;
            list->head->prev->next = node;
            list->head->prev = node;
            list->size++;
        }
    }
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    MyLinkedList *list = obj;
    struct Node *node;
    struct Node *new_node;

    /* according to the spec index can be equal list size */
    if (list && (index >= 0 && index <= list->size)) {
        if (!list->head || index == 0) {
            myLinkedListAddAtHead(list, val);
        } else {
            node = myLinkedListFindNode(list, index, 0 /*UNSAFE*/);
            new_node = allocNode(val, node, node->prev);
            if (new_node) {
                node->prev->next = new_node;
                node->prev = new_node;
                list->size++;
            }
        }
    }
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    MyLinkedList *list = obj;
    struct Node* node;

    if (list) {
        if (list->head && (index >= 0 && index < list->size)) {
            node = myLinkedListFindNode(list, index, 1 /*SAFE*/);
            if (list->size > 1) {
                node->prev->next = node->next;
                node->next->prev = node->prev;
                if (node == list->head)
                    list->head = node->next;
                free(node);
            } else {
                /* this is the last node */
                free(list->head);
                list->head = NULL;
            }
            list->size--;
        }
    }
}

void myLinkedListFree(MyLinkedList* obj) {
    MyLinkedList *list = obj;

    if (list) {
        while (list->size > 0)
            myLinkedListDeleteAtIndex(list, 0);
        free(list);
    }
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/
