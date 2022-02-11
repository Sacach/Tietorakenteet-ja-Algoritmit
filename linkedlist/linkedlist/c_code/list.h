#ifndef LIST_H_INCLUDED
#define LIST_H_INCLUDED

// Defines data to store in list
typedef int data_type;

// Defines node and its pointer
typedef struct nd {
	data_type data;
	struct nd* next;
} node, *pnode; 

// Defines linked list
typedef struct lst {
	pnode head;
} list; 

// Inserts key in the list
void list_insert(list *li, data_type key);

// Searches key from the list
pnode list_search(list li, data_type key);

// Removes key from the list
void list_remove(list *li,data_type key);

// Prints the list
void print_list(list li);

#endif