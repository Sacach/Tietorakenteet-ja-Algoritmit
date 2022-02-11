#include <stdio.h>
#include "list.h"

int main(){
	
	// Empty linked list
	list coll;
	coll.head=0;
	
	int i;
	
	// Insert keys 0,1,...,9 into the list
	for(i=0; i<10; i++){
		list_insert(&coll,i);
	}
	
	printf("Original list:\n");
	print_list(coll);
	
	printf("\nList after removing even keys:\n");
	// Remove even keys from the list
	for(i=0; i<10; i+=2){
		list_remove(&coll,i);
	}
	
	print_list(coll);
	
	printf("\nList after removing odd keys:\n");
	// Remove odd keys from the list
	for(i=9; i>0; i-=2){
		list_remove(&coll,i);
	}
	
	print_list(coll);
	
	return 0;
}