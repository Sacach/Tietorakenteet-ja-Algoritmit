#include <stdio.h>
#include <stdlib.h>
#include "list.h"

/*
	Allocates a node with data key
	and inserts it in the head of linked list
*/ 
void list_insert(list *li, data_type key){
	node *n = (node *)malloc(sizeof(node));
	n->data = key;
	n->next=li->head;
	li->head = n;
}

/*
	Searches a node according to key
	and returns a pointer to found node
*/
pnode list_search(list li, data_type key){
	pnode pNode = li.head;
	int found = 0;
	
	while(pNode != 0 && found == 0){
		if(pNode->data == key){
			found = 1;
		}
		else {
			pNode = (pnode)pNode->next;
		}
	}
	
	return pNode;
}

/*
	Searches a node according to key
	and removes it from the list
*/
void list_remove(list *li,data_type key){
	pnode pNode = list_search(*li,key);
	
	if(pNode != 0){
		
		// Check if head node deleted
		if(pNode == li->head){
			li->head = pNode->next;
		}
		else {
			// Find predecessor
			pnode pred = li->head;
			
			while(pred->next != pNode){
				pred = pred->next;
			}
			
			pred->next = pNode->next;
		}
		
		// free memory
		free(pNode);
	}
}

// Prints a node
void print_node(pnode n){
	printf("%d",n->data);
}

// Prints the whole list
void print_list(list li){
	pnode pNode = li.head;
	while( pNode != 0){
		print_node(pNode);
		printf("\n");
		pNode = (pnode)pNode->next;
	}
}
